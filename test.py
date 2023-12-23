import random

print("Bienvenue dans le Jeu de Devinettes de Nombres !")
min_nombre = 1  # Définissez votre nombre minimum
max_nombre = 100  # Définissez votre nombre maximum
nombre_aleatoire = random.randint(min_nombre, max_nombre)
tentatives = 0

while True:
    devinette = int(input(f"Devinez le nombre entre {min_nombre} et {max_nombre}: "))
    tentatives += 1

    if devinette < nombre_aleatoire:
            print("Trop bas ! Essayez encore.")
    elif devinette > nombre_aleatoire:
            print("Trop haut ! Essayez encore.")
    else:
        print(f"Félicitations ! Vous avez deviné le nombre {nombre_aleatoire} correctement en {tentatives} tentatives !")
        break
