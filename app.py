from flask import Flask, render_template, request, redirect, url_for
from mongo import insert_user_data, verify_credentials

app = Flask(__name__)

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
            return redirect(url_for('success'))
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
            return redirect(url_for('login'))  # go to success (will redirect later)
        except Exception as e:
            return render_template('signup.html', error="Error occurred during signup. Please try again.")

    return render_template('signup.html')

@app.route('/success')
def success():
    return "Sign up successful!"

if __name__ == '__main__':
    app.run(debug=True)
