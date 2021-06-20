'''
#Calculando Empréstimo
casa = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end='')
print("A prestação será de R${:.2f}".format(prestação))
if prestação <= mínimo:
    print("Empréstimo pode ser concedido")
else:
    print("Empréstimo negado")
'''

'''
#Conversor Bases Numéricas
num = int(input("Digite um número inteiro: "))

print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

opção = int(input("Sua opção: "))
if opção == 1:
          print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
          print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
          print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")
'''

'''
#Comparando números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print("o PRIMEIRO valor é maior")
elif n2 > n1:
    print("o SEGUNDO valor é maior")
else:
    print("Os dois valores são IGUAIS")
'''

'''
#Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
elif idade < 18:
    saldo = 18 - idade
    print("Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
else:
    saldo = idade - 18      
    print("Você já deveria ter se alistado há {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))
'''

'''
#Média Aluno
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
média = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, média))
if 7 > média >= 5:
    print("O aluno está em RECUPERAÇÃO")
elif média < 5:
    print("O aluno está REPROVADO")
else:
    print("O aluno está APROVADO")
'''

'''
#Classificando Atletas
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação MIRIM")
elif idade <= 14:
    print("Classificação INFANTIL")
elif idade <= 19:
    print("Classificação JUNIOR")
elif idade <= 25:
    print("Classificação SÊNIOR")
else:
    print("Classificação MASTER")
'''

'''
#Analisando Triângulos
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo", end=' ')
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
'''

'''
#Índice de Massa Corporal
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("Parabéns, você está na faixa de PESO NORMAL")
elif 25 <= imc <30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRIBA")
'''

'''
#Gerenciador de Pagamentos
print('{:=^40}'.format(' LOJA X '))
preço = float(input('Preço das compras: R$ '))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('\033[7:31:43mOPÇÃO INVÁLIDA de pagamento. Tente novamente\033[m')
'''

'''
#GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
      if jogador == 0:
          print('EMPATE')         
      elif jogador == 1:
          print('JOGADOR VENCE')          
      elif jogador == 2:
          print('COMPUTADOR VENCE')          
      else:
          print('JOGADA INVÁLIDA')          
elif computador == 1:
      if jogador == 0:
          print('COMPUTADOR VENCE')        
      elif jogador == 1:
          print('EMPATE')        
      elif jogador == 2:
          print('JOGADOR VENCE')        
      else:
          print('JOGADA INVÁLIDA')         
elif computador == 2:
      if jogador == 0:
          print('JOGADOR VENCE')           
      elif jogador == 1:
          print('COMPUTADOR VENCE')           
      elif jogador == 2:
          print('EMPATE')           
      else:
          print('JOGADA INVÁLIDA')         
'''
