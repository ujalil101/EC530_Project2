from flask import Flask, render_template, request, redirect, url_for, session, send_file
from Modules.authorization import insert_user_data, verify_credentials
from Modules.file_uploader import save_pdf
from Modules.nlp_analysis import analyze_uploaded_pdf
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # get data from signup html 
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # checking if passwords are same 
        if password != confirm_password:
            return render_template('signup.html', error="Passwords do not match")

        # insert data into mongo module
        try:
            insert_user_data(username, password)
            return redirect(url_for('login'))  
        except Exception as e:
            return render_template('signup.html', error="Error occurred during signup. Please try again.")

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Checking if username and password are valid
        if verify_credentials(username, password):
            session['username'] = username  # Set the username in the session
            return redirect(url_for('upload_file'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url) 
        file = request.files['file'] # get file
        if file.filename == '':
            return redirect(request.url)
        if file:
            username = session.get('username') # get username to associate with 
            if not username:
                return redirect(url_for('login'))
            saved_file_path = save_pdf(file, username) # to put pdf with associuated username in DB 
            if isinstance(saved_file_path, str):
                summary, sentiment, keywords = analyze_uploaded_pdf(saved_file_path)
                return redirect(url_for('result', summary=summary, sentiment=sentiment, keywords=keywords)) # return summary, sentiment, keywords for pdf
            else:
                return render_template('upload.html', error="Error saving the file.") # return error
        else:
            return render_template('upload.html', error="Invalid file format. Please upload a PDF file.") # return error
    return render_template('upload.html')

# returns the result of uploading pdf
@app.route('/result') 
def result():
    summary = request.args.get('summary')
    sentiment = request.args.get('sentiment')
    keywords = request.args.get('keywords')
    return render_template('result.html', summary=summary, sentiment=sentiment, keywords=keywords)

# for testing
@app.route('/success')
def success():
    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

