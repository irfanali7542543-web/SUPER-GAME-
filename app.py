from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gameplay.html')

@app.route('/start_battle')
def start_battle():
    return render_template('battle.html')

if __name__ == '__main__':
    app.run(port=8080)
