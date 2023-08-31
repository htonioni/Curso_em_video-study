//<img src="" alt="">
let anoAtual = new Date().getFullYear()
let fano = document.getElementById("txtano").value
const radioM = document.getElementById("masc")
const divImg = document.querySelector('div#img')



function verificar() {
    let idade = anoAtual - fano
    if (fano.length == 0 || fano > anoAtual){
        alert("[ERRO] Verifique os dados e tente novamente")
    } 
}