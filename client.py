import socket

def send_payload():
    host = "localhost"
    port = 10000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print("Connected to server...")

        payload = "**&^$" #"{khoo,swee,chuan}"
        data = payload.encode("utf-8")

        sock.sendall(data)

        print("Sent payload...")
        response = sock.recv(1024)
        response_code = response.decode("utf-8")

        print("Received response code: {}".format(response_code))

if __name__ == "__main__":
    send_payload()