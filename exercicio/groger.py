print ('BEM VINDO AO GROGER BANK, nos informe as seguintes informaçoes:')

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
saldo = float(input('(Simulação de saldo) - Digite o seu saldo: '))

# digitar numeros no sistema

numero = int(input('Digite qual funçao deseja: \n'
      
     'Digite (1) para saque. \n'
      
     'Digite (2) para deposito. \n'
      
    'Digite (3) para emprestimo. \n'
      
    'Digite (4) para visualizar informaçoes. \n'
))

def op_saque(saldo):

    saque = float(input('valor do saque:'))

    if saque > 1000 or saque > saldo:
        print('saque indisponivel')


    else:
        print('R$:' + str(saldo - saque))


def op_deposito():
        deposito = float(input('insira o valor do deposito:'))
        if deposito > 5000:
            print ('valor maximo do deposito sao R$ 5.000.00')

        else:
            print ('R$' + str(deposito + saldo))


if numero == 1:
    op_saque(saldo)

elif deposito == 2:
    op_deposito(saldo)











