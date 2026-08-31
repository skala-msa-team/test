import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

try:
    from backend.task_service import TaskService
except ModuleNotFoundError:
    from task_service import TaskService


HOST = "127.0.0.1"
PORT = 8000
SERVICE = TaskService()


class TaskRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PATCH, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length) if content_length else b"{}"
        return json.loads(raw_body.decode("utf-8"))

    def do_OPTIONS(self):
        self._send_json(204, {})

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != "/api/tasks":
            self._send_json(404, {"message": "요청한 경로를 찾을 수 없습니다."})
            return

        status = parse_qs(parsed.query).get("status", ["all"])[0]
        self._send_json(200, {"tasks": SERVICE.list_tasks(status)})

    def do_POST(self):
        if self.path != "/api/tasks":
            self._send_json(404, {"message": "요청한 경로를 찾을 수 없습니다."})
            return

        try:
            task = SERVICE.create_task(self._read_json().get("title"))
            self._send_json(201, {"task": task})
        except (ValueError, json.JSONDecodeError) as error:
            self._send_json(400, {"message": str(error)})

    def do_PATCH(self):
        segments = self.path.strip("/").split("/")
        if len(segments) != 3 or segments[:2] != ["api", "tasks"]:
            self._send_json(404, {"message": "요청한 경로를 찾을 수 없습니다."})
            return

        try:
            task = SERVICE.update_task(int(segments[2]), self._read_json().get("completed"))
            self._send_json(200, {"task": task})
        except (KeyError, ValueError, json.JSONDecodeError) as error:
            self._send_json(404, {"message": str(error)})

    def log_message(self, format, *args):
        return


def run():
    server = ThreadingHTTPServer((HOST, PORT), TaskRequestHandler)
    print(f"Backend running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()

