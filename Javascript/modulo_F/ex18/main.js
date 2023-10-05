let number = document.getElementById('num')
let result = document.getElementById('res')
let list = document.getElementById('list')
let array = []

function addNumber(num = Number(number.value)) {
    if (num < 0 || num > 100) {
        alert('[ERRO] Number is not between 1 and 100')
    } else {
        if (num === 0){
            alert('[ERRO] Number is null')
        } else if (array.includes(num) === true){ 
            alert('[ERRO] Value already in the list')
        } else {
            if (array.length === 0){
                list.innerHTML = ``
            }
            list.innerHTML += `<option>Value ${num} added to your list...</option>`
            array.push(num)
            console.log(array);
        }
    }
}

function finalize() {
    console.table(array);
    
}