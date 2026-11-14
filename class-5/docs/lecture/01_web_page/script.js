// The JavaScript file: what the page does.
const input = document.getElementById("name-input");
const button = document.getElementById("greet-btn");
const output = document.getElementById("output");

button.addEventListener("click", () => {
  output.textContent = "Hello, " + input.value + "!";
});
