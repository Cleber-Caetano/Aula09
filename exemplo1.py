'''
try:
    n = input('Informe um número: ')[0]
except ValueError:
    print(f'Precisa digitar algo')
else:
    print('Acertou!')
finally:
    print('SEMPRE EXECUTADO')
'''

try:
    resp = input('Informe (s/n): ').lower()

    if resp == '':
        raise EOFError('Você não digitou nada')
    if resp.isdigit():
        raise ValueError('Não informe números')
except EOFError as e:
    print(f'{e}')
except ValueError as e:
    print(f'{e}')
