// Homework 4: script.js
// See the list of things the site needs at the top of index.html.
// Remember: find an element first (getElementById), then change it or listen to it.
// ------------------------------------------------------------
// Write your code below this line

const heading = document.querySelector('h1');
document.getElementById("changeTitle").addEventListener("click", () => {
    heading.textContent = "Welcome to my city!";
});

let count = 0
document.getElementById("changeTitle").addEventListener("click", () => {
    count++;
    document.getElementById("count".textContent = count);
});

document.getElementById("darkMode").addEventListener("click", () => {
    document.body.classList.toggle("dark");
});

document.getElementById("greet").addEventListener("click", () => {
    const name = document.getElementById("nameInput").value.trim;
    const greeting = document.getElementById("greetingMessage");
    if (name === "") {
        greeting.textContent = "Please enter your name.";
    } else {
        greeting.textContent = `Hello, ${name}!`;
    }
});