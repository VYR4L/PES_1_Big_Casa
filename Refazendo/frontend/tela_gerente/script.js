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
    window.location.href = '../tela_loginGerente/index.html';
})
document.querySelector('#btnAdd').addEventListener('click', function(){
    window.location.href = './tela_adicionarFun/index.html';
})
document.querySelector('#btnEdit').addEventListener('click', function(){
    window.location.href = './tela_editarFun/index.html';
})
let state = 0
function slide(){
    let slide = document.querySelector("footer")
    if(state == 0){
        slide.style.bottom = "0"
        state = 1
    }else{
        slide.style.bottom = "-80vh"
        state = 0
    }
}