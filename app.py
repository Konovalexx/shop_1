from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Класс MyServer для обработки входящих HTTP-запросов.

    Наследуется от BaseHTTPRequestHandler и переопределяет метод do_GET
    для обработки GET-запросов.
    """

    @staticmethod
    def __get_html_content():
        """
        Читает содержимое HTML-файла.

        Возвращает:
            str: Содержимое HTML-файла.
        """
        with open("index.html", "r", encoding="utf-8") as file:
            return file.read()

    def do_GET(self):
        """
        Обрабатывает входящие GET-запросы.

        Печатает параметры запроса, если они есть.
        Возвращает содержимое favicon.ico, если запрашивается.
        Возвращает содержимое HTML-страницы для всех других запросов.
        """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)

        if self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            return

        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    """
    Главная функция для инициализации и запуска веб-сервера.

    Веб-сервер будет работать на localhost и порту 8080, 
    и будет обрабатывать запросы с помощью класса MyServer.
    """
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")