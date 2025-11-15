import os
import socket
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 9000  # Change if you want

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Serve EXE folder
    ip = get_ip()
    print(f"\nServing files from: {os.getcwd()}")
    print(f"Server running at: http://{ip}:{PORT}\n")

    server = ThreadingHTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
    server.serve_forever()