from flask import Flask, render_template, session, redirect, url_for
import redis
import psycopg2

app = Flask(__name__)
app.secret_key = 'super_game_super_secure_key'

# Redis کنکشن
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# PostgreSQL کنکشن
conn = psycopg2.connect("dbname=supergame_db user=postgres")
cur = conn.cursor()

@app.route('/')
def home():
    return "<h1>Welcome to Super Game</h1><a href='/upgrade'>Go to Upgrades</a>"

@app.route('/upgrade')
def upgrade():
    if session.get('video_count', 0) >= 2:
        return """
<html>
<head>
<style>
body { background-color: #0f0f0f; font-family: sans-serif; color: white; padding: 20px; }
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }
.card { padding: 40px; border-radius: 30px; color: white; text-decoration: none; display: block; box-shadow: 0 10px 20px rgba(0,0,0,0.5); transition: scale(1.05); }
.red-theme { background: linear-gradient(to right, #ff416c, #ff4b2b); }
.glacier-theme { background: linear-gradient(to right, #e0eafc, #cfdef3); color: #333; }
.green-theme { background: linear-gradient(to right, #56ab2f, #a8e063); }
.blue-theme { background: linear-gradient(to right, #00c6ff, #0072ff); }
h1 { margin-bottom: 40px; text-shadow: 0 0 10px #fff; }
</style>
</head>
<body>
<h1>SELECT YOUR UPGRADE</h1>
<div class="grid">
<a href="/upgrade/red" class="card red-theme">🔥 RED FIRE GUN</a>
<a href="/upgrade/glacier" class="card glacier-theme">🧊 GLACIER ICE GUN</a>
<a href="/upgrade/green" class="card green-theme">🌿 NEON GREEN GUN</a>
<a href="/upgrade/blue" class="card blue-theme">💧 AQUA BLUE GUN</a>
</div>
</body>
</html>
"""
    else:
        return redirect(url_for('watch_tasks'))

@app.route('/upgrade/<type>')
def upgrade_type(type):
    return f"<body style='background:#0f0f0f; color:white; padding:50px;'><h1>{type.upper()} UPGRADE SUCCESSFUL!</h1><a href='/upgrade'>Back</a></body>"

@app.route('/watch_tasks')
def watch_tasks():
    count = session.get('video_count', 0)
    return f"<body style='background:#121212; color:white; text-align:center; padding-top:50px;'><h1>Watch 2 videos to unlock upgrades!</h1><p>Videos watched: {count}</p><a href='/watch_video'>Watch Video</a></body>"

@app.route('/watch_video')
def watch_video():
    session['video_count'] = session.get('video_count', 0) + 1
    cache.set('last_video_watched', 'yes')
    return """
<html>
<head><style>body { background:#121212; color:white; text-align:center; padding-top:50px; font-family:sans-serif; }</style></head>
<body>
<h1>Watching Video...</h1>
<h2 id="timer">Please wait: 05:00</h2>
<div id="back-div" style="display:none;">
<a href="/watch_tasks" style="background:#4caf50; padding:15px 30px; color:white; text-decoration:none; border-radius:10px;">Back to Task List</a>
</div>
<script>
let time = 300;
let timerEl = document.getElementById('timer');
let backDiv = document.getElementById('back-div');
let interval = setInterval(() => {
    time--;
    let mins = Math.floor(time / 60);
    let secs = time % 60;
    timerEl.innerText = "Please wait: " + (mins < 10 ? "0" + mins : mins) + ":" + (secs < 10 ? "0" + secs : secs);
    if(time <= 0) {
        clearInterval(interval);
        timerEl.style.display = 'none';
        backDiv.style.display = 'block';
    }
}, 1000);
</script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(port=5000)
