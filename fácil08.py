preço =float(input('digite o valor do produto? R$'))
desconto =float(input('digite o percentual de desconto: '))
valor_do_desconto =preço * desconto / 100
a_pagar =preço - valor_do_desconto
print('Um desconto de %5.2f%% em um produto de R$%7.2f'% (desconto, preço ))
print('vale R$%7.2f.' % valor_do_desconto)
print('o valor do produto é de R$%7.2f' % a_pagar)