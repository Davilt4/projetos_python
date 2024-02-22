import random

print(50*"-")
print("Você foi escolhido para salvar a humanidade da calvice.")
print("Tudo que deve fazer é adivinhar um número secreto escolhido pelo computador.")
print("Você só tem 3 chances, nos salve, por favor!!")
print(50*"-")

def adivinhe(x):
    random_number = random.randint(1,x)
    palpite = 0
    while palpite != random_number:
        palpite = int(input(f"Digite um número entre 1 e {x} para adivinhar o número secreto: "))
        if palpite < random_number:
            print("Seu número é menor do que o número secreto.")
        elif palpite > random_number:
            print("Seu número é maior que o número secreto.")    
    print("Parabéns você salvou o mundo da calvice.")       
adivinhe(15)
