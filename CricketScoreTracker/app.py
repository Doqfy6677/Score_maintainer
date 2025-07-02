from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import json
import socket

# Create Flask app
app = Flask(__name__)
# Set to False in production
app.config['DEBUG'] = False

# This is important for Vercel deployment
app.config['PREFERRED_URL_SCHEME'] = 'https'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/api/teams', methods=['GET'])
def get_teams():
    # This is just a placeholder - in a real app, you'd fetch from a database
    # For now, we'll return an empty list as the data will be managed client-side
    return jsonify({"teams": []})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/static/service-worker.js')
def service_worker():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'service-worker.js', mimetype='application/javascript')

def get_ip_address():
    """Get the local IP address of the machine"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Get port from environment variable for deployment platforms
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    ip_address = get_ip_address()
    print(f"Cricket Score Tracker is running!")
    print(f"Access locally at: http://127.0.0.1:{port}")
    print(f"Access from other devices on the same network at: http://{ip_address}:{port}")
    # In production, debug should be False
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=port)