function trocaCor() {
    let elemento = document.getElementById("titulo");
    elemento.style.color = 'blue';
}

function chamaLogin() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    let corpoRequisicao = {
        "email": email,
        "password": password
    }
    let rota = 'localhost:5000/login'
    let method = 'POST'

    // enviar isso para o backend

    let result = 'Não autorizado!'

    let divAlerta = document.getElementById("alerta");
    divAlerta.innerHTML = result;
}