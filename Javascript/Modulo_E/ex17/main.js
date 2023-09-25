function tabuada() {
    let numero = Number(document.getElementById("txtn").value)
    let lista = document.getElementById("lista")
    
    for (let i = 1; i <= 10; i++){
        if (i == 1){
            lista.innerHTML = `<option>Segue a tabua do ${numero}.....</option>`
        }
        lista.innerHTML += `<option>${numero} x ${i} = ${numero * i}</option>`
    }
}