let arr = [1, 2, 2, 5]


arr.sort()
let sum = 0
for (pos in arr){
    sum = sum + (arr[pos])
    console.log(sum, "<- Total");
}

console.log("Index do 5: ",arr.indexOf(5));