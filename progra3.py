import random
from tkinter import *

class tablero():
    def __init__(self,mapa):
        self.mapa = mapa
    
        
        
class peon():
    def __init__(self,nombre,vida,items):
        self.nombre = nombre
        self.vida = vida
        self.items = items
        super().__init__(nombre,vida,items)

class player(peon,tablero):
    def __init__(self,nombre,vida,items):
        self.nombre = nombre
        self.vida = vida
        self.items = items

"""ffffffffffffffffffffffffffffffffffffffffffffff"""    
    def mover(self,dir):
        
            cont = 0
            if dir == 1:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player1.nombre:
                            
                            nuevo = lista.index(player1.nombre) + 1
                            if nuevo != 8:
                                if nuevo != zombiex.nombre and nuevo != zombiey.nombre and nuevo != zombiez.nombre:
                                    if nuevo != "obstaculo":
                                        viejo = lista.index(player1.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player1.nombre
                                        
                                        for x in tablero1.mapa:
                                            print(x)
                                        main1.main()
                                        cont += 1
                                        break
                                    else:
                                        print("invalido")
                                else:
                                    print("invalido")
                            else:
                                print("invalido")
            if dir == 2:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player2.nombre:
                            
                            nuevo = lista.index(player2.nombre) + 1
                            if nuevo != 8:
                                if nuevo != zombiex.nombre and nuevo != zombiey.nombre and nuevo != zombiez.nombre:
                                    if nuevo != "obstaculo":
                                        viejo = lista.index(player2.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player2.nombre
                                        for x in tablero1.mapa:
                                            print(x)
                                        cont += 1
                                        main1.main()
                                        break
                                    else:
                                        print("invalido")
                                else:
                                    print("invalido")
                            else:
                                print("invalido")
            if dir == 3:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            
                            nuevo = lista.index(player3.nombre) + 1
                            if nuevo != 8:
                                if lista[nuevo] != zombiex.nombre or lista[nuevo] != zombiey.nombre or lista[nuevo] != zombiez.nombre:
                                    
                                    if nuevo != "obstaculo":
                                        viejo = lista.index(player3.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player3.nombre
                                        for x in tablero1.mapa:
                                            print(x)
                                        main1.zzombie()
                                        cont += 1
                                        break
                                    else:
                                        print("Invalido")
                                else:
                                    print("invalido")

                            else:
                                print("invalido")

            if dir == 4:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player1.nombre:
                                c = tablero1.mapa.index(lista)
                                print(c)
                                if c == 4:
                                    print("Invalido")
                                    main1.main()
                                    break
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player1.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = player1.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False
                                    
                                    
                                    main1.main()
                                    break

            if dir == 5:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player2.nombre:
                                c = tablero1.mapa.index(lista)
                                print(c)
                                if c == 4:
                                    print("Invalido")
                                    main1.main()
                                    break
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player2.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = player2.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False
                                    
                                    main1.main()
                                    break
                                    
                            

            if dir == 6:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player3.nombre:
                                c = tablero1.mapa.index(lista)
                                print(c)
                                if c == 0:
                                    print("Invalido")
                                    main1.main()
                                    break
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player3.nombre)
                                    lista[viejo] = 0
                                    if c == 4:
                                        c = -1
                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = player3.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False
                                    
                                    main1.zzombie()
                                    break

            if dir == 7:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player1.nombre:
                                c = tablero1.mapa.index(lista)
                                #print(c)
                                
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player1.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = player1.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False

                                    
                                    main1.main()
                                    break    
            
            if dir == 8:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player2.nombre:
                                c = tablero1.mapa.index(lista)
                                #print(c)
                                
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player2.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = player2.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False
                                    
                                    main1.main()
                                    break
            
            if dir == 9:
                m = True
                while m == True:
                    for lista in tablero1.mapa:
                        for x in lista:
                            if x == player3.nombre:
                                c = tablero1.mapa.index(lista)
                                #print(c)
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player3.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = player3.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    cont += 1
                                    m = False
                                    
                                    main1.zzombie()
                                    break
            if dir == 10:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player1.nombre:
                            if lista.index(player1.nombre) == 1:
                                print("invalido")
                            nuevo = lista.index(player1.nombre) - 1
                            
                            viejo = lista.index(player1.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player1.nombre
                            for x in tablero1.mapa:
                                print(x)
                            cont += 1
                            main1.main()
                            break
            if dir == 11:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player2.nombre:
                            if lista.index(player2.nombre) == 1:
                                print("invalido")
                            nuevo = lista.index(player2.nombre) - 1
                            
                            viejo = lista.index(player2.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player2.nombre
                            for x in tablero1.mapa:
                                print(x)
                            cont += 1
                            main1.main()
                            break
            if dir == 12:
                
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            if lista.index(player3.nombre) == 1:
                                print("invalido")
                                main1.main()
                                break
                            nuevo = lista.index(player3.nombre) - 1
                            
                            viejo = lista.index(player3.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player3.nombre
                            for x in tablero1.mapa:
                                print(x)
                            cont += 1
                            main1.zzombie()
                            break
                       

    def atacar(self):
        atq = input(("Diga 1 para que persoanje1 ataque, 2 para que personaje2 ataque, 3 para que personaje3 ataque "))
        
        if atq == 1:
            for lista in tablero1.mapa:
                    for x in lista:
                        if x == player1.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player1.nombre) + 1
                            atras = lista.index(player1.nombre) - 1
                            
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] == zombiex.items
                                break
                            if lista[nuevo] == zombiey.nombre: 
                                lista[nuevo] == zombiey.items
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] == zombiez.items
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] == zombiex.items
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] == zombiey.items
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] == zombiez.items
                                break
                            num = tablero1.mapa.index(lista) - 1
                            print(num)
                            print(i)
                            try:
                                arriba = tablero1.mapa[num][i]
                                if arriba == zombiex.nombre: 
                                    arriba == zombiex.items
                                if arriba == zombiey.nombre: 
                                    arriba == zombiey.items
                                if arriba == zombiez.nombre: 
                                    arriba == zombiez.items
                                
                                break
                            except:
                                try:
                                    num2 = tablero1.mapa.index(lista) + 1
                                    
                                    abajo = tablero1.mapa[num2][i]
                                    if abajo == zombiex.nombre: 
                                        abajo == zombiex.items
                                    if abajo == zombiey.nombre: 
                                        abajo == zombiey.items
                                    if abajo == zombiez.nombre: 
                                        abajo == zombiez.items
                                    break
                                except:
                                    print("no deberia llegar aqui")
                                    break        
                    

                            

                                
        if atq ==2:
            for lista in tablero1.mapa:
                    for x in lista:
                        if x == player2.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player2.nombre) + 1
                            atras = lista.index(player2.nombre) - 1
                            
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] == zombiex.items
                                break
                            if lista[nuevo] == zombiey.nombre: 
                                lista[nuevo] == zombiey.items
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] == zombiez.items
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] == zombiex.items
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] == zombiey.items
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] == zombiez.items
                                break
                            num = tablero1.mapa.index(lista) - 1
                            print(num)
                            print(i)
                            try:
                                arriba = tablero1.mapa[num][i]
                                if arriba == zombiex.nombre: 
                                    arriba == zombiex.items
                                if arriba == zombiey.nombre: 
                                    arriba == zombiey.items
                                if arriba == zombiez.nombre: 
                                    arriba == zombiez.items
                                
                                break
                            except:
                                try:
                                    num2 = tablero1.mapa.index(lista) + 1
                                    
                                    abajo = tablero1.mapa[num2][i]
                                    if abajo == zombiex.nombre: 
                                        abajo == zombiex.items
                                    if abajo == zombiey.nombre: 
                                        abajo == zombiey.items
                                    if abajo == zombiez.nombre: 
                                        abajo == zombiez.items
                                    break
                                except:
                                    print("no deberia llegar aqui")
                                    break        
                    


        if atq == 3:
            for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player3.nombre) + 1
                            atras = lista.index(player3.nombre) - 1
                            
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] == zombiex.items
                                break
                            if lista[nuevo] == zombiey.nombre: 
                                lista[nuevo] == zombiey.items
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] == zombiez.items
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] == zombiex.items
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] == zombiey.items
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] == zombiez.items
                                break
                            num = tablero1.mapa.index(lista) - 1
                            print(num)
                            print(i)
                            try:
                                arriba = tablero1.mapa[num][i]
                                if arriba == zombiex.nombre: 
                                    arriba == zombiex.items
                                if arriba == zombiey.nombre: 
                                    arriba == zombiey.items
                                if arriba == zombiez.nombre: 
                                    arriba == zombiez.items
                                
                                break
                            except:
                                try:
                                    num2 = tablero1.mapa.index(lista) + 1
                                    
                                    abajo = tablero1.mapa[num2][i]
                                    if abajo == zombiex.nombre: 
                                        abajo == zombiex.items
                                    if abajo == zombiey.nombre: 
                                        abajo == zombiey.items
                                    if abajo == zombiez.nombre: 
                                        abajo == zombiez.items
                                    break
                                except:
                                    print("no deberia llegar aqui")
                                    break        
                    

                            

        
    
class zombie(tablero,peon):
    def __init__(self,nombre,vida,items):
        self.nombre = nombre
        self.vida = vida
        self.items = items
        
    def mover(self):
        for lista in tablero1.mapa:
            for x in lista:
                if x == zombiex.nombre:
                    nuevo = lista.index(zombiex.nombre) - 1
                    if lista[nuevo] != "Base":
                        if lista[nuevo] == player1.nombre or lista[nuevo] == player2 or lista[nuevo] == player3.nombre:
                            print("aleluya")
                            main1.zzombieatq()
                            break
                        else:
                            if lista[nuevo] != "obstaculo":
                                viejo = lista.index(zombiex.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiex.nombre
                                        
                                for x in tablero1.mapa:
                                    print(x)
                                #zombiey.mover()
                                
                                
                                break                            
                            else: 
                                print("invalido")
                        
                    else:
                        print("ganaron los zombies")
                
                if x == zombiey.nombre:
                    nuevo = lista.index(zombiey.nombre) - 1
                    if lista[nuevo] != "Base":
                        if lista[nuevo] == player1.nombre or lista[nuevo] == player2.nombre or lista[nuevo]== player3.nombre:
                            main1.zzombieatq()
                        else:
                            if lista[nuevo] != "obstaculo":
                                viejo = lista.index(zombiey.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiey.nombre
                                        
                                for x in tablero1.mapa:
                                    print(x)
                                #zombiey.mover()
                                
                                
                                break
                                
                            else: 
                                print("invalido")
                        
                    else:
                        print("ganaron los zombies")
                
                if x == zombiez.nombre:
                    nuevo = lista.index(zombiez.nombre) - 1
                    if lista[nuevo] != "Base":
                        if lista[nuevo] == player1.nombre or lista[nuevo] == player2 or lista[nuevo] == player3.nombre:
                            
                             
                            main1.zzombieatq()
                        else:
                            if lista[nuevo] != "obstaculo":
                                viejo = lista.index(zombiez.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiez.nombre
                                        
                                for x in tablero1.mapa:
                                    print(x)
                                #zombiey.mover()
                                
                                main1.main()
                                break
                            else: 
                                print("invalido")
                    else:
                        print("ganaron los zombies")
                continue

            """cont = 0
            while cont < 4:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == zombiex.nombre:
                            c = tablero1.mapa.index(lista)
                            if c == 4:
                                print("Invalido")
                            if tablero1.mapa[c] == lista:
                                viejo = lista.index(zombiex.nombre)
                                aux = lista
                                lista = tablero1.mapa[c+3]
                                abajo = lista[viejo]
                                if abajo == player1.nombre or abajo == player2.nombre or abajo == player3.nombre:

                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = zombiex.nombre
                                    aux[viejo] = 0

                                aux = tablero1.mapa[c-3]
                                arriba = aux[viejo]
                                if arriba == player1.nombre or arriba == player2.nombre or arriba == player3.nombre:

                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = zombiex.nombre
                                    aux[viejo] = 0
                            else:
                                nuevo = lista.index(zombiex.nombre) - 1
                                viejo = lista.index(zombiex.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiex.nombre
                                print(tablero1.mapa)
                                cont += 1
        
                        if x == zombiey.nombre:

                            c = tablero1.mapa.index(lista)
                            if c == 4:
                                print("Invalido")
                            if tablero1.mapa[c] == lista:
                                viejo = lista.index(zombiey.nombre)
                                aux = lista
                                lista = tablero1.mapa[c+3]
                                abajo = lista[viejo]
                                if abajo == player1.nombre or abajo == player2.nombre or abajo == player3.nombre:

                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = zombiey.nombre
                                    aux[viejo] = 0

                                aux = tablero1.mapa[c-3]
                                arriba = aux[viejo]
                                if arriba == player1.nombre or arriba == player2.nombre or arriba == player3.nombre:

                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = zombiey.nombre
                                    aux[viejo] = 0
                            else:
                                nuevo = lista.index(zombiey.nombre) - 1
                                viejo = lista.index(zombiey.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiey.nombre
                                #print(tablero1.mapa)
                                cont += 1
        
                        
            
                        if x == zombiez.nombre:
                            c = tablero1.mapa.index(lista)
                            if c == 4:
                                print("Invalido")
                            if tablero1.mapa[c] == lista:
                                viejo = lista.index(zombiez.nombre)
                                aux = lista
                                lista = tablero1.mapa[c+3]
                                abajo = lista[viejo]
                                if abajo == player1.nombre or abajo == player2.nombre or abajo == player3.nombre:

                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = zombiez.nombre
                                    aux[viejo] = 0

                                aux = tablero1.mapa[c-3]
                                arriba = aux[viejo]
                                if arriba == player1.nombre or arriba == player2.nombre or arriba == player3.nombre:

                                    lista = tablero1.mapa[c-1]
                                    lista[viejo] = zombiez.nombre
                                    aux[viejo] = 0
                            else:
                                nuevo = lista.index(zombiez.nombre) - 1
                                viejo = lista.index(zombiez.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiez.nombre
                                print(tablero1.mapa)
                                cont += 1
        
                else:
                    main1.main()"""
        
    def atacar(self):

        print("ataquw wn peoceso1")
        for lista in tablero1.mapa:
            for x in lista:
                if x == zombiex.nombre:
                    aux = lista
                    i = lista.index(x)
                    nuevo = lista.index(zombiex.nombre) - 1
                    atras = lista.index(zombiex.nombre) + 1
                            
                    if lista[nuevo] == player1.nombre: 
                        lista[nuevo] = player1.items
                        print("q outas")
                        for x in tablero1.mapa:
                            print(x)
                        break
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] == player2.items
                        break
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] == player3.items
                        break

                    if lista[atras] == player1.nombre: 
                        lista[atras] == player1.items
                        break
                    if lista[atras] == player2.nombre: 
                        lista[atras] == player2.items
                        break
                    if lista[atras] == player3.nombre: 
                        lista[atras] == player3.items
                        break
                    num = tablero1.mapa.index(lista) - 1
                    print(num)
                    print(i)
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba == player1.items
                        if arriba == player2.nombre: 
                            arriba == player2.items
                        if arriba == player3.nombre: 
                            arriba == player3.items
                        
                        break
                    except:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                            
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo == player1.items
                            if abajo == player2.nombre: 
                                abajo == player2.items
                            if abajo == player3.nombre: 
                                abajo == player3.items
                            break
                        except:
                            print("no deberia llegar aqui")
                            break        
            

                            
        
            if x == zombiey.nombre:
                aux = lista
                i = lista.index(x)
                nuevo = lista.index(zombiey.nombre) - 1
                atras = lista.index(zombiey.nombre) + 1
                            
                if lista[nuevo] == player1.nombre: 
                    lista[nuevo] == player1.items
                    break
                if lista[nuevo] == player2.nombre: 
                    lista[nuevo] == player2.items
                    break
                if lista[nuevo] == player3.nombre: 
                    lista[nuevo] == player3.items
                    break

                if lista[atras] == player1.nombre: 
                    lista[atras] == player1.items
                    break
                if lista[atras] == player2.nombre: 
                    lista[atras] == player2.items
                    break
                if lista[atras] == player3.nombre: 
                    lista[atras] == player3.items
                    break
                num = tablero1.mapa.index(lista) - 1
                print(num)
                print(i)
                try:
                    arriba = tablero1.mapa[num][i]
                    if arriba == player1.nombre: 
                        arriba == player1.items
                    if arriba == player2.nombre: 
                        arriba == player2.items
                    if arriba == player3.nombre: 
                        arriba == player3.items
                        
                    break
                except:
                    try:
                        num2 = tablero1.mapa.index(lista) + 1
                            
                        abajo = tablero1.mapa[num2][i]
                        if abajo == player1.nombre: 
                            abajo == player1.items
                        if abajo == player2.nombre: 
                            abajo == player2.items
                        if abajo == player3.nombre: 
                            abajo == player3.items
                        break
                    except:
                        print("no deberia llegar aqui")
                        break        
            

                            
                break            
        
            if x == zombiez.nombre:
                aux = lista
                i = lista.index(x)
                nuevo = lista.index(zombiez.nombre) - 1
                atras = lista.index(zombiez.nombre) + 1
                            
                if lista[nuevo] == player1.nombre: 
                    lista[nuevo] == player1.items
                    break
                if lista[nuevo] == player2.nombre: 
                    lista[nuevo] == player2.items
                    break
                if lista[nuevo] == player3.nombre: 
                    lista[nuevo] == player3.items
                    break

                if lista[atras] == player1.nombre: 
                    lista[atras] == player1.items
                    break
                if lista[atras] == player2.nombre: 
                    lista[atras] == player2.items
                    break
                if lista[atras] == player3.nombre: 
                    lista[atras] == player3.items
                    break
                num = tablero1.mapa.index(lista) - 1
                print(num)
                print(i)
                try:
                    arriba = tablero1.mapa[num][i]
                    if arriba == player1.nombre: 
                        arriba == player1.items
                    if arriba == player2.nombre: 
                        arriba == player2.items
                    if arriba == player3.nombre: 
                        arriba == player3.items
                        
                    break
                except:
                    try:
                        num2 = tablero1.mapa.index(lista) + 1
                            
                        abajo = tablero1.mapa[num2][i]
                        if abajo == player1.nombre: 
                            abajo == player1.items
                        if abajo == player2.nombre: 
                            abajo == player2.items
                        if abajo == player3.nombre: 
                            abajo == player3.items
                        break
                    except:
                        print("no deberia llegar aqui")
                        break        
            


zombiex = zombie("Zombie X",True,"Pistola")
zombiey = zombie("Zombie Y",True,"Medicina")
zombiez = zombie("Zombie Z",True,"Pocion")
player1 = player("Player1",True,"Pistola")
player2 = player("Player2",True,"Cuchillo")
player3 = player("Player3",True,"Pistola2")
tablero1 = tablero([["Base",player1.nombre,0,0,0,0,0,zombiex.nombre],
            ["Base",0,0,0,0,0,0,"SpawnPoint"],
            ["Base",player2.nombre,0,0,0,0,0,zombiey.nombre],
            ["Base",0,0,0,0,0,0,"Spawnpoint"],
            ["Base",player3.nombre,0,0,0,0,0,zombiez.nombre]])

for x in tablero1.mapa:
    print(x)
class main():
    def main(self):
        
            
            dir = int(input(("diga 1 para mover personaje1 hacia adelante,",
                    "2 para mover personaje2 hacia adelante",
                    "3 para mover personaje3 hacia adelante",
                    "4 para mover personaje1 hacia abajo",
                    "5 para mover personaje2 hacia abajo",
                    "6 para mover personaje3 hacia abajo",
                    "7 personaje1 arriba",
                    "8 personaje2 arriba",
                    "9 personaje3 arriba",
                    "10 personaje1 atras",
                    "11 p2 atras",
                    "12 p3 atras")))
            
            if dir == 1:
                player1.mover(dir)
            if dir == 2:
                player2.mover(dir)
            if dir == 3:
                player3.mover(dir)
            if dir == 4:
                #print("gg")
                player1.mover(dir)
            if dir == 5:
                player2.mover(dir)
            if dir == 6:
                player3.mover(dir)
            if dir == 7:
                player1.mover(dir)
            if dir == 8:
                player2.mover(dir)
            if dir == 9:
                player3.mover(dir)
            if dir == 10:
                player1.mover(dir)
            if dir == 11:
                player2.mover(dir)
            if dir == 12:
                player3.mover(dir)

    def zzombie(self):
        zombiex.mover()
        zombiey.mover()
        zombiez.mover()

    def zzombieatq(self):
        zombiex.atacar()
        zombiey.atacar()
        zombiez.atacar()
    
            #else:
                #print("opcion no valida")
                
            #dirz = (input(("diga x para mover zombie x hacia adelante,/n"
                # "y para mover zombie y hacia adelante/n",
                    #"z para mover zombie z hacia adelante")))
            #if dirz == "x":
                #zombiex.mover(dirz)
            #if dirz == "y":
                #zombiey.mover(dirz)
        # if dirz == "z":
            # zombiez.mover(dirz)

"""class mover_matriz(object):
    x = 0
    y = 0
    boton = None

    def __init__(self, x, y, ventana, matrix):
        colores = {0: "red", "Base": "yellow", "Player1" : "blue", "Player2" : "blue", "Player2" : "blue", "Zombie X" : "green", "Zombie Y" : "pink", "Zombie Z" : "orange"}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    fontcolor = "white"
                else:
                    fontcolor = "black"
        #global x
        #global y
        self.x = x
        self.y = y
        boton = Button(ventana, text = matrix[x][y],fg=fontcolor, width=4, heigh=2, bg=colores[matrix[x][y]], font="Arial",command = lambda: ventana.after(200, gui.coord3(self.x, self.y)))
        boton.grid(row = self.x, column = self.y)



class ventanaJuego():
    def __init__(self,ventana):
        self.ventana = ventana
    def gui(self):
        #ventana = Tk()
        ventana.geometry("800x500") #dimensiones

        ventana.config(bg="rosybrown1")  
        #botones(ventana,tablero1.mapa)

    def botones(self,ventana, mapa):
    #global j,i
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                mover_matriz(j, i, ventana, mapa)    

    def coord3(self,x, y):
        print("x:", x, "y:", y)
        
        
        pos = (x,y)
        return (x,y)

ventana = Tk()
gui = ventanaJuego(ventana)
gui.gui()   
gui.botones(ventana,tablero1.mapa)  """
main1 = main()
main1.main()
#main1.zzombie()
