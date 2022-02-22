# Ciência da computação - Cruzeiro do Sul Virtual EAD
# Disciplina: PROJETO INTEGRADOR DE COMPETÊNCIAS EM CIÊNCIA DA COMPUTAÇÃO I
# Aluna: Tamires Ataíde de Freitas

cadastro = "0"
obrigatorio = 0
facultativo = 0
nao = 0
while cadastro != "2":
    cadastro = input("Você deseja cadastrastrar algum usuário?\n1 - Sim  2 - Não\n")
    while cadastro != "1" and cadastro != "2":
        print("Você digitou um valor inválido")
        cadastro = input("Deseja cadastrastrar algum usuário?\n1 - Sim  2 - Não\n")
    if cadastro == "1":
        idade = int(input("Digite a sua idade: "))
        if idade >= 18 and idade <= 69:
            obrigatorio += 1
        elif idade == 16 or idade == 17 or idade >= 70:
            facultativo += 1
        else:
            nao += 1
    else:
        total = obrigatorio + facultativo + nao
        print("No município há %s cidadãos."
              "\nNo município há %s de cidadãos no qual o voto é obrigatório."
              "\nNo município há %s de cidadãos no qual o voto é facultativo."
              "\nNo município há %s de cidadãos no qual não são eleitores."
              %(total, obrigatorio, facultativo, nao))
