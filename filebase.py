import os
import argparse

from base import Socket, flags
from socket import socket, AF_INET, SOCK_STREAM


class Client(Socket):
    def __init__(self, host="127.0.0.1", port=5368):
        Socket.__init__(self)

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect((host, port))

        self.host = host
        self.port = port

    def sendfile(self, user, path):
        json = {
            'dir': user,
            'size': os.path.getsize(path),
            'filename': os.path.basename(path),
            'process': 'upload'
        }

        self.send(self.server, str(json))
        status = self.recv(self.server)

        if status == flags['success']:
            print ('[+] uploading...')
            self.upload(self.server, path)
            if user != 'default':
                print ('[+] usage: python {} download -f {} -u {}'.format(__file__, json['filename'], user))
            else:
                print ('[+] usage: python {} download -f {}'.format(__file__, json['filename']))

        elif status == flags['file_size_exceeded']:
            print ('[-] file limit exceeded (max 50 mb)!')

        else:
            print ('[-] error')

    def recvfile(self, user, filename):
        json = {
            'dir': user,
            'filename': filename,
            'process': 'download'
        }

        self.send(self.server, str(json))
        status = self.recv(self.server)

        if status == flags['success']:
            print ('[+] downloading...')
            self.download(self.server, filename)
            print ('[+] done')

        elif status == flags['file_not_found']:
            print ('[-] file not found!')

        else:
            print ('[-] error')

if __name__ == '__main__':
    client = Client(host='207.154.221.93')
    parser = argparse.ArgumentParser(description="File Server")

    parser.add_argument('process', choices=['upload', 'download'])
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-u', '--username', default='default')

    args = parser.parse_args()

    if args.process == 'upload':
        client.sendfile(args.username, args.filename)

    else:
        client.recvfile(args.username, args.filename)
