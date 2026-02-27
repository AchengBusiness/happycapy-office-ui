#!/usr/bin/env python3
"""HappyCapy Office UI - Backend State Service"""

from flask import Flask, jsonify, send_from_directory, make_response
from datetime import datetime
import json
import os
import fcntl
import threading

# Paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")
STATE_FILE = os.path.join(ROOT_DIR, "state.json")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/static")

# 文件锁
file_lock = threading.Lock()

# Default state
DEFAULT_STATE = {
    "state": "idle",
    "detail": "等待任务中...",
    "progress": 0,
    "updated_at": datetime.now().isoformat()
}


def load_state():
    """Load state from file with proper locking."""
    with file_lock:
        state = None
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r", encoding="utf-8") as f:
                    fcntl.flock(f.fileno(), fcntl.LOCK_SH)
                    try:
                        state = json.load(f)
                    finally:
                        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            except Exception:
                state = None

        if not isinstance(state, dict):
            state = dict(DEFAULT_STATE)

        # Auto-idle mechanism
        try:
            ttl = int(state.get("ttl_seconds", 25))
            updated_at = state.get("updated_at")
            s = state.get("state", "idle")
            working_states = {"writing", "researching", "executing"}
            if updated_at and s in working_states:
                dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
                if dt.tzinfo:
                    from datetime import timezone
                    age = (datetime.now(timezone.utc) - dt.astimezone(timezone.utc)).total_seconds()
                else:
                    age = (datetime.now() - dt).total_seconds()
                if age > ttl:
                    state["state"] = "idle"
                    state["detail"] = "待命中（自动回到休息区）"
                    state["progress"] = 0
                    state["updated_at"] = datetime.now().isoformat()
                    try:
                        save_state_internal(state)
                    except Exception:
                        pass
        except Exception:
            pass

        return state


def save_state_internal(state: dict):
    """Save state to file (internal, assumes lock is held)"""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            json.dump(state, f, ensure_ascii=False, indent=2)
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def save_state(state: dict):
    """Save state to file with locking"""
    with file_lock:
        save_state_internal(state)


# Initialize state
if not os.path.exists(STATE_FILE):
    save_state(DEFAULT_STATE)


@app.after_request
def add_headers(response):
    """Add CORS and cache headers"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    # Allow cross-origin for images (required for WebGL/Canvas)
    response.headers['Cross-Origin-Resource-Policy'] = 'cross-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'credentialless'
    return response


@app.route("/", methods=["GET"])
def index():
    """Serve the pixel office UI"""
    response = make_response(send_from_directory(FRONTEND_DIR, "index.html"))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@app.route("/cad", methods=["GET"])
def cad_view():
    """Serve the CAD floor plan UI"""
    response = make_response(send_from_directory(FRONTEND_DIR, "index_cad.html"))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@app.route("/status", methods=["GET"])
def get_status():
    """Get current state"""
    state = load_state()
    response = jsonify(state)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


if __name__ == "__main__":
    print("=" * 50)
    print("HappyCapy Office UI - Backend State Service")
    print("=" * 50)
    print(f"State file: {STATE_FILE}")
    print("Listening on: http://0.0.0.0:18791")
    print("=" * 50)

    app.run(host="0.0.0.0", port=18791, debug=False, threaded=True)
