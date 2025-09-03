class Quizz:
    def __init__(self, nb_de_chances):
        self.nb_de_chances = nb_de_chances

    def poser_question(self, question, reponse):
        while self.nb_de_chances > 0:
            rep = input(question + " ").lower().strip()
            if rep == reponse:
                print("Bonne réponse ")
                return True
            else:
                self.nb_de_chances -= 1
                if self.nb_de_chances == 0:
                    print("Oh non ! Tu as perdu le jeu...")
                    return False
                print(f"Dommage ! Il te reste {self.nb_de_chances} chances")
        return False

    def demarrer(self):
        print(f"Voici notre quiz, tu as {self.nb_de_chances} chances !")

        if not self.poser_question("Combien de fois la France a gagné la coupe du monde ?", "2"):
            return
        if not self.poser_question("Quand a été fondé Apple ?", "1976"):
            return
        if not self.poser_question("Qui a fondé SpaceX ?", "elon musk"):
            return

        print("Bravo ! Tu as gagné le quiz 🎉")

jeu = Quizz(3)
jeu.demarrer()