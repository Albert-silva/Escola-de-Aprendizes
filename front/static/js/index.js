function trocaCor() {
    let elemento = document.getElementById("titulo");
    elemento.style.color = 'blue';
}

function Login() {
    let email = document.getElementById("email").value;
    let senha = document.getElementById("password").value;
    let tipo = document.getElementById("tipo").value;

    let corpoRequisicao = {
        "email": email,
        "senha": senha
    }
    let rota = 'http://localhost:5000/login/diretor'
   
    if (tipo === "Professor"){
         rota = 'http://localhost:5000/login/professor'
    }
    if (tipo === "Aluno"){
         rota = 'http://localhost:5000/login/aluno'
    }

    fetch(rota, {
        method: 'POST',
        headers: {
            'Accept': '*/*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(corpoRequisicao)
    })
    .then(result => {
        if (result.ok) {
            result.json().then(resposta => {
                mostraAlerta(true, resposta.message)
            })
        } else {
            result.text().then(erro => {
                mostraAlerta(false, erro)
            })
        }
    })
}
function mostraAlerta(status, mensagem) {
    let divAlerta = document.getElementById("alerta");
    divAlerta.style.display = 'block';

    if (status === true) {
        divAlerta.style.background = 'green';
    } else {
        divAlerta.style.background = 'red';
    }

    divAlerta.innerHTML = mensagem;
}

function limpar() {
    let divAlerta = document.getElementById("alerta");
    divAlerta.style.display = 'none';

    document.getElementById("email").value = '';
    document.getElementById("senha").value = '';
}