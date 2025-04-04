def change():
    expense = 23.75
    money = 100
    
    print ("Ingresas gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print ("\nVuelto\n")
    print ("Pesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    print (pesos)
    print ("Centavos:")
    centavos= vuelto-pesos
    centavos_entero=int(centavos*100)
    print (centavos_entero)


change()
