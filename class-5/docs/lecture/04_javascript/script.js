// Class 5: dark and light mode. Find, listen, change.

// 1. Find the button.
const themeBtn = document.getElementById("theme-btn");

// 2. Listen for a click.
themeBtn.addEventListener("click", () => {
  // 3. Change: add or remove the class "dark" on <body>.
  document.body.classList.toggle("dark");

  // Update the button text to match.
  if (document.body.classList.contains("dark")) {
    themeBtn.textContent = "Light mode";
  } else {
    themeBtn.textContent = "Dark mode";
  }
});
