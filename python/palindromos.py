palabra=str(input("Digite una palabra: "))
palabra=palabra.replace(" ","")
palabra=palabra.lower()
if palabra==palabra[::-1]:
    print("Es un palindromo")
else :
    print("No es un palindromo")