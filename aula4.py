while True:
        valor = int(input("Digite um valor positivo (ou zero para terminar): "))
        
        if valor < 0:
             print("Eu não gosto de números negativos, vamos tentar de novo.")
             continue
        
        if valor == 0:
            print("Ok, parando...")     
            break
        
        print("Você digitou {0}".format(valor))

print("Até mais!")
