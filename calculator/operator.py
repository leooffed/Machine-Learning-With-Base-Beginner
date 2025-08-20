def addiction(a, b):
    try:
        add = a + b
        return a + b
    except TypeError:
        print("Entrer une valeur numérique")

def sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Les valeurs doivent être numériques")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def substraction(a, b):
    try:
        return a - b
    except TypeError:
        print("Les valeurs doivent être numériques")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def multiplication(a, b):
    try:
        return a * b
    except TypeError:
        print("Les valeurs doivent être numériques")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro")
    except TypeError:
        print("Les valeurs doivent être numériques")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def power(a, b):
    try:
        return a ** b
    except TypeError:
        print("Les valeurs doivent être numériques")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

