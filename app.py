from flask import Flask, render_template, request, redirect, url_for, session
from Modules.authorization import insert_user_data, verify_credentials
from Modules.file_uploader import save_pdf

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # checking if username and pwd in db 
        if verify_credentials(username, password):
            session['username'] = username  #set the username in the session
            return redirect(url_for('upload_file'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

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

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        username = session.get('username')  # get username from session
        if not username:
            return redirect(url_for('login'))  # go to login if user is not logged in
        if file.filename == '':
            return redirect(request.url)
        if file and save_pdf(file, username):
            return redirect(url_for('success'))
        else:
            return render_template('upload.html', error="Invalid file format. Please upload a PDF file.")
    return render_template('upload.html')


@app.route('/success')
def success():
    return "File uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)
