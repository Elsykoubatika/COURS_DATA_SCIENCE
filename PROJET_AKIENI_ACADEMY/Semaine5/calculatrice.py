#PROJET CALCULATRICE AVCE PYTHON

#fonction pour faire des calcule avec une liste
def calcul_list(liste, operation):
    """
    Calcul dans une liste avec difference operateur.

    Args:
        Liste: les chiffres saisis par l'utilisateurs
        operation : operateur et statistique de base et données selectioner par l'utilisateur 
                    (*, /, +, -, min, max, moyenne, mediane, tri, taille)

    Returns:
        float: total
    """
    # Si la liste est vide il renvois un zero
    if not liste:
        return 0
    
    #Si l'operateur est '+' il fais la somme de tout les element de la liste
    if operation == "+":
        return sum(liste)
    #Si l'operateur est "-" il fait la soustraction de tout les element de la liste
    elif operation == "-":
        total = liste[0] # le total est initiliser avec le premier element de la liste
        
        # Utilise la boucle for pour parcourir la liste et  desincrement en excullant le premier element
        for num in liste[1:]: # liste[1:] permet d'exclure le premier element et garder le reste ex: ma_liste = [10, 5, 2, 1], print(ma_liste[1:]) Affiche : [5, 2, 1] (la liste sans le 1er élément)
            total -= num
        return total
    #Si L'utilisateur choisi de trouve la valeur "maximum"
    elif operation == "max":
        return max(liste)
    #Si l'operateur est "*"
    elif operation == "*":
        total = 1 # la variable est initialiser a 1 sinon la reponse sera zero
        for num in liste: # pas besoin d'excure le premier element
            total *= num
        return total
    # Divise chaque element de la liste par le premier et renvoie la reponse    
    elif operation == "/":
        total = liste[0]
        for num in liste[1:]: # liste[1:] permet d'exclure le premier element et garder le reste ex: ma_liste = [10, 5, 2, 1], print(ma_liste[1:]) Affiche : [5, 2, 1] (la liste sans le 1er élément)
            #Verifie que le denominateur n'est egale a zero
            if num == 0:
                print("Erreur : division par zéro détectée dans la liste.")
                return None
            total /= num
        return total
    #Si l'utilisateur  choisi de trouver le "min"   
    elif operation == "min":
        return min(liste)
    
    #Si l'utilisateur  choisi de trouver le "La moyenne"  
    elif operation == "moyenne":
        return sum(liste) / len(liste)
    
    # Renvoie une nouvelle liste triée    
    elif operation == "tri":
        # Renvoie une nouvelle liste triée
        return sorted(liste)
    else:
        print("Opérateur non reconnu pour la liste.")
        return None

#Fonction pour aditionner deux element
def addition(num1, num2):
    """
    Addition de deux valeurs.

    Args:
        num1 : premier valeur float ou int
        num2 : deuxieme valeur  float ou int
    Returns:
        float: total
    """
    return num1 + num2

#Fonction pour soustraire deux element
def soustraction(num1, num2):
    """
    Soustraction de deux valeurs.

    Args:
        num1 : premier valeur float ou int
        num2 : deuxieme valeur  float ou int
    Returns:
        float: total
    """
    return num1 - num2

#Fonction pour diviser deux element et verifie que le nombre n'est pas egale a zero
def division(num1, num2):
    """
    division de deux valeurs.

    Args:
        num1 : premier valeur float ou int
        num2 : deuxieme valeur  float ou int
    Returns:
        float: total
    """
    if num2 == 0:
        print("Erreur : vous ne pouvez pas diviser un nombre par zéro.")
        return None
    return num1 / num2

#Fonction pour Multiplier deux element
def multiplication(num1, num2):
    """
    multiplier deux valeurs.

    Args:
        num1 : premier valeur float ou int
        num2 : deuxieme valeur  float ou int
    Returns:
        float: total
    """
    return num1 * num2

#Importation du module math pour les calcules scientifique
import math

#Fonction pour Faire de calcules scientifique
def calcul_scientifique():
    """
    Fait des calcules scientifique .
    Returns:
        float
    """
    print("\n" + "="*20 + " MODE SCIENTIFIQUE " + "="*20)
    print("a - Racine carrée (√x)")
    print("b - Puissance (x^y)")
    print("c - Sinus (sin)")
    print("d - Cosinus (cos)")
    print("e - Logarithme népérien (ln)")
    print("f - Logarithme base 10 (log10)")
    
    # la fonction strip() permet d'effacer les espaces avant aprés les chaine de caractaire saisi
    # lower() permet de mettre tout en minuscul
    op_sci = input("Choisissez l'opération (a à f) : ").strip().lower()
    
    # verifie que la valeur saisi n'est pas une chaine de caractaire
    try:
        #Trouve la racine carrée d'un nombre
        if op_sci == 'a':
            num = float(input("Entrez le nombre : "))
            
            if num < 0: #Verifie que le nombre n'est pas inferieur a 0
                print("Erreur : impossible de calculer la racine carrée d'un nombre négatif.")
                return None
            return math.sqrt(num)
        
        #Trouve la puissance d'un nombre    
        elif op_sci == 'b':
            base = float(input("Entrez la base (x) : "))
            exposant = float(input("Entrez l'exposant (y) : "))
            return math.pow(base, exposant)
        
        #Trouve le sinus
        elif op_sci == 'c':
            num = float(input("Entrez l'angle (en radians) : "))
            return math.sin(num)
        
        #Trouve le Cosinus   
        elif op_sci == 'd':
            num = float(input("Entrez l'angle (en radians) : "))
            return math.cos(num)
            
        # Trouve le logarithme
        elif op_sci == 'e':
            num = float(input("Entrez le nombre (x > 0) : "))
            if num <= 0: #Verifie que la valeur n'est pas inferieur ou egale a zero
                print("Erreur : le logarithme n'est défini que pour les nombres strictement positifs.")
                return None
            return math.log(num)
        
        #Trouve log de base 10   
        elif op_sci == 'f':
            num = float(input("Entrez le nombre (x > 0) : "))
            if num <= 0: #Verifie que la valeur n'est pas inferieur ou egale a zero
                print("Erreur : le logarithme n'est défini que pour les nombres strictement positifs.")
                return None
            return math.log10(num)
            
        else:
            print("Opération scientifique non reconnue.")
            return None
            
    except ValueError:
        print("Erreur : veuillez saisir uniquement des chiffres.")
        return None

    
# --- BOUCLE PRINCIPALE ---
while True: # Ou encore while choix =! "quit"
    print("=" * 55)
    print("Quelle opération voulez-vous effectuer :")
    print("1- addition")
    print("2- soustraction")
    print("3- division")
    print("4- multiplication")
    print("6- scientifique")
    print("7- quit")
    
    choix = input("Votre choix (1-7 ou quit) : ").strip().lower()

    # Si l'utilisateur veut quitter
    if choix == '7' or choix == 'quit':
        print("Au revoir !")
        break

    # Opérations mathématiques basiques (choix 1 à 4)
    if choix in ['1', '2', '3', '4']:
        try:
            # On essaie de convertir les entrées en nombres (float)
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            # Si l'utilisateur tape des lettres au lieu de chiffres
            print("Erreur : veuillez saisir uniquement des chiffres (ex: 1, 2.5, 50).")
            continue

        if choix == '1':
            total = addition(num1, num2)
        elif choix == '2':
            total = soustraction(num1, num2)
        elif choix == '3':
            total = division(num1, num2)
        elif choix == '4':
            total = multiplication(num1, num2)
            
        if total is not None:
            print(f">>> Le résultat est : {total}")

    # Opération sur une liste (choix 5)
    elif choix == '5':
        operation = input("Choisissez l'opérateur (+, -, *, /, max, min, moyenne,tri ) : ")
        nombres_str = input("Entrez les nombres séparés par un espace : ")
        
        try:
            # On convertit la chaîne de caractères en une liste de floats
            # Creer une liste vide pour accueillir nos futurs nombres
            #liste = []
            # Découper le texte saisi par l'utilisateur (ex: "10 20 30" devient ["10", "20", "30"])
            #mots_decoupes = nombres_str.split()
            # boucle pour parcourir chaque mot découpé
            #for x in mots_decoupes:
                # Convertit le mot en nombre décimal
                #nombre = float(x)
                # Ajouter ce nombre à notre liste finale
                #liste.append(nombre)

            liste = [float(x) for x in nombres_str.split()] #La méthode .split() découpe la phrase d'origine à chaque fois qu'elle rencontre un espace. Elle transforme notre chaîne "10.5 20 5" en une liste de plusieurs petites chaînes de caractères : ["10.5", "20", "5"]
            total = calcul_list(liste, operation)
            if total is not None:
                print(f">>> Le résultat de la liste est : {total}")
                
        except ValueError:
            print("Erreur : veuillez saisir uniquement des chiffres valides.")

    # Si l'utilisateur choisit le mode scientifique
    elif choix == '6':
        total = calcul_scientifique()
        if total is not None:
            print(f">>> Le résultat scientifique est : {total}")
    else:
        print("Choix invalide. Veuillez sélectionner une option du menu.")

    # Demander s'il veut continuer
    print("-" * 20)
    continuer = input("Voulez-vous continuer ? (oui / quit) : ").strip().lower()
    if continuer == 'quit':
        print("Au revoir !")
        break