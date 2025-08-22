const form = document.getElementById("form");
const input = document.getElementById("input");
const messages = document.getElementById("messages");


const sessionId = Math.random().toString(36).slice(2);


function addMessage(role, text){