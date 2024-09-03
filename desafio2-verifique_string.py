# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
#  além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
#  definida no código;



def contains_a(str):
    contains = "A"
    count = 0
    new_str = str.upper()
    

    for char in new_str:
        if contains == char:
            count += 1
    
    print(f"A string: {str}. \nContém: {count} letra '{contains}' nela.")

string = str(input("escreva uma frase: "))

contains_a(string)