#signup includes 4 different fields, ending with a submit statement:
#--------Username field
#--------Password field
#--------Verify Password field
#--------Email (optional) field

#once the form is created then I need to: 
#--------validate the input and if correct redirect them to a webpage
#--------or provide error info if input=invalid

#if input is invalid:
#--------preserve the input fields except for the password
#--------each feedback message should be next to the field where the issue is

#if input is valid:
#--------show the user a Welcome page that displays: "Welcome, [username]!"

#what needs to validate:
#--------username/password should be b/w 3-20 characters and no spaces
#--------password and password must match
#--------must have a valid email meaning including the @ symbol 


from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup")
def index():
    return render_template('index.html') #username_error = "", password_error = "")

def char_length(word):
    if " " in word:
        return True
    if 3< len(word) <20:
        return False
    else:
        return True

def password_check(word, verify_word):
    if word == verify_word:
        return False
    else:
        return True

def email_check(word):
    if char_length(word):
        return True
    elif "@" not in word:
        return True
    elif "." not in word:
        return True
    else:
        return False

@app.route("/signup", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email_optional = request.form['email_optional']
    
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_optional_error = ''

    if char_length(username):
        username_error = 'Username must not contain a space and be between 3-20 characters long' 
    
    if char_length(password):
        password_error = 'Password must not contain a space and be between 3-20 characters long'
    
    if password_check(password, verify_password):
        verify_password_error = 'Passwords must match'
    
    if email_check(email_optional):
        email_optional_error= 'Email must not contain a space and be between 3-20 in length and contain a @ and .'

    if not username_error and not password_error and not verify_password_error:
        return render_template('Welcome_greeting.html', name=username)
    
    else:
        return render_template('index.html', username=username, email_optional=email_optional,
                    password_error=password_error, username_error=username_error, 
                    verify_password_error=verify_password_error, email_optional_error=email_optional_error)

app.run()
