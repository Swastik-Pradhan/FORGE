import socket


def scan_localhost(start=1, end=1024):
    """
    Scan localhost ports.
    """

    open_ports = []

    for port in range(start, end + 1):
        sock = socket.socket()

        sock.settimeout(0.2)

        result = sock.connect_ex(("127.0.0.1", port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports