document.querySelector('#btnBack').addEventListener('click', function(){
    window.history.back();
});

function getDiasNoMes(mes, ano) {
    return new Date(ano, mes, 0).getDate();
}

let dataAtual = new Date();
let meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
let mesAtual = meses[dataAtual.getMonth()];
let diasNoMes = getDiasNoMes(dataAtual.getMonth()+1, dataAtual.getFullYear());

document.getElementById('mes').innerText = mesAtual;

let p = [];

for(let i = 0; i < diasNoMes; i++){
    p[i] = document.createElement("p");

    p[i].innerText = i + 1;
    
    let div = document.querySelector('#dias');

    div.appendChild(p[i]);
}