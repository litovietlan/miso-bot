import os
import threading
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Miso Bot is live!")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"Faking port listener on port {port}")
    server.serve_forever()

if __name__ == "__main__":
    # Start web port server in background
    threading.Thread(target=run_http_server, daemon=True).start()
    # Launch the actual bot in main thread
    subprocess.run(["poetry", "run", "python", "main.py"])
