numero = int(input("Digite um numero para soma-lo a um valor: "))
resto = numero % 2
if numero % 2 == 0:
    print("Como o número é par, o seu resultado é {}".format(numero + 5))
else:
    print("Como o número é ímpar, o seu resultado é {}".format(numero + 8))