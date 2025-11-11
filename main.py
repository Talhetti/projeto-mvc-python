from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from model.database import create_table
from model.usuario_model import criar_usuario
from controller.login_controller import login

# Garante que o banco e o usuário admin existem
create_table()
try:
    criar_usuario("admin", "123")
except:
    pass


class SimpleMVCServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/login":
            self.render_view("view/login.html")
        elif self.path == "/dashboard":
            self.render_view("view/dashboard.html")
        elif self.path.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open(self.path.lstrip("/"), "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "Página não encontrada")

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode("utf-8"))

            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]

            next_page = login(username, password)
            if "dashboard" in next_page:
                self.redirect("/dashboard")
            else:
                self.redirect("/login")

    def render_view(self, file_path):
        try:
            with open(file_path, "rb") as f:
                content = f.read()
                self.send_response(200)
                if file_path.endswith(".html"):
                    self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "Arquivo não encontrado")

    def redirect(self, path):
        self.send_response(302)
        self.send_header("Location", path)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=SimpleMVCServer):
    server_address = ("", 8080)
    httpd = server_class(server_address, handler_class)
    print("🚀 Servidor rodando em http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
