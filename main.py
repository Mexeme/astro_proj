import math

# Constantes astronomiques
UA_EN_KM = 149597870.7  # 1 Unité Astronomique (UA) en kilomètres
LUMIERE_PAR_AN_EN_KM = 9.461e12  # 1 année-lumière en kilomètres
PARSEC_EN_KM = 3.086e13  # 1 parsec en kilomètres

# Fonctions de conversion
def ua_to_km(ua):
    return ua * UA_EN_KM

def km_to_ua(km):
    return km / UA_EN_KM

def al_to_km(al):
    return al * LUMIERE_PAR_AN_EN_KM

def km_to_al(km):
    return km / LUMIERE_PAR_AN_EN_KM

def pc_to_km(pc):
    return pc * PARSEC_EN_KM

def km_to_pc(km):
    return km / PARSEC_EN_KM

# Calcul de la luminosité d'une étoile
def luminosity_from_magnitude(magnitude, distance_pc):
    distance_modulus = 5 * math.log10(distance_pc) - 5
    absolute_magnitude = magnitude + distance_modulus
    luminosity = 10**((absolute_magnitude - 4.83) / -2.5)
    return luminosity

# Fonction principale
def main():
    print("Bienvenue dans la calculatrice astronomique !")
    print("\nQuelques informations sur les unités astronomiques :")
    print("1 UA = distance moyenne entre la Terre et le Soleil.")
    print("1 année-lumière = distance parcourue par la lumière en un an.")
    print("1 parsec = unité pour mesurer les distances aux étoiles.")

    while True:
        print("\nMenu Principal :")
        print("1. Conversion d'unités")
        print("2. Calcul de la luminosité d'une étoile")
        print("3. Quitter")

        choice = input("Choisissez une option (1/2/3) : ")

        if choice == '1':
            while True:
                print("\nMenu Conversion :")
                print("a. UA vers kilomètres")
                print("b. Kilomètres vers UA")
                print("c. Année-lumière vers kilomètres")
                print("d. Kilomètres vers année-lumière")
                print("e. Parsecs vers kilomètres")
                print("f. Kilomètres vers parsecs")
                print("q. Retour au menu principal")

                conversion_choice = input("Choisissez une conversion (a-f ou q) : ")

                if conversion_choice == 'q':
                    break

                if conversion_choice in ['a', 'b', 'c', 'd', 'e', 'f']:
                    try:
                        value = float(input("Entrez la valeur à convertir : "))
                        if conversion_choice == 'a':
                            print(f"{value} UA = {ua_to_km(value):.2f} km")
                        elif conversion_choice == 'b':
                            print(f"{value} km = {km_to_ua(value):.2f} UA")
                        elif conversion_choice == 'c':
                            print(f"{value} al = {al_to_km(value):.2e} km")
                        elif conversion_choice == 'd':
                            print(f"{value} km = {km_to_al(value):.2e} al")
                        elif conversion_choice == 'e':
                            print(f"{value} pc = {pc_to_km(value):.2e} km")
                        elif conversion_choice == 'f':
                            print(f"{value} km = {km_to_pc(value):.2e} pc")
                        break  # Retourner au menu principal après une conversion réussie
                    except ValueError:
                        print("Erreur : Veuillez entrer un nombre valide.")
                else:
                    print("Choix invalide, veuillez réessayer.")

        elif choice == '2':
            while True:
                print("\nCalcul de la luminosité d'une étoile :")
                try:
                    magnitude = float(input("Entrez la magnitude apparente de l'étoile : "))
                    distance_pc = float(input("Entrez la distance à l'étoile en parsecs : "))
                    luminosity = luminosity_from_magnitude(magnitude, distance_pc)
                    print(f"La luminosité de l'étoile est de {luminosity:.2f} fois la luminosité du Soleil.")
                    break  # Retour au menu principal après un calcul réussi
                except ValueError:
                    print("Erreur : Veuillez entrer des valeurs valides.")


        elif choice == '3':
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme
if __name__ == "__main__":
    main()
