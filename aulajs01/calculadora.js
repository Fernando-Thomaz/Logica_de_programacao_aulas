// variaveis do imc
const peso = 70; // em kg
const altura = 1.70; // em m

// menu
console.log("Calculadora de imc");
console.log("Seu peso:", peso);
console.log("Sua altura:", altura.toFixed(2));

// calculo do imc
const imc = peso / (altura * altura)
console.log("Valor do imc:", imc.toFixed(2));

// possiveis resultados
if (imc < 18.5) {
    console.log("Abaixo do peso");
} else if (imc < 24.9) {
    console.log("Peso normal");
} else if (imc < 29.9) {
    console.log("Sobrepeso");
} else {
    console.log("Obesidade");
}