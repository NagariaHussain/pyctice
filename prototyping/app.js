var editor = ace.edit("editor");
editor.setTheme("ace/theme/github");
editor.session.setMode("ace/mode/python");
editor.setOption("maxLines", 5);
editor.setOption("minLines", 4);
editor.setOption("fontSize", "18px");   
editor.setOption("cursorStyle", "wide");   

let button = document.getElementById("reset-button");

button.addEventListener('click', function() {
    console.log(editor.getValue());
});

// console.log(html);
const clearButton = document.getElementById("clearButton");

clearButton.addEventListener('click', function() {
    document.getElementById("mkarea").value = "";
});