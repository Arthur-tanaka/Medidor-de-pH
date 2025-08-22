# Crie uma variável chamada pH e avalie se oc valor informado
# Por um input, se o pH é neutro, alcalino ou ácido
# ácido <= 0
# neutro >= <7 e>14
# alcalino <= <7 e>1

pH = input("Digite o pH: ")

if float(pH) == 7:
  print("Neutro")

if float(pH) <= 0:
  print("ÁCIDO")

elif float(pH) <= 7:
  print("básico")