let func = 25;

let newTextarea = [];

for(let i = 0; i < func; i++){
    newTextarea[i] = document.createElement("textarea");
    
    newTextarea.readOnly = true;
    
    let main = document.querySelector('main');

    main.appendChild(newTextarea[i]);
}