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
                                        tablerogui(ventana,tablero1.mapa)
                                        
                                        for x in tablero1.mapa:
                                            print(x)
                                        if player2.vida == True or player3.vida == True:
                                            #main1.main()
                                            break
                                        else:
                                            main1.zzombie()
                                            break
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
                                        tablerogui(ventana,tablero1.mapa)
                                        cont += 1
                                        if player1.vida == True or player3.vida == True:
                                            #main1.main()
                                            break
                                        else:
                                            main1.zzombie()
                                            break
                                        
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
                                        tablerogui(ventana,tablero1.mapa)
                                        if player2.vida == True or player1.vida == True:
                                            #main1.main()
                                            break
                                        else:
                                            main1.zzombie()
                                            break
                                        
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
                                    #main1.main()
                                    break
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player1.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = player1.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False
                                    
                                    
                                    if player2.vida == True or player3.vida == True:
                                        #main1.main()
                                        break
                                    else:
                                        main1.zzombie()
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
                                    #main1.main()
                                    break
                                
                                if tablero1.mapa[c] == lista:


                                    viejo = lista.index(player2.nombre)
                                    lista[viejo] = 0
                                    
                                    lista = tablero1.mapa[c+1]
                                    lista[viejo] = player2.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False
                                    
                                    if player1.vida == True or player3.vida == True:
                                        #main1.main()
                                        break
                                    else:
                                        main1.zzombie()
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
                                    #main1.main()
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
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False
                                    
                                    if player1.vida == True or player2.vida == True:
                                        #main1.main()
                                        break
                                    else:
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
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False

                                    
                                    if player2.vida == True or player3.vida == True:
                                        #main1.main()
                                        break
                                    else:
                                        main1.zzombie()
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
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False
                                    
                                    if player1.vida == True or player3.vida == True:
                                        #main1.main()
                                        break
                                    else:
                                        main1.zzombie()
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
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    m = False
                                    
                                    if player2.vida == True or player1.vida == True:
                                        #main1.main()
                                        break
                                    else:
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
                            tablerogui(ventana,tablero1.mapa)
                            cont += 1
                            if player2.vida == True or player3.vida == True:
                                #main1.main()
                                break
                            else:
                                main1.zzombie()
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
                            tablerogui(ventana,tablero1.mapa)
                            cont += 1
                            if player1.vida == True or player3.vida == True:
                                #main1.main()
                                break
                            else:
                                main1.zzombie()
                                break

            if dir == 12:
                
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            if lista.index(player3.nombre) == 1:
                                print("invalido")
                                #main1.main()
                                break
                            nuevo = lista.index(player3.nombre) - 1
                            
                            viejo = lista.index(player3.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player3.nombre
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            cont += 1
                            if player1.vida == True or player2.vida == True:
                                #main1.main()
                                break
                            else:
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
                            if lista[nuevo] == 0:
                                viejo = lista.index(zombiex.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiex.nombre
                                        
                                for x in tablero1.mapa:
                                    print(x)
                                    tablero(tablero1.mapa)
                                #zombiey.mover()
                                
                                
                                break                            
                            else: 
                                print("invalido")
                        
                    else:
                        print("zombiex")
                        print("ganaron los zombies")
                
                if x == zombiey.nombre:
                    nuevo = lista.index(zombiey.nombre) - 1
                    if lista[nuevo] != "Base":
                        if lista[nuevo] == player1.nombre or lista[nuevo] == player2.nombre or lista[nuevo]== player3.nombre:
                            main1.zzombieatq()
                            break
                        else:
                            if lista[nuevo] == 0:
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
                            break
                        else:
                            if lista[nuevo] == 0:
                                viejo = lista.index(zombiez.nombre)
                                lista[viejo] = 0
                                lista[nuevo] = zombiez.nombre
                                        
                                for x in tablero1.mapa:
                                    print(x)
                                #zombiey.mover()
                                
                                #main1.main()
                                break
                            else: 
                                print("invalido")
                    else:
                        print("ganaron los zombies")
                

            
        
    def atacar(self):

        print("ataque en proceso")
        for lista in tablero1.mapa:
            for x in lista:
                if x == zombiex.nombre:
                    print(zombiex.nombre)
                    aux = lista
                    i = lista.index(x)
                    nuevo = lista.index(zombiex.nombre) - 1
                    atras = lista.index(zombiex.nombre) + 1
                            
                    if lista[nuevo] == player1.nombre: 
                        lista[nuevo] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                    num = tablero1.mapa.index(lista) - 1
                    
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba = player1.items
                            player1.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                        
                        break
                    except:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                            
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            break
                        except:
                            print("no deberia llegar aqui")
                            break        
                
    def y(self):
        for lista in tablero1.mapa:
            for x in lista:                  
                if x == zombiey.nombre:
                    print(zombiey.nombre)
                    aux = lista
                    i = lista.index(x)
                    nuevo = lista.index(zombiey.nombre) - 1
                    atras = lista.index(zombiey.nombre) + 1
                                
                    if lista[nuevo] == player1.nombre: 
                        lista[nuevo] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                        
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        break
                        
                    num = tablero1.mapa.index(lista) - 1
                    print(num)
                    print(i)
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba = player1.items
                            player1.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            break
                            
                        
                    except:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                                
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                break
                            
                        except:
                            print("no deberia llegar aqui")
                            break        
                
                                
    def z(self):
        for lista in tablero1.mapa:
            for x in lista:    
                if x == zombiez.nombre:
                    print(zombiez.nombre)
                    aux = lista
                    i = lista.index(x)
                    nuevo = lista.index(zombiez.nombre) - 1
                    atras = lista.index(zombiez.nombre) + 1
                                
                    if lista[nuevo] == player1.nombre: 
                        lista[nuevo] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        #main1.main()
                        break
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        #main1.main()
                        break
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        
                        
                        #main1.main()
                        break

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        #main1.main()
                        
                        break
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        #main1.main()
                        
                        break
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        #main1.main()
                        
                        
                        break
                    num = tablero1.mapa.index(lista) - 1
                    print(num)
                    print(i)
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba = player1.items
                            player1.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            #main1.main()
                            
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            #main1.main()
                            
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            for x in tablero1.mapa:
                                print(x)
                            #main1.main()
                            
                            break
                            
                        
                    except:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                                
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                #main1.main()
                                
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                #main1.main()
                                
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                #main1.main()
                                
                                break
                                
                        except:
                            print("no deberia llegar aqui")
                            break        
                
            

zombiex = zombie("Zombie X",True,"Latigo")
zombiey = zombie("Zombie Y",True,"Espada")
zombiez = zombie("Zombie Z",True,"Pocion")
player1 = player("Player1",True,"Pistola")
player2 = player("Player2",True,"Cuchillo")
player3 = player("Player3",True,"Veneno")
tablero1 = tablero([["Base",player1.nombre,0,0,0,0,0,zombiex.nombre],
            ["Base",0,0,0,0,0,0,"SpawnPoint"],
            ["Base",player2.nombre,0,0,0,0,0,zombiey.nombre],
            ["Base",0,0,0,0,0,0,"Spawnpoint"],
            ["Base",player3.nombre,0,0,0,0,0,zombiez.nombre]])

for x in tablero1.mapa:
    print(x)
def upkey1(event):
    player1.mover(7)

def upkey2(event):
    player2.mover(8)
def upkey3(event):
    player3.mover(9)
def downkey1(event):
    player1.mover(4)
def downkey2(event):
    player2.mover(5)
def downkey3(event):
    player3.mover(6)
def leftkey1(event):
    player1.mover(10)
def leftkey2(event):
    player2.mover(11)
def leftkey3(event):
    player3.mover(12)
def rightkey1(event):
    player1.mover(1)
def rightkey2(event):
    player2.mover(2)
def rightkey3(event):
    player3.mover(3)
class main2():


    
    def main(self,num):
        print("main")
        
            
        """dir = int(input(("diga 1 para mover personaje1 hacia adelante,",
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
            player3.mover(dir)"""

    

    
        if num == 1:
            print("pretzel")
            ventana.bind("<Up>", upkey1)
            ventana.bind("<Down>", downkey1)
            ventana.bind("<Left>", leftkey1)
            ventana.bind("<Right>", rightkey1)
        if num == 2:
            ventana.bind("<Up>", upkey2)
            ventana.bind("<Down>", downkey2)
            ventana.bind("<Left>", leftkey2)
            ventana.bind("<Right>", rightkey2)
        if num == 3:
            ventana.bind("<Up>", upkey3)
            ventana.bind("<Down>", downkey3)
            ventana.bind("<Left>", leftkey3)
            ventana.bind("<Right>", rightkey3)
    

    def zzombie(self):
        zombiex.mover()
        zombiey.mover()
        zombiez.mover()

    def zzombieatq(self):
        zombiex.atacar()
        zombiey.y()
        zombiez.z()
    
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

def tablerogui(tab, tablero):
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                fontcolor = "black"
            if tablero[i][j] == "Player1":
                fontcolor = "cyan"
            if tablero[i][j] == "Player2":
                fontcolor = "cyan"
            if tablero[i][j] == "Player3":
                fontcolor = "cyan"
            if tablero[i][j] == "Zombie X":
                fontcolor = "deeppink"
            if tablero[i][j] == "Zombie X":
                fontcolor = "deeppink"
            if tablero[i][j] == "obstaculo":
                fontcolor = "red"
            else:
                fontcolor = "blue"

            b = Button(tab, text=tablero[i][j], fg=fontcolor, width=8, heigh=4, font="Arial")
            b.grid(row=i, column=j)

class ventanaJuego():
    def __init__(self,ventana):
        self.ventana = ventana
    def gui(self):
        
        moverp = Label(ventana, text="MOVER")
        moverp.place(x = 800,y = 0) 
        atqp = Label(ventana,text = "ATACAR")
        atqp.place(x = 850,y = 0)
        player1mover = Button(ventana, text="PLAYER1 m",
                        command=lambda: ventana.after(200, main1.main(1)))
        player1mover.place(x=800, y=20)
        player2mover = Button(ventana, text="PLAYER2 m",
                        command=lambda: ventana.after(200, main1.main(2)))
        player2mover.place(x=500, y=20)
        player3mover= Button(ventana, text="PLAYER3 m",
                        command=lambda: ventana.after(200, main1.main(3)))
        player3mover.place(x=300, y=20)






  
         

        

    

ventana = Tk()
ventana.geometry("1000x500") #dimensiones

ventana.config(bg="blue")  
gui = ventanaJuego(ventana)
gui.gui()   
tablerogui(ventana,tablero1.mapa)
main1 = main2()
#main1.main(1)
#main1.zzombie()
ventana.mainloop()