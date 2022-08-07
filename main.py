# Exercice sur les Collections : Le Quizz_v2
# Créer un quizz contenant 4 questions : Chaque question propose 1 bonne et 3 mauvaises réponses.
# Question : Quelle est la capitale de la France ?
# a) Paris
# b) Marseille
# c) Nantes
# d) Amiens
#
# Votre réponse : 
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
# 4 questions

def ask_number(min, max):
	try:
		reponse = int(input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : "))
		if min <= reponse <= max:
			return reponse
		print(f"Erreur : Vous devez entrer un chiffre compris entre {min} et {max}")
	except:
		print("Erreur : Veuillez entrer uniquement un chiffre")
	return ask_number(min, max)


def show_question(question):
	result = False
	print("Question : " + question[0])
	for i in range(0, len(question[1])):
		print(f"{i + 1}) " + question[1][i])

	usr_ans = ask_number(0, len(question[1]))
	if question[1][usr_ans - 1] == question[2]:
		print("Bonne réponse")
		result = True
	else:
		print("Mauvaise réponse")
	return result

def start_questions(questionnaire):
	score = 0
	for question in questionnaire:
		if show_question(question):
			score += 1
	print(f"Votre score : {score} / {len(questionnaire)}")


score = 0

questionnaire = (
	("Quelle est la capitale de la France", ("Cannes", "Paris", "Bruxelles", "Amiens"), "Paris"),
	("Quelle est la capitale de l'Italie", ("Liège", "Madrid", "Bruxelles", "Rome"), "Rome"),
	("Quelle est la capitale de l'Espagne", ("Madrid", "Paris", "Bruxelles", "Amiens"), "Madrid"),
	("Quelle est la capitale de la Belgique", ("Cannes", "Paris", "Bruxelles", "Amsterdam"), "Bruxelles")
)

start_questions(questionnaire)

