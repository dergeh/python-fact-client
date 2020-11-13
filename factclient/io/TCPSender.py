import socket
from datetime import datetime


class TCPSender:
    address = ""
    port = 9999
    connected = False

    def connect(self, env):
        self.address = env["fact_tcp_address"]
        if "fact_tcp_port" in env:
            self.port = env["fact_tcp_port"]
        self.connected = True

    def send(self, message, trace):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.address, self.address))
            trace.Logs[datetime.now().timestamp() * 1000] = message
            s.sendall(trace)
