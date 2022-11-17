from flask import Flask


def start_flask_sever(port:int, debug:bool):
  # Create flas app
  app = Flask(__name__)

  print(f"Flask server is running on port {port}")
  app.run(port=port, debug=debug)
  pass