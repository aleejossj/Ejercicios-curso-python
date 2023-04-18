def run():
    # for contador in range (100):
    #     if contador%2 !=0:
    #         continue
    #     print(contador)
    texto=input("Escriba un texto: ")
    for letra in texto:
        if letra =='i':
            break
        print(letra)

if __name__=='__main__':
    run()