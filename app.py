from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve videos
@app.route('/video/<filename>')
def serve_video(filename):
    return send_from_directory('static/videos', filename)

# Route to download files
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/downloads', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
