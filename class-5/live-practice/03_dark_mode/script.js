// Live practice 3: this script already works. It does three things:
// find the button, listen for a click, change the class on <body>.

const themeBtn = document.getElementById("theme-btn");

themeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});
