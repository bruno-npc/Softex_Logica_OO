//Desenvolva um código e crie nele:

//- um objeto com, no mínimo, três propriedades;
//- um array de tamanho três no mínimo;
//- duas funções, a primeira lista as propriedades do objeto e a segunda, os elementos do array.

const myObject = {
    name: "John",
    age: 30,
    city: "New York"
  };
  
  const myArray = [1, 2, 3];
  
  function listObjectProperties(obj) {
    for (const prop in obj) {
      console.log(prop + ": " + obj[prop]);
    }
  }
  
  function listArrayElements(arr) {
    for (let i = 0; i < arr.length; i++) {
      console.log("Index " + i + ": " + arr[i]);
    }
  }
  
  listObjectProperties(myObject);
  listArrayElements(myArray);