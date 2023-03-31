while True:
    print("Bienvenue dans le menu de sélection")
    print("1. Ohms (Ω)")
    print("2. Puissance (W)")
    print("3. Option 3")
    print("4. Quitter")

    choix = int(input("Sélectionnez une option: "))

    if choix == 1:
        print("1. Utiliser R = U x I")
        print("2. Utiliser P = I² / R")
        print("3. Retour")

        sec_menu = int(input("Sélectionne quelle formule tu souhaites choisir : "))

        if sec_menu == 1:
            print("Tu as choisi la formule classique (R = U x I)")

            i=float(input("Donne la valeur I (A) : "))
            u=float(input("Donne la valeur U (V) : "))
            r=float(input("Donne la valeur R (Ω) : "))
            a=None

            if r == 0 :
                a=u/i
                b=1
            elif u == 0 :
                a=r*i
                b=2
            elif i == 0 :
                a=r/u
                b=3

            if b == 1 :
                print("\nRésulat :",a, "Ω\n")
            elif b == 2 :
                print("\nRésulat :",a, "V\n")
            elif b == 3 :
                print("\nRésulat :",a, "A\n")

        elif sec_menu == 2:
            print("Tu as choisi la formule avec I2 (P = I² / R)")

            i2=float(input("Donne la valeur I² (A) : "))
            r=float(input("Donne la valeur R (Ω) : "))
            p=float(input("Donne la valeur P (W) : "))
            a=None

            if p == 0 :
                a=r/i2
                b=1
            elif r == 0 :
                a=p/i2
                b=2
            elif i2 == 0 :
                a=p*r
                b=3

            if b == 1 :
                print("\nRésulat :",a, "W\n")
            elif b == 2 :
                print("\nRésulat :",a, "Ω\n")
            elif b == 3 :
                print("\nRésulat :",a, "A\n")

        elif sec_menu ==3 : 
            continue

    elif choix == 2:
        print("Vous avez choisi la formule de la puissance (P = U x I)")

        p=float(input("Donne la valeur P (W) : "))
        u=float(input("Donne la valeur U (V) : "))
        i=float(input("Donne la valeur I (A) : "))
        a=None

        if p == 0 :
            a=u*i
            b=1
        elif u == 0 :
            a=p/i
            b=2
        elif i == 0 :
            a=p/u
            b=3

        if b == 1 :
            print("\nRésulat :",a, "W\n")
        elif b == 2 :
            print("\nRésulat :",a, "V\n")
        elif b == 3 :
            print("\nRésulat :",a, "A\n")

    elif choix == 3:
        print("Vous avez choisi l'option 3")
    
    elif choix == 4:
        print("Au revoir")
        break

    else:
        print("Option non valide, veuillez choisir une option valide")