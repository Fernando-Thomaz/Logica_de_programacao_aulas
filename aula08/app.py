# biblioteca
import random
import string

# funções
def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True, incluir_numero=True, incluir_caracter=True):
    caracteres = ''

    if incluir_maiusculo:
        caracteres += string.ascii_uppercase

    elif incluir_minusculo:
        caracteres += string.ascii_lowercase

    elif incluir_numero:
        caracteres += string.digits

    elif incluir_caracter:
        caracteres += string.punctuation

    elif not caracteres:
        return ValueError('Deve ter pelo menos um tipo de caractere')

    senha=''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha gerada: {senha}')
    return senha

def main():
    print('Gerador de senhas')
    comprimento = int(input('Digite o comprimento da senha (padrão 12): ') or 12)
    incluir_maiusculo = input('Incluir letras maiúsculas? (s/n, padrão s): ').lower() != 'n'
    incluir_minusculo = input('Incluir letras minúsculas? (s/n, padrão s): ').lower() != 'n'
    incluir_numero = input('Incluir números? (s/n, padrão s): ').lower() != 'n'
    incluir_caracter = input('Incluir caracteres especiais? (s/n, padrão s): ').lower() != 'n'

    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minusculo, incluir_numero, incluir_caracter)

    print(f'Senha gerada: {senha}')

    with open('senha.txt', 'a', encoding='utf-8') as s:
        s.write(f'\n{senha}')

if __name__ == '__main__':
    main()