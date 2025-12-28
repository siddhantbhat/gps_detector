from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>📍 GPS Detector Running</h2><p>Open <a href='/map'>/map</a></p>"

# Optional API (kept for future use / merging)
@app.route("/api/ping")
def ping():
    return jsonify({
        "status": "ok",
        "time": datetime.now().isoformat()
    })

@app.route("/map")
def show_map():
    return render_template("map.html")

if __name__ == "__main__":
    print("🚀 GPS Detector running at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

