ano_atual = int(input("Digite o ano Atual : "))
ano_nasc = int(input("Digite o ano de nascimento : "))

idade = ano_atual - ano_nasc
print("O ano atual é {} e o ano de seu nascimento é {} então, a sua idade é de {} anos " 
    .format(ano_atual, ano_nasc, idade))
if idade >= 18 :
    print("Como você é maior de idade estás apto para conduzir")
else:
    print("Como você é menor de idade não estás apto para conduzir, !Alerta cuidado ao dirigir")
