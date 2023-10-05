let number = document.getElementById('num')
let result = document.getElementById('res')
let list = document.getElementById('list')
let array = []

function addNumber(num = Number(number.value)) {
    result.innerHTML=``
    if (num < 0 || num > 100) {
        alert('[ERROR] Number is not between 1 and 100')
    } else {
        if (num === 0){
            alert('[ERRO] Number is null')
        } else if (array.includes(num) === true){ 
            alert('[ERROR] Value already in the list')
        } else {
            if (array.length === 0){
                list.innerHTML = ``
            }
            list.innerHTML += `<option>Value ${num} added to your list...</option>`
            array.push(num)
        }
    }
}

function finalize() {
    let arrayLength = array.length
    if (arrayLength == 0){
        alert("[ERROR] There's no numbers to analyze")
    } else {
        array.sort((a,b)=>a-b)
        let sum = 0
        for (pos in array){
            sum += array[pos]
        }
        let average = sum / arrayLength
        result.innerHTML +=`
        <p>Total of registered values : ${arrayLength}</p>
        <p>The highest value was: ${array[arrayLength-1]} </p>
        <p>The lowest value was: ${array[0]} </p>
        <p>The summatory of all registered values is: ${sum} </p>
        <p>The average value is: ${average} </p>
        `
        console.table(array);
    }
}