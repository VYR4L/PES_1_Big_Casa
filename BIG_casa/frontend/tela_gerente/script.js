document.querySelector('#btnBanco').addEventListener('click', function(){
    window.location.href = '../tela_bancoHoras/index.html';
})
document.querySelector('#btnFolga').addEventListener('click', function(){
    window.location.href = '../tela_folgaFuncionarios/index.html';
})
document.querySelector('#btnExtra').addEventListener('click', function(){
    window.location.href = '../tela_extraFuncionarios/index.html';
})
document.querySelector('#shutButton').addEventListener('click', function(){
    window.location.href = '../tela_login/index.html';
})
let state = 0
function slide(){
    let slide = document.querySelector("footer")
    if(state == 0){
        console.log("porra")
        slide.style.bottom = "0"
        state = 1
    }else{
        console.log("pika")
        slide.style.bottom = "-85vh"
        state = 0
    }
}