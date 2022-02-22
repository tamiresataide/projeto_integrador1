#Ciência da computação - EAD - Cruzeiro do Sul Virtual
#Disciplina: PROJETO INTEGRADOR DE COMPETÊNCIAS EM CIÊNCIA DA COMPUTAÇÃO I
#Aluno: Tamires Ataíde de Freitas

cliente = "sim"
while cliente != "não":
    cliente = input("Gostaria de calcular o seu desconto? ")
    if cliente != "sim" and cliente != "não":
        print("Por favor, responda 'sim' ou 'não' :")

    elif cliente == "sim":
        livros = float(input("Quantos livros você está comprando? "))
        a = (livros * 0.25) + 7.50
        b = (livros * 0.50) + 2.50
        c = (livros * 0.65) + 1.50

        if a == b:
            print("O seu total é de R$%.2f e foi utilizado o critério C." %c)
        elif a == c:
            print("O seu total é de R$%.2f e foi utilizado o critério B." %b)
        elif b == c:
            print("O seu total é de R$%.2f e foi utilizado o critério A." %a)
        elif a > b and a > c:
            print("O seu total é de R$%.2f e foi utilizado o critério A." %a)
        elif b > a and b > c:
            print("O seu total é de R$%.2f e foi utilizado o critério B." %b)
        elif c > a and c > b:
            print("O seu total é de R$%.2f e foi utilizado o critério C." %c)