import string
import secrets

# Demande les préférences et valide la longueur avant de continuer
def saisir_preferences():
    while True:
        try:
            longueur = int(input("\nLongueur souhaitée (8-32) : "))
            if longueur < 8 or longueur > 32:
                print("\nValeurs incorrectes. Veuillez recommencer.\n")
            else:
                chiffres = input("\nInclure des chiffres ? (o/n) : ").lower()
                c_speciaux = input("\nInclure des caractères spéciaux ? (o/n) : ").lower()
                break
        # Saisie non numérique interceptée proprement
        except ValueError:
            print("\nVeuillez entrer un nombre entier.\n")
    return longueur, chiffres, c_speciaux


def generer_mot_de_passe(longueur, chiffres, c_speciaux):
    reservoir = string.ascii_letters
    # Liste plutôt que string : plus efficace pour append et shuffle
    mot_de_passe = []
    
    # Garantit la présence d'au moins une majuscule et une minuscule
    mot_de_passe.append(secrets.choice(string.ascii_uppercase))
    mot_de_passe.append(secrets.choice(string.ascii_lowercase))
    
    if chiffres == "o":
        reservoir += string.digits
        mot_de_passe.append(secrets.choice(string.digits))
    
    if c_speciaux == "o":
        reservoir += string.punctuation
        mot_de_passe.append(secrets.choice(string.punctuation))
    
    # Complète le reste de la longueur avec des caractères aléatoires
    for i in range(longueur - len(mot_de_passe)):
        mot_de_passe.append(secrets.choice(reservoir))
    
    # Mélange sûr d'etre complètement aléatoire
    secrets.SystemRandom().shuffle(mot_de_passe)
    
    return "".join(mot_de_passe)


def main():
    print("\n=== Générateur de mot de passe ===")
    while True:
        longueur, chiffres, c_speciaux = saisir_preferences()
        mot_de_passe = generer_mot_de_passe(longueur, chiffres, c_speciaux)
        print(f"\nMot de passe généré : {mot_de_passe}")
        
        recommencer = input("\nGénérer un nouveau mot de passe ? (o/n) : ").lower()
        if recommencer == "n":
            print("\nA bientôt !\n")
            break
    
if __name__ == "__main__":
    main()
