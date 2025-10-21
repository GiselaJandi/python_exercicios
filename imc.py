massa = float(input("Digite a sua massa (kg) : "))
altura = float(input("Digite a sua altura (m) :" ))
 
IMC = massa/altura**2

print ("O seu Imc é {:.2f} " .format(IMC))

if IMC <17 : 
    print("Muito abaixo do peso ")
elif IMC >17 and IMC <= 18.5 : 
    print ("Abaixo do peso")
elif IMC >18.5 and IMC <= 25: 
    print ("Peso ideal")
elif IMC  >25 and IMC <= 30: 
    print ("Sobrepeso")
elif IMC >30 and IMC <= 35 : 
    print >("Obesidade")
elif IMC  >35 and IMC <= 40: 
    print ("Obesidade Severa")
else: 
    print ("Obesidade Mórbida")