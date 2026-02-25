// variavel
let sorteado = 1;

// WHILE
while (sorteado !== 5) {
    // sorteia um numero na variavel sorteado
    // floor aredonda pra baixo o numero aleatorio
    // random aleatoriza um numero de 0 a 0,99999999999
    // por isso ele multiplica por 10
    sorteado = Math.floor(Math.random() * 10) + 1
    console.log("Número sorteado", sorteado);
}

console.log("Finalmento o número 5 for sorteado!");

// FUNCAO
// funcao de soma
function soma(a, b) {
    return a + b
}

// funcao de subtracao
function subtracao(a, b) {
    return a - b
}

// ARROW FUNCTION
// uma variavel com uma funcao nela
// funcao de multiplicacao
const multiplica = (a, b) => {
    return a * b
}

// calculadora
console.log("Escolha uma operação: +, -, *");

// escolha
let operacao = "+"

// possiveis escolhas
switch (operacao) {
    case "+":
        console.log(soma(10, 5));
        break;
    
    case "-":
        console.log(subtracao(10,5));
        break;

    case "*":
        console.log(multiplica(10, 5));
        break;
    
    default:
        console.log("Operação invalida!");
}