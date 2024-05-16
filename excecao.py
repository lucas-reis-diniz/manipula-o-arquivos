while True:
    try:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
        num1/num2
    except ZeroDivisionError:
        print('Divisão por 0')
    except ValueError:
        print('Nao pode converter para int')
    else:
        print('Tudo foi correto!')
    finally:
        print('finally')




