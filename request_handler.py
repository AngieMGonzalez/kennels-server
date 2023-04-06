import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (get_all_animals,
            get_single_animal,
            get_all_locations,
            get_single_location,
            get_all_customers,
            get_single_customer,
            get_all_employees,
            get_single_employee)

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.

# It looks like you have a basic HTTP server implementation
# in your request_handler.py file,
# using the BaseHTTPRequestHandler class
# from Python's built-in http.server module.
# The HandleRequests class defined in the file
# inherits from this base class
# and overrides several of its methods,
# including do_GET(), do_POST(), do_PUT(), and do_OPTIONS(),
# to handle incoming HTTP requests of different types.

class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.

    # In do_GET(), for example, the server responds
    # with a JSON-encoded list of animal objects
    # if the request path is /animals, and an empty list otherwise.
    # The response is sent back to the client with an HTTP status code of 200,
    # along with the necessary headers to indicate that the response contains JSON data
    # and can be accessed from any domain (i.e., via cross-origin resource sharing, or CORS).
    # def do_GET(self):
    #     """Handles GET requests to the server
    #     """
    #     # Set the response code to 'Ok'
    #     self._set_headers(200)

    #     # Your new console.log() that outputs to the terminal
    #     print(self.path)

    #     # # It's an if..else statement
    #     # if self.path == "/animals":
    #     #     # In Python, this is a list of dictionaries
    #     #     # In JavaScript you would call it an array of objects
    #     #     response = [
    #     #         {"id": 1, "name": "Snickers", "species": "Dog"},
    #     #         {"id": 2, "name": "Lenny", "species": "Cat"}
    #     #     ]

    #     # else:
    #     #     response = []
    #     if self.path == "/animals":
    #         response = get_all_animals()
    #     else:
    #         response = []

    #     # Send a JSON formatted string as a response
    #     self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        """GET
        """
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = get_single_animal(id)

            else:
                response = get_all_animals()

        if resource == "locations":
            if id is not None:
                response = get_single_location(id)

            else:
                response = get_all_locations()

        if resource == "customers":
            if id is not None:
                response = get_single_customer(id)

            else:
                response = get_all_customers()

        if resource == "employees":
            if id is not None:
                response = get_single_employee(id)

            else:
                response = get_all_employees()

        self.wfile.write(json.dumps(response).encode())

    def parse_url(self, path):
        """
        parse
        """
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    # The do_POST() method is similarly implemented to handle incoming HTTP POST requests,
    # reading the request body and echoing it back to the client
    # as a JSON payload in the response body.
    def do_POST(self):
        """Handles POST requests to the server"""

        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = {"payload": post_body}
        self.wfile.write(json.dumps(response).encode())

    # A method that handles any PUT request.
    def do_PUT(self):
        """Handles PUT requests to the server"""
        self.do_PUT()

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.

# THIS MAKE IT GO
# Finally, the main() function at the end of the file starts the server on port 8088
# and listens for incoming requests indefinitely,
# using the HTTPServer class also from the http.server module.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()