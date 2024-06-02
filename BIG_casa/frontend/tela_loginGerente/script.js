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

function trocaLogin(){
    alert("Trocando para o login de Funcionários");
    window.location.href = '../tela_loginFuncionario/index.html'
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