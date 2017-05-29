import os
import string
import random

flags = dict(
    success='1',
    login_failed='-1',
    signup_failed='-2',
    file_not_found='-3',
    file_size_exceeded='-4'
)


class Socket(object):
    def __init__(self):
        self.buffer_size = 1024
        self.end_command = "dzeGjqWLJO"

    def recv(self, connection):
        message = ""

        while True:
            bumper = connection.recv(self.buffer_size)
            message += bumper

            if message.endswith(self.end_command):
                break

        return message[:-len(self.end_command)]

    def send(self, connection, message):
        connection.sendall(message + self.end_command)

    def upload(self, connection, path):
        with open(path, 'rb') as stream:
            while True:
                bumper = stream.read(self.buffer_size)
                if not bumper:
                    break
                connection.sendall(bumper)
            connection.send(self.end_command)

    def download(self, connection, path):
        temp = ''

        if os.path.dirname(path) and not os.path.isdir(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))

        with open(path, 'wb') as stream:
            while True:
                bumper = connection.recv(self.buffer_size)
                concat = temp + bumper

                if concat.endswith(self.end_command):
                    stream.write(concat[:-len(self.end_command)])
                    break

                else:
                    stream.write(temp)
                    temp = bumper

    @classmethod
    def generate_key(cls, size=10):
        return ''.join(random.sample(string.ascii_letters, size))
