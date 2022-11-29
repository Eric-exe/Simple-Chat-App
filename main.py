# define behavior of web server
# receives requests from client and respons appropriately
import bottle
import json
# Send contents of index html to the requesting client
@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html", root=".")

@bottle.route("/ajax.js")
def serve_ajax():
  return bottle.static_file("ajax.js", root=".")

@bottle.route("/chat.js")
def serve_chat():
  return bottle.static_file("chat.js", root=".")

@bottle.route("/style.css")
def serve_style():
  return bottle.static_file("style.css", root=".")

@bottle.post("/send")
def receive_message():
  data = json.loads(bottle.request.body.read().decode())
  return process_message(data)
  
  
def process_message(data):
  # special commands
  if (data["message"] == "/clear"):
    open("chat.txt", "w")
    
  elif (data["message"] != ""):
    with open("chat.txt", "a") as f:
      f.write("[" + data["name"].strip() + "]: " + data["message"] + '\n')

  # create a json to send back
  result = {"message" : []}
  with open("chat.txt") as f:
    for line in f:
      result["message"].append(line)
  return json.dumps(result)

bottle.run(host="0.0.0.0", port=8080)
