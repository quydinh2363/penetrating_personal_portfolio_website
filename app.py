from flask import Flask, render_template, request
import database, hashlib

dtb = database.DATABASE()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('mypage.html')

@app.route('/login.html', methods = ['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        checker = dtb.log_in(username,password)
        if checker:
            return render_template('portfolio.html')
        else:
            message = "Incorrect username or password"

    return render_template('login.html',message=message)

bad_chars= ["'",";","--","#","or"]

def black_list(s):
    for char in bad_chars:
        if char in s.lower():
            return True
    return False

def check_match_password(password, confirm_password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    confirm_password_hash = hashlib.sha256(confirm_password.encode()).hexdigest()
    if password_hash == confirm_password_hash:
        return True
    else:
        return False


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        if black_list(username):
          message = "??? Don't do that, your mom will sad!"
          return render_template('register.html', message=message)     
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        confirm_password_checker = check_match_password(password,confirm_password)
        if confirm_password_checker == False:
            message = "Password doesn't match!"
            return render_template('register.html', message=message) 
        user_checker = dtb.sign_up(username, confirm_password)
        if user_checker == False:
            message = "Username already exist!"
        else:
            return render_template('login.html')
    return render_template('register.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)