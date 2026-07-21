import os
import threading
import subprocess
import asyncio
import aiohttp
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Miso Bot Web Wrapper is live!")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"Faking port listener on port {port} for Render...")
    server.serve_forever()

if __name__ == "__main__":
    # 1. Start the HTTP listener in a background thread to keep Render alive
    web_thread = threading.Thread(target=run_http_server, daemon=True)
    web_thread.start()

    # 2. Launch the actual Miso Bot main script cleanly via Poetry 
    print("Launching Miso Bot package...")
    subprocess.run(["poetry", "run", "python", "main.py"])

