from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup():
    return render_template('user_signup.html', title='User Signup')

@app.route('/', methods=['POST'])
def index():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) == 0:
        username_error = 'Please enter a username.'
    elif len(username) > 20 or len(username) < 3:
        username_error = 'Please enter a username between 3 and 20 characters long.'
    elif ' ' in username:
        username_error = 'Username cannot contain any spaces.'

    if len(password) == 0:
        password_error = 'Please enter a password.'
    elif len(password) > 20 or len(password) < 3:
        password_error = 'Please enter a password between 3 and 20 characters long.'
    elif ' ' in password:
        password_error = 'Password cannot contain any spaces.'

    if password != verify:
        verify_error = 'Please re-enter the password'

    if email:
        if '@' not in email or '.' not in email or ' ' in email or email.count('@') > 1 or email.count('.') > 1  or len(email) > 20 or len(email) < 3:
            email_error = 'Please enter a valid email address between 3 and 20 characters long.'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('user_signup.html', username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error, username = username, email = email)

#@app.route('/welcome', methods=['POST'])
#def signup():
#    username = request.post('username')
#    return render_template('welcome.html', username=username, title='Thank You!')

app.run()