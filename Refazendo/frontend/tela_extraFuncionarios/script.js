let func = 100;

let newTextarea = [];

for(let i = 0; i < func; i++){
    newTextarea[i] = document.createElement("textarea");
    
    newTextarea.readOnly = true;

    /* newTextarea[i].style. */
    
    let div = document.querySelector('#content');

    div.appendChild(newTextarea[i]);
}

document.querySelector('#btnBack').addEventListener('click', function(){
    window.history.back();
});