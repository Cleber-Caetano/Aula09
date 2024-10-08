try:
    n = int(input('Informe um número: '))
except ValueError as e:
    print(f'{e}')
except KeyboardInterrupt as e:
    print(f'{e}')