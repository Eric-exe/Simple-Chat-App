function sendMessage() {
  // check if name is input
  let nameElement = document.getElementById("name");
  if (nameElement.value == "" || nameElement.value == null) {
    
    let name = prompt("Enter your name","");
    
    if (name == "" || name == null) {
      return;
    }
    nameElement.value = name;
  }
  
  let messageElement = document.getElementById("message");
  let message = messageElement.value;
  messageElement.value = "";
  let messageContents = { "name" : nameElement.value, "message" : message };
  ajaxPostRequest("/send", JSON.stringify(messageContents), renderChat);
}

function renderChat(jsonData) {
  let data = JSON.parse(jsonData);
  let messages = data["message"];
  
  let chatElement = document.getElementById("chat");
  chatElement.innerHTML = "";
  
  for (let i = 0; i < messages.length; i += 1) {
    chatElement.innerHTML += messages[i] + "<br>";
  }
}

function getMessages() {
  ajaxPostRequest("/send", JSON.stringify({"message": ""}), renderChat);
}

setInterval(getMessages, 100);
