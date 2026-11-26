"""Invented RedBus-style bus timing API for local GET practice (stdlib only)."""
from __future__ import annotations

import json
import re
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = 18765
VALID_KEY = "redbus-campus-demo-2611"
DATA = json.loads((Path(__file__).parent / "bus_departures.json").read_text(encoding="utf-8"))
DEPARTURES = DATA["departures"]

_server: HTTPServer | None = None
_thread: threading.Thread | None = None
_ready = threading.Event()


def route_get(path: str, headers: dict | None = None, params: dict | None = None) -> tuple[int, dict]:
    """Return the same JSON body a GET to the mock API would send."""
    headers = headers or {}
    params = params or {}
    key = headers.get("X-Bus-Key", "")

    if path == "/v1/health":
        return 200, {"service": "bus-timing-demo", "status": "ok"}

    m = re.fullmatch(r"/v1/stops/([A-Z0-9]+)/departures", path)
    if not m:
        return 404, {"error": "route_not_found", "path": path}

    if key != VALID_KEY:
        return 401, {"error": "missing_or_bad_key"}

    stop_id = m.group(1)
    if stop_id == "ST99":
        return 404, {"error": "stop_not_found", "stop_id": stop_id}

    limit = int(params.get("limit", 5))
    matched = [d for d in DEPARTURES if d["stop_id"] == stop_id]
    matched = sorted(matched, key=lambda x: (x["eta_min"], x["trip_id"]))[:limit]
    if not matched:
        return 200, {"stop_id": stop_id, "departures": [], "count": 0}

    return 200, {
        "stop_id": stop_id,
        "stop_name": matched[0]["stop_name"],
        "departures": matched,
        "count": len(matched),
    }


class BusHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def _send(self, code: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        raw_params = parse_qs(parsed.query)
        params = {k: v[0] for k, v in raw_params.items()}
        key = self.headers.get("X-Bus-Key", "")
        code, payload = route_get(path, {"X-Bus-Key": key}, params)
        self._send(code, payload)


def start_server(host: str = HOST, port: int = PORT) -> HTTPServer:
    global _server
    if _server is not None:
        return _server
    _server = HTTPServer((host, port), BusHandler)
    _ready.set()
    _server.serve_forever()
    return _server


def boot_background(host: str = HOST, port: int = PORT, wait: float = 2.0) -> None:
    global _thread
    if _thread is not None and _thread.is_alive():
        return
    _ready.clear()
    _thread = threading.Thread(target=start_server, args=(host, port), daemon=True)
    _thread.start()
    _ready.wait(timeout=wait)


if __name__ == "__main__":
    print(f"Serving on http://{HOST}:{PORT}")
    start_server()