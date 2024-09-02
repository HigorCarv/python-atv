nota1 = float(input('Me diga uma nota : '))
nota2 = float(input('Me diga uma nota : '))
nota3 = float(input('Me diga uma nota : '))
nota4 = float(input('Me diga uma nota : '))

media = (nota1 + nota2 + nota3 + nota4)/ 4
print(f'Sua média {media}')

if media >= 7:
    print('Aprovado')
else:
    print ('Reprovado')