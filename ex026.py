fra = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(fra.count('A')))
print('A primeira letra A apareceu na posição {}'.format(fra.find('A')+1))
print('A última letra A apareceu na posição {}'.format(fra.rfind('A')+1))