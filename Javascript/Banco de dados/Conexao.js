//Implemente e trate uma conexão com o seu banco de dados, usando JavaScript. 
//Caso a conexão com o banco tenha sucesso, ele deve retornar uma frase positiva. 
//Se isso não ocorrer, retorne uma frase informando o erro.


const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'myuser',
  password: 'mypassword',
  database: 'mydatabase'
});

connection.connect(function(err) {
  if (err) {
    console.error('Erro ao conectar ao banco de dados: ' + err.stack);
    return;
  }

  console.log('Conexão com o banco de dados estabelecida com sucesso!');
});