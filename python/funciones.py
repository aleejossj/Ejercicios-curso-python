def imprimir_Mensaje(mensaje):
    print('Hola')
    print('Como estas')    
    print(mensaje)
    print('Adios')

opcion=int(input("Elija una opcion (1,2,3): "))

if opcion==1:
    imprimir_Mensaje('Elegiste la opcion 1')
elif opcion==2:
    imprimir_Mensaje('Elegiste la opcion 2')
elif opcion==3:
    imprimir_Mensaje('Elegiste la opcion 3')
else:
    print("La opcion digitada no existe")


