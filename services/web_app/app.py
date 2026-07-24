from flask import Flask, render_template

app = Flask(__name__)

signals = [
    {"pair": "EUR/USD", "type": "BUY", "entry": "1.0850", "tp": "1.0900", "sl": "1.0820", "status": "Active"},
    {"pair": "GBP/USD", "type": "SELL", "entry": "1.2650", "tp": "1.2600", "sl": "1.2680", "status": "Pending"}
]

@app.route('/')
def home():
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
