function contar() {
    let inicio = document.getElementById("inicio")
    let fim = document.getElementById("fim")
    let passo = document.getElementById("passo")
    let resultado = document.getElementById("res")

    
    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        alert("[ERRO] Valor inválido")
    } else {
        resultado.innerHTML = `Contando...: `
        let i = Number(inicio.value)
        let f = Number(fim.value)
        let p = Number(passo.value)
        if (i < f){
            for (let counter = i; counter <= f; counter += p){
                resultado.innerHTML += ` ${counter} \u{1F449} `
            }
        } else {
            for (let counter = i; counter >= f; counter -= p){
                resultado.innerHTML += ` ${counter} \u{1F449} `
            }
        }
        resultado.innerHTML += `\u{1F3C1}`
    }
}   
