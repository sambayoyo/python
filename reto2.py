cadena = input("escribe una palabra")

if str(cadena) == str(cadena)[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")