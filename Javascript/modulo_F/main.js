let arr = [1, 2, 8, 5, 3]

console.log(arr, "<- Non Sorted");
arr.sort()

for (pos in arr){
    console.log(arr[pos]);
}

console.log("Index do 5: ",arr.indexOf(5));