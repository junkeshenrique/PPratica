consumo = float(input("Informe o consumo de seu veículo por km:"))
kms = float(input("Informe a distância que for percorrer:"))

litros = kms / consumo
print(f"Será necessário {litros:.2f} litros para percorrer essa distância.")