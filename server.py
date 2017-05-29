import os
import ast

from base import Socket, flags
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Server(Socket):
    def __init__(self, host="", port=5368):
        Socket.__init__(self)

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4096)

        self.host = host
        self.port = port
        self.flag = True

        self.max_file_size = 50 * (1 << 20)

    def run(self):
        for i in range(5):
            thread = Thread(target=self.accept)
            thread.start()

    def accept(self):
        while self.flag:
            conn, addr = self.server.accept()
            print ('[+] connected: {}'.format(str(addr)))

            json = ast.literal_eval(self.recv(conn))
            folder = json.get('dir', 'default')

            print (json)

            if json.get('process', None) == 'download':
                path = os.path.join(folder, json.get('filename', '--'))

                if not os.path.isfile(path):
                    self.send(conn, flags['file_not_found'])

                else:
                    self.send(conn, flags['success'])
                    self.upload(conn, path)

            elif json.get('process', None) == 'upload':
                if json.get('size', float('inf')) > self.max_file_size:
                    self.send(conn, flags['file_size_exceeded'])

                elif 'filename' in json:
                    self.send(conn, flags['success'])

                    path = os.path.join(folder, json['filename'])
                    self.download(conn, path)


if __name__ == '__main__':
    server = Server()
    server.run()
