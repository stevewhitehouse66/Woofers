
//Local Storage code based on ChatGPT suggestion to modify my original mode-flip function,
//to stop page reverting to light colours on clicking navigation link.

//Get mode button element
const modeSwitch = document.getElementById("mode-switch-container");
// Load mode from local storage or default to light mode
let isDarkMode = localStorage.getItem("isDarkMode") === "true";
const darkHTML = '<i class="fa-solid fa-lightbulb mode-switch"></i>'
const lightHTML = '<i class="fa-regular fa-lightbulb mode-switch"></i>'
function updateMode() {
//If --setting = light, switch to dark
  if (isDarkMode) {
    document.documentElement.style.setProperty(
      "--current-background-gradient",
      "linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(30,30,30,1) 50%, rgba(0,0,0,1) 100%)"
    );
    document.documentElement.style.setProperty(
      "--current-div-gradient",
      "linear-gradient(90deg, rgb(00,00,00) 0%, rgba(10,10,30,1) 100%)"
    );
    document.documentElement.style.setProperty("--current-text", "#ffffff");
    modeSwitch.innerHTML= lightHTML;
  } else {
    document.documentElement.style.setProperty(
      "--current-background-gradient",
      "linear-gradient(90deg, #d9e7ff 0%, #e3ffe7 50%, #d9e7ff 100%)"
    );
    document.documentElement.style.setProperty(
      "--current-div-gradient",
      "linear-gradient(90deg,rgb(230, 230, 235) 0%,rgb(250, 250, 245) 100%)"
    );
    document.documentElement.style.setProperty("--current-text", "#000000");
    modeSwitch.innerHTML= darkHTML;
  }
}

function flipState() {
// Toggle the mode
isDarkMode = !isDarkMode;
// Save mode to local storage
localStorage.setItem("isDarkMode", isDarkMode);
// Update the mode
updateMode();
}

// Update the mode on page load
updateMode();