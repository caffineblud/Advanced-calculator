// ==========================
// Variables
// ==========================

const display = document.getElementById("display");

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


            if(value === "="){

                calculate();

            }

            else if(value === "C"){

                display.value = "";

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

        display.value += replacements[value];

    }

    else{

        display.value += value;

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


    history.forEach(item=>{


        let li=document.createElement(
            "li"
        );


        li.innerText=item;


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