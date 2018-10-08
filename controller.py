import threading
from os.path import exists
import logging

from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import webview

from model import Model

# Only show ERROR messages
logging.getLogger("socketio").setLevel(logging.ERROR)
logging.getLogger("engineio").setLevel(logging.ERROR)

class Controller():

    def __init__(self, client_dir):
        """Initalize the location of index.html + other static files"""
        self.client_dir = client_dir
        self.model = Model()


    def run_server(self):
        self._app = Flask(__name__,
                          static_folder=self.client_dir)
        self._socketio = SocketIO(self._app)

        @self._app.route("/", defaults={"path": ""})
        @self._app.route("/<path:path>")
        def serve(path):
            """Serve index.html and static content from
            the python webserver.

            Parameters
            ----------
            path : string
                url path to resource requested

            """

            if path != "" and exists(f"{self.client_dir}/{path}"):
                return send_from_directory(self.client_dir, path)
            else:
                return send_from_directory(self.client_dir, "index.html")

        @self._socketio.on("connect")
        def connect():
            """Do something when the client connects"""
            print("Welcome from the python backend")

        @self._socketio.on("information")
        def information(feature):
            """The client requests a feature information from
            the model"""
            feature_data = self.model.feature_data(feature)
            self._socketio.emit("server_info", feature_data)

        @self._socketio.on("action")
        def action(feature):
            """Open a file dialog and send back the file path
            to the client
            """
            file_path = self.model.feature_action(feature)
            self._socketio.emit("server_info", file_path)

        self._socketio.run(self._app, debug=False)


    def run_server_background(self):
        """Run the GUI.

        Runs the server in a background thread and then
        creates a webview to display the HTML UI.

        """

        server_thread = threading.Thread(target=self.run_server,
                                         args=())
        server_thread.start()

    def run_server_main(self):
        """Run the local python webserver in the main thread"""
        self.run_server()

if __name__ == "__main__":
    controller = Controller("client/build")
    controller.run_server_background()
    webview.create_window("Hello World",
                          "http://localhost:5000")