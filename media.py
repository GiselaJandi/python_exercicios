n1 = int(input("digite a primeira nota : "))
n2 = int(input("digite a segunda nota : "))

media = float ((n1 + n2)/2) 
print("A sua media é de : {}" .format(media))
if media >= 10 :
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
