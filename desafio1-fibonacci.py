def isfibonacci(num):
    fn1 = 0
    fn2 = 1
    while  fn1 <= num:
        soma = 0
        if num == fn1:
           return print(f"O número {num} pertence à estrutura Fibonacci")
        soma = fn1 + fn2
        fn1 = fn2
        fn2 = soma
    
    return print(f"O número {num} não pertence à estrutura Fibonacci")


numero = int(input("Digite o número que deseja saber se faz parte do Fibonacci: "))


isfibonacci(numero)