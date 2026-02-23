// variaveis do estacionamento
var estacionamentolivre = 1;
var diaria = 20;
var hora = 8;
var vip = 0.8;

// variaveis de usuario
let user_name = "Fernando T";
let user_hora = 2;
let user_vip = false;
let user_valor = (user_hora >= 3) ? 20 : user_hora * hora;

// funcao para estacionar
function estacionar (user_name, user_hora, user_vip, user_valor) {
    if (estacionamentolivre > 0) {
        console.log(`${user_name} estacionou na vaga ${estacionamentolivre--} e ficou por ${user_hora} horas`);
        let user_valorfinal = (user_vip == true) ? user_valor * vip : user_valor;
        console.log(`Valor a ser pago: R$${user_valorfinal.toFixed(2)}`);
    } else {
        console.log(`${user_name} tentou estacionar`)
        console.log("Não tem mais vaga no estacionamento");
    }
}

// ativa funcao
estacionar(user_name, user_hora, user_vip, user_valor);