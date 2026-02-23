// DOCUMENTACAO JAVASCRIPT

// comentario de linha

/*
 comentario de bloco
 comentario de bloco
*/

// print no console
console.log("Olá, mundo!");

// variaveis
var nome = "João"; // variavel global
let idade = 30; // variavel de bloco
const pi = 3.14; // variavel constante, não pode ser alterada

// mostrando as variaveis
console.log(nome);
console.log(idade);
console.log(pi);

// operadores
let a = 10;
let b = 5;

console.log(a + b); // adicao
console.log(a - b); // subtracao
console.log(a * b); // multiplicacao
console.log(a / b); // divisao
console.log(a % b); // resto

console.log(a ** b); // exponencial

// operadore de comparacao
console.log(a > b); // maior que
console.log(a < b); // menor que
console.log(a >= b); // maior ou igual a
console.log(a <= b); // menor ou igual a
console.log(a == b); // comparacao
console.log(a === b); // restritamente igual
console.log(a != b); // diferente
console.log(a !== b); // restritamente diferente

// operadores logicos
let x = true;
let y = false;
console.log(x && y); // AND logico
console.log(x || y); // OR logico
console.log(!x); // NOT logico

nome = "Maria"; // reatribuindo a variavel nome
idade = 25; // reatribuindo a variavel idade

// concatenando strings e variaveis
console.log("Nome: " + nome, "Idade " + idade);

console.log(`Nome: ${nome} Idade ${idade}`);

// verificar tipo da variavel
console.log(typeof nome2);

// if e else
idade = 20;

if (idade >= 18) {
    console.log("Você é maior de idade");
} else {
    console.log("Você é menor de idade");
}

// operador alternado
let resultado = (idade >= 18) ? "Maior de idade" : "Menor de idade";
console.log(resultado)

let num1 = 10;

let resultado2 = (num1 % 2 === 0) ? "O numero é par" : "O numero é impar";
console.log(resultado2);

// estrutura de repeticao
for (let i = 0; i <= 5; i++) {
    console.log("Contagem: "+ i);
}

// arrays
let frutas = ["maça", "bananas", "laranja"];
console.log(frutas[0]); // acessar o primeiro elemento do array
console.log(frutas.length); // verificar o tamanho do array

// for para array
for (let fruta of frutas) {
    console.log(fruta);
}

// objeto
let pessoas = {
    nome: "Carlos",
    idade: 28,
    profissao: "Desenvolvedor de sistemas"
};
console.log(pessoas["nome"]);
console.log(pessoas["idade"]);

// for para objeto
for (let pessoa in pessoas) {
    console.log(pessoa);
}