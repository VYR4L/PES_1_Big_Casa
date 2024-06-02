function mostrarSenha(){
    let campoSenha = document.getElementById("int_pass");
    let checkbox = document.getElementById("pass_check");
    if(checkbox.checked){
        campoSenha.type = "text";
    }else{
        campoSenha.type = "password";
    }
}

function login(){
    alert("CPF CORRETO");
    window.location.href = '../tela_gerente/index.html';
};

function validarCPF(){
    let cpf = document.getElementById("int_cpf");
    let senha = document.getElementById("int_pass");

    let valor_cpf = cpf.value;
    let valor_senha = senha.value;

    if(valor_cpf.length == 0 || valor_cpf.length == 0){
        alert("CPF ou senha não podem ser vazios.")
    }else if(valor_cpf.length != 11){
        alert("Tamanho do CPF incorreto, deve conter no mínimo 11 caracteres.");
    }else if(/^(.)\1*$/.test(valor_cpf)){
        alert("CPF não pode conter apenas um número repitido.")
    }else{
        login();
    }

}
function naoExiste(){
    alert("AINDA NÃO EXISTE");
}
document.getElementById('toggleMode').addEventListener('click', function() {
    let body = document.body;
    let passCheck = document.getElementById("pass_check");
    let entradas = document.getElementsByClassName("entradas");
    let footer = document.getElementById('pe')
    if (body.classList.contains('darkmode')) {
        body.classList.remove('darkmode');
        body.classList.add('lightmode');
        passCheck.classList.remove('darkmode');
        passCheck.classList.add('lightmode');

        for(let i = 0; i < entradas.length; i++) {
            entradas[i].classList.remove('darkmode');
            entradas[i].classList.add('lightmode');
        }

        footer.classList.remove('darkmode');
        footer.classList.add('lightmode');
    } else {
        body.classList.remove('lightmode');
        body.classList.add('darkmode');
        passCheck.classList.remove('lightmode');
        passCheck.classList.add('darkmode');

        for(let i = 0; i < entradas.length; i++) {
            entradas[i].classList.remove('lightmode');
            entradas[i].classList.add('darkmode');
        }
        
        footer.classList.remove('lightmode');
        footer.classList.add('darkmode');
    }
});