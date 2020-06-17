/*
  * Question
  * Write a function that accepts an array and returns the minimum value in the array
  * Solved by:  Michael Sarpong
*/

function getMinValue(array){
  let numberOfElements = array.length;
  let minValue = 0;
  let counter = 0;

  while(counter < numberOfElements){
    if(counter === 0){
      minValue = array[counter];
    }
    if(array[counter] < minValue){
      minValue = array[counter];
    }
    counter++;
  }
  return minValue;
}

let ages = [34, 87,90,14,12,33,14,19];
let output = getMinValue(ages);
console.log(output);