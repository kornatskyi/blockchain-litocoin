import os
from pathlib import Path
from random import random
import sys, getopt
from flask import Flask
from src.classes import Node
from src.flask_server import start_flask_sever




# @app.route("/")
# def hello_world():
#     print("hello")
#     return f"<p>Hello, I'm </p> "

def main(argv):
  # Read cli args
  env_file = ''
  try:
    (opts, args )= getopt.getopt(argv,"he:",["efile="])
  except getopt.GetoptError:
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('test.py -e nodeDefault.json')
      sys.exit()
    elif opt in ("-e", "--env"):
      env_file = arg
    else:
      env_file = './config_files/nodeDefault.json'
      pass
  
  print(sys.argv)

  me = Node(Path(env_file))

  start_flask_sever(port=me.port, debug=True)
  pass

if __name__ == "__main__":
  # Clearing the sonsole
    os.system('clear')
    main(sys.argv[1:])
    pass
