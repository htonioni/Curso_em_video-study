function carregar() {
    let data = new Date()
    let horaAtual = data.getHours()
    let titulo = document.getElementsByTagName('div')[0]
    let imagem = document.getElementsByTagName('div')[1]

    titulo.innerText = `Agora sao ${horaAtual} horas.`
    titulo.style.fontFamily = 'Arial'
    titulo.style.fontSize = '20px'


    if (horaAtual >= 0 && horaAtual <= 12) {
        imagem.innerHTML = `<img src="https://images.pexels.com/photos/17988529/pexels-photo-17988529/free-photo-of-alvorecer-amanhecer-aurora-manha.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="manha">`
        
    } else if (horaAtual < 18) {
        imagem.innerHTML = `<img src="https://images.pexels.com/photos/3975681/pexels-photo-3975681.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="manha">`
        document.body.style.backgroundColor ='#364438'
    } else {
        imagem.innerHTML = `<img src="https://images.pexels.com/photos/18047931/pexels-photo-18047931/free-photo-of-carros-veiculos-automoveis-cidade.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="noite">`
        document.body.style.backgroundColor = '#0c0d40'
    }

}
