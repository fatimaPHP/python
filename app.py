from flask import Flask, render_template, request, session, url_for, redirect, make_response
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        response = make_response('Login Success!', 200)
        response.headers['Content-Type'] = 'text/plain'
        session['username'] = request.form.get('username')

    return render_template('guess.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


