function contar() {
    let inicio = document.getElementById("inicio").value
    let fim = document.getElementById("fim").value
    let passo = document.getElementById("passo")
    let resultado = documet.getElementById("res")

    if (inicio == "" || fim == "" || passo.value == ""){
        alert("[ERRO] Valor inválido")
    } else {
        if (passo.value == 0){
            alert("[ERRO] Passo nao pode ser 0, considerando 1")
            passo.setAttribute("value", 1)
        }
    }
    for (let i = inicio; i <= fim; i++){

    }
}   