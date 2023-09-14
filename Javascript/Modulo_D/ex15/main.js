


function verificar() {
    var ano = new Date().getFullYear()
    var formAno = document.getElementById("txtano")
    const divRes = document.querySelector('div#res')
    if (formAno.value > ano || formAno.value == 0 || formAno.value < (ano - 150)){
        alert("[ERRO] Verifique os dados e tente novamente")
    } else {
        var formSex = document.getElementsByName('radsex')
        var idade = ano - Number(formAno.value)
        var genero = ''
        //Criando tag img
        var tagImg = document.createElement('img')
        //Adicionando a tag o id='foto'
        tagImg.setAttribute('id', 'foto')
        if (formSex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                tagImg.setAttribute('src', 'img/bM.jpg')
            } else if (idade <= 18){
                tagImg.setAttribute('src', 'img/jM.jpg')
            } else if (idade <= 51){
                tagImg.setAttribute('src', 'img/aM.jpg')
            } else {
                tagImg.setAttribute('src', 'img/oM.jpg')
            }
        } else {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                tagImg.setAttribute('src', 'img/bF.jpg')
            } else if (idade <= 18){
                tagImg.setAttribute('src', 'img/jF.jpeg')
            } else if (idade <= 51){
                tagImg.setAttribute('src', 'img/AF.jpg')
            } else {
                tagImg.setAttribute('src', 'img/oF.jpg')
            }
        }
        divRes.innerHTML = `Foi encontrado um ${genero} de ${idade} anos`
        divRes.appendChild(tagImg) 
    }
}
