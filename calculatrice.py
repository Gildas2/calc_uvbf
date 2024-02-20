def addition(x, y):
    return x + y


def division(x, y):
    if y == 0:
        return "Erreur : Division par zéro !"
    else:
        return x / y

def quitter():
    print("Merci d'avoir utilisé la calculatrice. À bientôt !")

def main():
    while True:
        try:
            print("\nBienvenue dans la Calculatrice Console")
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            continue

        print("\nChoisissez l'opération à effectuer :")
        print("1. Addition")
        print("4. Division")
        print("5. Sortie")

        choix = input("Entrez le numéro de l'opération choisie : ")

        if choix == '1':
            print("Résultat : ", addition(num1, num2))
        
            print("Résultat : ", division(num1, num2))
        elif choix == '5':
            quitter()
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
