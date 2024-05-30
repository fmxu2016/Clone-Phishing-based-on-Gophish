from flask import Flask, request, redirect, url_for, render_template_string
from pyngrok import ngrok

app = Flask(__name__)

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
        # In actual application, verification will be carried out here
        return 'Logged in as {}'.format(username)
    return render_template_string(login_form)

if __name__ == '__main__':
    # Authenticate ngrok
    ngrok.set_auth_token('no')

    # Start ngrok tunnel
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))

    # Start Flask app
    app.run(port=5000)
