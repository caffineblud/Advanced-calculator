// ==========================
// Variables
// ==========================
const display = document.getElementById("display");

const expressionDisplay =
document.getElementById(
    "expression-display"
);

const buttons = document.querySelectorAll(
    ".buttons button, .scientific button"
);

const historyList = document.getElementById(
    "history-list"
);

const clearHistoryBtn = document.getElementById(
    "clear-history"
);


let history = JSON.parse(
    localStorage.getItem("history")
) || [];



// ==========================
// Button Click Handling
// ==========================


buttons.forEach(button => {

    button.addEventListener(
        "click",
        () => {

            const value = button.innerText;
            animateButton(
                button.dataset.key
            );

            if(value === "="){

                calculate();

            }

            else if(value === "C"){

                display.value = "0";
                expressionDisplay.textContent = "0";

            }

            else if(value === "⌫"){

                display.value =
                display.value.slice(0,-1);

            }

            else {

                addInput(value);

            }

        }
    );

});



// ==========================
// Add Input
// ==========================

function addInput(value){

    const replacements = {

        "π":"Math.PI",
        "sin":"sin(",
        "cos":"cos(",
        "tan":"tan(",
        "sqrt":"sqrt(",
        "log":"log("

    };


    if(replacements[value]){

        if(display.value === "0"){
            display.value = replacements[value];
        }
        else{
            display.value += replacements[value];
        }

    }

    else{

        if(display.value === "0"){
            display.value = value;
        }
        else{
            display.value += value;
        }

    }

}




// ==========================
// Calculator Logic
// ==========================


function calculate(){

    try{


        let expression = display.value;


        let result = evaluateExpression(
            expression
        );


        expressionDisplay.textContent =
        expression;

        display.value = result;

        saveHistory(
            expression + " = " + result
        );


    }


    catch(error){


        display.value = "Error";


    }

}





// ==========================
// Scientific Functions
// ==========================


function sin(x){

    return Math.sin(
        x * Math.PI / 180
    );

}


function cos(x){

    return Math.cos(
        x * Math.PI / 180
    );

}


function tan(x){

    return Math.tan(
        x * Math.PI / 180
    );

}


function sqrt(x){

    return Math.sqrt(x);

}


function log(x){

    return Math.log10(x);

}




// ==========================
// Safe Evaluation
// ==========================


function evaluateExpression(expression){


    return Function(

        "sin",
        "cos",
        "tan",
        "sqrt",
        "log",

        "return " + expression

    )

    (
        sin,
        cos,
        tan,
        sqrt,
        log
    );


}




// ==========================
// History
// ==========================


function saveHistory(item){


    history.unshift(item);


    localStorage.setItem(
        "history",
        JSON.stringify(history)
    );


    loadHistory();


}



function loadHistory(){


    historyList.innerHTML="";
    history.forEach(item => {

        const li = document.createElement("li");

        li.textContent = item;

        li.style.cursor = "pointer";

        li.title = "Click to reuse";

        li.addEventListener("click", () => {

            const expression = item.split("=")[0].trim();

            display.value = expression;

            expressionDisplay.textContent = "History";

        });

        historyList.appendChild(li);

    });

}



clearHistoryBtn.addEventListener(
    "click",
    ()=>{


        history=[];


        localStorage.removeItem(
            "history"
        );


        loadHistory();


    }
);



// Load old history

loadHistory();
const themeButton =
document.getElementById(
    "theme-toggle"
);

loadTheme();

themeButton.addEventListener(
    "click",
    toggleTheme
);
document.addEventListener(
    "keydown",
    handleKeyboardInput
);
function handleKeyboardInput(event) {

    const key = event.key;

    // Numbers
    if (/^[0-9]$/.test(key)) {
        animateButton(key);
        display.value += key;
        return;
    }

    // Operators
    if (["+", "-", "*", "/", ".", "%"].includes(key)) {
        animateButton(key);
        display.value += key;
        return;
    }

    // Parentheses
    if (key === "(" || key === ")") {
        animateButton(key);
        display.value += key;
        return;
    }

    // Enter
    if (key === "Enter") {
        animateButton("enter");
        event.preventDefault();
        calculate();
        return;
    }

    // Backspace
    if (key === "Backspace") {
        animateButton("backspace");
        display.value =
            display.value.slice(0, -1);
        return;
    }

    // Escape or Delete
    if (
        key === "Escape" ||
        key === "Delete"
    ) {
        animateButton("clear");
        display.value = "0";
        expressionDisplay.textContent = "0";
        return;
    }

}
function toggleTheme(){

    document.body.classList.toggle(
        "light"
    );

    const isLight =
        document.body.classList.contains(
            "light"
        );

    localStorage.setItem(
        "theme",
        isLight ? "light" : "dark"
    );

    updateThemeIcon();

}



function loadTheme(){

    const theme =
        localStorage.getItem("theme");

    if(theme==="light"){

        document.body.classList.add(
            "light"
        );

    }

    updateThemeIcon();

}



function updateThemeIcon(){

    themeButton.textContent =
    document.body.classList.contains("light")
    ? "🌙"
    : "☀️";

}

function animateButton(key){

    const button=document.querySelector(
        `[data-key="${key}"]`
    );

    if(!button) return;

    button.classList.add("active");

    setTimeout(()=>{

        button.classList.remove("active");

    },120);

}