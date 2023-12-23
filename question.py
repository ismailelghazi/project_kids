# Définition des questions et réponses
questions = [
    {
        "question": "Quelle est la capitale de la France ?\n(a) Londres\n(b) Paris\n(c) Berlin\n",
        "reponse": "b"
    },
    {
        "question": "Quel est le résultat de 5 + 7 ?\n(a) 10\n(b) 12\n(c) 15\n",
        "reponse": "b"
    },
    {
        "question": "Quel animal miaule ?\n(a) Chien\n(b) Chat\n(c) Oiseau\n",
        "reponse": "b"
    }
]

# Initialisation du score
score = 0

# Boucle pour poser les questions
for question in questions:
    print(question["question"])
    user_answer = input("Réponse : ").lower()

    # Vérification de la réponse
    if user_answer == question["reponse"]:
        print("Bonne réponse !")
        score += 1
    else:
        print("Mauvaise réponse.")

# Affichage du score final
print(f"Votre score final est de {score}/{len(questions)}")

# Message en fonction du score
if score == len(questions):
    print("Félicitations ! Vous avez eu toutes les bonnes réponses.")
elif score >= len(questions) // 2:
    print("Pas mal ! Vous avez bien répondu à plusieurs questions.")
else:
    print("Vous pouvez essayer à nouveau. Continuez à vous entraîner !")