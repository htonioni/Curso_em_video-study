//ex11
var idade = 67;

if (idade < 16 ) {
    console.log('Nao vota');
} else if (idade < 18 || idade >= 67) {
    console.log("Voto opcional")
} else {
    console.log("Voto obrigatorio");
}

//ex12

var agora = new Date()
var hora = agora.getHours()
console.log(`Agora sao exatamente ${hora} horas`);
if (hora < 12) {
    console.log("Bomdia");
} else if (hora <= 18) {
    console.log(`Boa tarde`);
} else {
    console.log(`Boa noite`);
}

//ex13 switch

var diaSem = 10
switch (diaSem) {
    case 0:
        console.log("Domingo");
        break;
    case 1:
        console.log("Segunda-feira");
        break;
    case 2:
        console.log("Terca-feira");
        break;
    case 3:
        console.log("quarta");
        break;
    case 4:
        console.log("quinta");
        break;
    case 5:
        console.log("sexta");
        break;
    default:
        console.log("[ERRO]");
        break;
}