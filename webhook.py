import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system('git pull origin main')
    os.system('pm2 restart all')
    return 'Updated Successfully', 200

if __name__ == '__main__':
    app.run(port=5000)
