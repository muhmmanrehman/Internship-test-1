from flask import Flask
import os
import datetime
import pytz
import subprocess
app = Flask(__name__)
@app.route('/htop')
def htop():
    full_name = "Mohammed Abdul Rahman"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {e}"
    response = f"""
    <html>
    <head><title>HTop Data</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>TOP Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
