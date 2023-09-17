function chamar() {
    return "Retorno da função"
}

function perguntar() {
    let nome;
    nome = prompt("Informe seu nome: ")
    return alert('Nome informado ' + nome)
}

function mudar_texto() {
    var texto = document.getElementsByTagName("h1")
    alert(texto[0].innerText)
    if(texto[0].innerText == "Básico JS") {
        texto[0].innerText = "Mudança do elemento"
    } else {
        texto[0].innerText = "Básico JS"
    }   
}

function incrementar() {
    let value = document.getElementById("value");
    value.innerText = parseInt(value.innerText) +1
}