import math

# Constantes astronomiques
UA_EN_KM = 149597870.7  # 1 Unité Astronomique (UA) en kilomètres
LUMIERE_PAR_AN_EN_KM = 9.461e12  # 1 année-lumière en kilomètres
PARSEC_EN_KM = 3.086e13  # 1 parsec en kilomètres

# Fonctions de conversion
def ua_to_km(ua):
    """Convertir des unités astronomiques (UA) en kilomètres."""
    return ua * UA_EN_KM

def km_to_ua(km):
    """Convertir des kilomètres en unités astronomiques (UA)."""
    return km / UA_EN_KM

def al_to_km(al):
    """Convertir des années-lumière (al) en kilomètres."""
    return al * LUMIERE_PAR_AN_EN_KM

def km_to_al(km):
    """Convertir des kilomètres en années-lumière (al)."""
    return km / LUMIERE_PAR_AN_EN_KM

def pc_to_km(pc):
    """Convertir des parsecs (pc) en kilomètres."""
    return pc * PARSEC_EN_KM

def km_to_pc(km):
    """Convertir des kilomètres en parsecs (pc)."""
    return km / PARSEC_EN_KM

# Calculer la luminosité d'une étoile à partir de sa magnitude apparente et de sa distance
def luminosity_from_magnitude(magnitude, distance_pc):
    """Calculer la luminosité d'une étoile à partir de sa magnitude apparente et de sa distance en parsecs."""
    distance_modulus = 5 * math.log10(distance_pc) - 5
    absolute_magnitude = magnitude + distance_modulus
    luminosity = 10**((absolute_magnitude - 4.83) / -2.5)
    return luminosity

# Affichage d'informations générales sur les unités astronomiques
def print_astronomical_info():
    """Afficher quelques informations générales sur les unités astronomiques."""
    print("\nQuelques informations sur les unités astronomiques :")
    print("1 Unité Astronomique (UA) est la distance moyenne entre la Terre et le Soleil.")
    print("1 année-lumière (al) est la distance parcourue par la lumière en un an.")
    print("1 parsec (pc) est une unité utilisée pour mesurer les distances aux étoiles.")

# Fonction de validation des entrées numériques
def demander_float(prompt):
    """Demander un nombre flottant et valider l'entrée."""
    while True:
        try:
            valeur = float(input(prompt))
            return valeur
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

# Fonction principale
def main():
    print("Bienvenue dans la calculatrice astronomique !")
    print_astronomical_info()
    
    while True:
        print("\nOptions:")
        print("1. Convertir des unités astronomiques (UA, parsec, année-lumière)")
        print("2. Calculer la luminosité d'une étoile")
        print("3. Quitter")
        
        choice = input("Choisissez une option (1/2/3): ")

        if choice == '1':
            print("\nChoisissez une conversion:")
            print("a. UA vers kilomètres")
            print("b. Kilomètres vers UA")
            print("c. Année-lumière vers kilomètres")
            print("d. Kilomètres vers année-lumière")
            print("e. Parsecs vers kilomètres")
            print("f. Kilomètres vers parsecs")
            
            conversion_choice = input("Choisissez une conversion (a-f): ")
            
            if conversion_choice in ['a', 'b', 'c', 'd', 'e', 'f']:
                value = demander_float("Entrez la valeur à convertir: ")
                
                if conversion_choice == 'a':
                    print(f"{value} UA = {ua_to_km(value)} km")
                elif conversion_choice == 'b':
                    print(f"{value} km = {km_to_ua(value)} UA")
                elif conversion_choice == 'c':
                    print(f"{value} al = {al_to_km(value)} km")
                elif conversion_choice == 'd':
                    print(f"{value} km = {km_to_al(value)} al")
                elif conversion_choice == 'e':
                    print(f"{value} pc = {pc_to_km(value)} km")
                elif conversion_choice == 'f':
                    print(f"{value} km = {km_to_pc(value)} pc")
            else:
                print("Choix de conversion invalide.")
        
        elif choice == '2':
            print("\nCalculer la luminosité d'une étoile:")
            magnitude = demander_float("Entrez la magnitude apparente de l'étoile: ")
            distance_pc = demander_float("Entrez la distance à l'étoile en parsecs: ")
            
            luminosity = luminosity_from_magnitude(magnitude, distance_pc)
            print(f"La luminosité de l'étoile est de {luminosity} fois la luminosité du Soleil.")
        
        elif choice == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, essayez à nouveau.")

# Lancer le programme
if __name__ == "__main__":
    main()
