#!/usr/bin/python3
"""
This script implements a simple HTTP server using http.server module.
It handles different endpoints and serves both text and JSON responses.
"""
import http.server
import json
import socketserver


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server.
    """
    
    def do_GET(self):
        """
        Handle GET requests to different endpoints.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "OK"
            self.wfile.write(response.encode('utf-8'))
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Endpoint not found"
            self.wfile.write(response.encode('utf-8'))


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.
    """
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server running on http://localhost:{port}")
        print("Available endpoints:")
        print("  /          - Welcome message")
        print("  /data      - Sample JSON data")
        print("  /status    - API status")
        print("\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    run_server()
