from flask import Flask, render_template, session
import redis, sqlite3

app = Flask(__name__)
app.secret_key = 'super_game_super_secure_key'

cache = redis.StrictRedis(host='localhost', port=6379, db=0)
conn = sqlite3.connect('supergame.db', check_same_thread=False)
cur = conn.cursor()

@app.route('/')
def home():
    return render_template('gameplay.html')

@app.route('/start_battle')
def start_battle():
    return "<h1>FX Master Battle Started!</h1><br><a href='/'>Go Back</a>"

@app.route('/upgrade')
def upgrade():
    return render_template('upgrade.html')

if __name__ == '__main__':
    app.run(port=8080)
