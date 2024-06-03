let func = 10;

let newTextarea = [];

for(let i = 0; i < func; i++){
    newTextarea[i] = document.createElement("textarea");
    
    newTextarea.readOnly = true;

    newTextarea[i].onclick = function(){
        window.location.href = "./tela_edicao/index.html";
    }
    
    let div = document.querySelector('#content');

    div.appendChild(newTextarea[i]);
}

document.querySelector('#btnBack').addEventListener('click', function(){
    window.location.href = '../index.html';
});