from __future__ import annotations

import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


class GameHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory: str | None = None, **kwargs) -> None:
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/health":
            self._send_json({"status": "ok", "message": "Emoji Drop Python backend is live"})
            return

        if parsed.path == "/api/leaderboard":
            leaderboard = [
                {"name": "CyberKing 👑", "score": 1420},
                {"name": "NeonMaster ⚡", "score": 890},
                {"name": "YOU (Player)", "score": 100, "isUser": True},
                {"name": "PixelDrop 👾", "score": 85},
                {"name": "StarBounce ✨", "score": 40},
            ]
            self._send_json(leaderboard)
            return

        super().do_GET()

    def _send_json(self, payload: object) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    directory = str(Path(__file__).resolve().parent)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), partial(GameHandler, directory=directory))
    print("Serving Emoji Drop on http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
