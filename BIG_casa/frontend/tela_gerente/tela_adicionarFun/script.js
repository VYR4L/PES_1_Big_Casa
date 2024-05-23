document.querySelector('#btnBack').addEventListener('click', function(){
    window.location.href = '../index.html';
})

let inputs = document.querySelectorAll('.inputs');
let btn = document.querySelector('#btn');

inputs.forEach(input => {
    input.addEventListener('input', () => {
        let todosPreenchidos = Array.from(inputs).every(input => input.value !== '');
        btn.disabled = !todosPreenchidos;
    });
});