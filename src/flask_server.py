from flask import Flask, request
from src.classes.Context import Context


def start_flask_sever(context: Context, port:int, debug:bool):


  # Create flas app
  app = Flask(__name__)

  @app.route("/")
  def hello_world():
      print("hello")
      return f"<p>Hello, I'm sdf </p> "

  @app.route("/name")
  def get_node_name():
      print("hello")
      return f"{context.node.name}"
    
  @app.route("/set/name")
  def set_node_name():
      new_name = request.args.get('name')
      context.node.set_name(new_name)
      return f"New name '{new_name}' succsesfully set"
      
  print(f"Flask server is running on port {port}")
  app.run(port=port, debug=debug)
  pass