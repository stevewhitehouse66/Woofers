// Get the root element variables
const rootElements = document.querySelector(':root');
//Function for getting the variable values
function readVariables() {
    var variableValues = getComputedStyle(rootElements);
    console.log("The value of gradient is: " + variableValues.getPropertyValue('--light-background-gradient'));
  }

readVariables()