function tabuada() {
    let numero = document.getElementById("txtn").value
    let lista = document.getElementById("lista")
    if (numero.length == 0) {
        alert("[ERRO] Valor invalido!")
    } else {
        let num = Number(numero)
        for (let i = 1; i <= 10; i++){
            if (i == 1){
                lista.innerHTML = `<option>Segue a tabua do ${numero}.....</option>`
                // let item = document.createElement('option')
                // lista.appendChild(item)
            }
            lista.innerHTML += `<option>${numero} x ${i} = ${numero * i}</option>`
        }
    }
}