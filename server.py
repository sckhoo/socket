import socket

def listen_for_connections():
    host = "localhost"
    port = 10000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print("Listening on port 10000...")

        while True:
            connection, address = sock.accept()
            print(f"Connection from {address}")

            with connection:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break

                    payload = data.decode("utf-8")
                    print(f"Received payload: {payload}")

                    if not payload.startswith("{") or not payload.endswith("}"):
                        response = "NACK"
                    else:
                        values = payload[1:-1].split(",")
                        if all(value.strip() for value in values):
                            response = "ACK"
                        else:
                            response = "NACK"

                    connection.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    listen_for_connections()