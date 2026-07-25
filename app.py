from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'fx_master_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/watch')
def watch_video():
    session['watched'] = True
    return "<h1>Video watched! Now you can download.</h1><br><a href='/'>Go back</a>"

@app.route('/download')
def download_file():
    if session.get('watched'):
        return "<h1>Download starting...</h1>"
    else:
        return "<h1>Please watch the video first!</h1><br><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(port=5000)
