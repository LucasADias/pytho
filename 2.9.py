a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
if a>b>c>d:
    print('{}'.format(a))
if a<b>c>d:
    print('{}'.format(b))
if a<b<c>d:
    print('{}'.format(c))
if a<b<c<d:
    print('{}'.format(d))
