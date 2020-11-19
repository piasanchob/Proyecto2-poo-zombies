import random
from tkinter import *
from tkinter import messagebox

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
                                if lista[nuevo] != zombiex.nombre and lista[nuevo] != zombiey.nombre and lista[nuevo] != zombiez.nombre:
                                    if lista[nuevo] != "obstaculo":
                                        viejo = lista.index(player1.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player1.nombre
                                        tablerogui(ventana,tablero1.mapa)
                                        
                                        for x in tablero1.mapa:
                                            print(x)
                                        if player2.vida == False and player3.vida == False:
                                            main1.zzombie()
                                            break
                                        
                                        cont += 1
                                        break
                                    else:
                                        messagebox.showinfo(message = "invalido",title = ".")
                                        
                                else:
                                    messagebox.showinfo(message = "invalido",title = ".")
                            else:
                                messagebox.showinfo(message = "invalido",title = ".")
            if dir == 2:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player2.nombre:
                            
                            nuevo = lista.index(player2.nombre) + 1
                            if nuevo != 8:
                                if lista[nuevo] != zombiex.nombre and lista[nuevo]!= zombiey.nombre and lista[nuevo] != zombiez.nombre:
                                    #if lista[nuevo] != "obstaculo":
                                        viejo = lista.index(player2.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player2.nombre
                                        for x in tablero1.mapa:
                                            print(x)
                                        tablerogui(ventana,tablero1.mapa)
                                        cont += 1
                                        if player3.vida == False:
                                            main1.zzombie()
                                            break
                                        
                                        
                                        break
                                    #else:
                                        #print("invalido")
                                else:
                                    messagebox.showinfo(message = "invalido",title = ".")
                            else:
                                messagebox.showinfo(message = "invalido",title = ".")
            if dir == 3:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            
                            nuevo = lista.index(player3.nombre) + 2
                            if nuevo != 8:
                                if lista[nuevo] != zombiex.nombre and lista[nuevo] != zombiey.nombre and lista[nuevo] != zombiez.nombre:
                                    
                                    if lista[nuevo] != "obstaculo":
                                        viejo = lista.index(player3.nombre)
                                        lista[viejo] = 0
                                        lista[nuevo] = player3.nombre
                                        for x in tablero1.mapa:
                                            print(x)
                                        cont += 1
                                        tablerogui(ventana,tablero1.mapa)
                                        main1.zzombie()
                                        break
                                        
                                    
                                    else:
                                        messagebox.showinfo(message = "invalido",title = ".")
                                else:
                                    messagebox.showinfo(message = "invalido",title = ".")

                            else:
                                messagebox.showinfo(message = "invalido",title = ".")

            if dir == 4:
               pinto = True
               m = True
               while m:
                    for lista in tablero1.mapa:
                        if not pinto:
                            break
                        else:
                            for x in lista:
                                if x == player1.nombre:
                                    c = tablero1.mapa.index(lista)
                                    #print(c)
                                    #if c == 4:
                                        #print("invalido")
                                        #break
                                        
                                    if tablero1.mapa[c] == lista:

                                        
                                        viejo = lista.index(player1.nombre)
                                        if tablero1.mapa[c + 1][viejo] != "obstaculo":
                                            if tablero1.mapa[c + 1][viejo] != zombiex.nombre and tablero1.mapa[c + 1][viejo] != zombiey.nombre and tablero1.mapa[c + 1][viejo] != zombiez.nombre:
                                            

                                                lista[viejo] = 0
                                                print(c)
                                                if c == 4:
                                                    c = -1
                                                #main1.main()
                                                
                                                lista = tablero1.mapa[c+1]
                                                lista[viejo] = player1.nombre
                                                for x in tablero1.mapa:
                                                    print(x)
                                                tablerogui(ventana,tablero1.mapa)
                                                cont += 1
                                                pinto = False
                                                m = False
                                                
                                                
                                                
                                                if player2.vida == False and player3.vida == False:
                                                    main1.zzombie()
                                                    break
                                            else: 
                                                messagebox.showinfo(message = "invalido",title = ".")
                                                break
                                        else:
                                            messagebox.showinfo(message = "invalido",title = ".")
                                            break

                                        
            if dir == 5:
                pinto = True
                m = True
                while m:
                    for lista in tablero1.mapa:
                        if not pinto:
                            break
                        else:
                            for x in lista:
                                if x == player2.nombre:
                                    c = tablero1.mapa.index(lista)
                                    print(c)
                                    
                                    
                                    if tablero1.mapa[c] == lista:


                                        viejo = lista.index(player2.nombre)
                                        if tablero1.mapa[c + 1][viejo] != zombiex.nombre and tablero1.mapa[c + 1][viejo] != zombiey.nombre and tablero1.mapa[c + 1][viejo] != zombiez.nombre:
                                            lista[viejo] = 0
                                            if c == 4:
                                                c = -1
                                            #main1.main()
                                            
                                            
                                            lista = tablero1.mapa[c+1]
                                            lista[viejo] = player2.nombre
                                            for x in tablero1.mapa:
                                                print(x)
                                            tablerogui(ventana,tablero1.mapa)
                                            cont += 1
                                            m = False
                                            pinto = False

                                            #break
                                            
                                            
                                            
                                            if player3.vida == False:
                                                main1.zzombie()
                                                break
                                        else:
                                            messagebox.showinfo(message = "invalido",title = ".")
                                        
                                        
                                

            if dir == 6:
               pinto = True
               m = True
               while m:
                    for lista in tablero1.mapa:
                        if not pinto:
                            for x in lista:
                                if x == player3.nombre:
                                    c = tablero1.mapa.index(lista)
                                    print(c)
                                    #if c == 4:
                                        #c = -1
                                        #main1.main()
                                        #break
                                    
                                    if tablero1.mapa[c] == lista:


                                        viejo = lista.index(player3.nombre)
                                        if tablero1.mapa[c + 1][viejo] != "obstaculo":
                                            if tablero1.mapa[c + 1][viejo] != zombiex.nombre and tablero1.mapa[c + 1][viejo] != zombiey.nombre and tablero1.mapa[c + 1][viejo] != zombiez.nombre:
                                            
                                                lista[viejo] = 0
                                                if c == 3:
                                                    c = -1
                                                lista = tablero1.mapa[c+2]
                                                lista[viejo] = player3.nombre
                                                for x in tablero1.mapa:
                                                    print(x)
                                                tablerogui(ventana,tablero1.mapa)
                                                cont += 1
                                                m = False
                                                pinto = False
                                                
                                                
                                                
                                                main1.zzombie()
                                                break
                                            else:
                                                messagebox.showinfo(message = "invalido",title = ".")
                                        else:
                                            messagebox.showinfo(message = "invalido",title = ".")

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
                                    if tablero1.mapa[c - 1][viejo] != "obstaculo":
                                        if tablero1.mapa[c - 1][viejo] != zombiex.nombre and tablero1.mapa[c - 1][viejo] != zombiey.nombre and tablero1.mapa[c - 1][viejo] != zombiez.nombre:
                                            
                                            lista[viejo] = 0
                                            
                                            lista = tablero1.mapa[c-1]
                                            lista[viejo] = player1.nombre
                                            for x in tablero1.mapa:
                                                print(x)
                                            tablerogui(ventana,tablero1.mapa)
                                            cont += 1
                                            m = False

                                            
                                            if player2.vida == False and player3.vida == False:
                                                main1.zzombie()
                                                break
                                        else:
                                            messagebox.showinfo(message = "invalido",title = ".")
                                            break
                                    else:
                                        messagebox.showinfo(message = "invalido",title = ".")
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
                                    if tablero1.mapa[c - 1][viejo] != zombiex.nombre and tablero1.mapa[c -1][viejo] != zombiey.nombre and tablero1.mapa[c - 1][viejo] != zombiez.nombre:
                                         
                                        lista[viejo] = 0
                                        
                                        lista = tablero1.mapa[c-1]
                                        lista[viejo] = player2.nombre
                                        for x in tablero1.mapa:
                                            print(x)
                                        tablerogui(ventana,tablero1.mapa)
                                        cont += 1
                                        m = False
                                        
                                        if player3.vida == False:
                                            main1.zzombie()
                                            break
                                    else:
                                        messagebox.showinfo(message = "invalido",title = ".")    

            
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

                                    if tablero1.mapa[c - 1][viejo] != "obstaculo":
                                        if tablero1.mapa[c - 1][viejo] != zombiex.nombre and tablero1.mapa[c - 1][viejo] != zombiey.nombre and tablero1.mapa[c - 1][viejo] != zombiez.nombre:
                                        
                                            
                                            lista[viejo] = 0
                                            
                                            lista = tablero1.mapa[c-1]
                                            lista[viejo] = player3.nombre
                                            for x in tablero1.mapa:
                                                print(x)
                                            tablerogui(ventana,tablero1.mapa)
                                            cont += 1
                                            m = False
                                            
                                            main1.zzombie()
                                            break
                                        else:
                                            messagebox.showinfo(message = "invalido",title = ".")
                                    else:
                                        messagebox.showinfo(message = "invalido",title = ".")
            if dir == 10:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player1.nombre:
                            if lista.index(player1.nombre) == 1:
                                messagebox.showinfo(message = "invalido",title = ".")
                                break
                            nuevo = lista.index(player1.nombre) - 1
                            
                            viejo = lista.index(player1.nombre)
                            if lista[nuevo] != zombiex.nombre and lista[nuevo] != zombiey.nombre and lista[nuevo] != zombiez.nombre:
                                    
                                if lista[nuevo] != "obstaculo":
                                    lista[viejo] = 0
                                    lista[nuevo] = player1.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    if player2.vida == False and player3.vida == False:
                                        main1.zzombie()
                                        break
                                else:
                                    messagebox.showinfo(message = "invalid")

                            else:
                                messagebox.showinfo(message = "invalid")

                                
            if dir == 11:
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player2.nombre:
                            if lista.index(player2.nombre) == 1:
                                messagebox.showinfo(message = "invalid")
                            nuevo = lista.index(player2.nombre) - 1
                            
                            viejo = lista.index(player2.nombre)
                            if lista[nuevo] != zombiex.nombre and lista[nuevo] != zombiey.nombre and lista[nuevo] != zombiez.nombre:
                             
                                lista[viejo] = 0
                                lista[nuevo] = player2.nombre
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                cont += 1
                                if player3.vida == False:
                                    main1.zzombie()
                                    break
                            else:
                                messagebox.showinfo(message = "invalid")

            if dir == 12:
                
                for lista in tablero1.mapa:
                    for x in lista:
                        if x == player3.nombre:
                            if lista.index(player3.nombre) == 1:
                                messagebox.showinfo(message = "invalid")
                                #main1.main()
                                break
                            nuevo = lista.index(player3.nombre) - 1
                            
                            viejo = lista.index(player3.nombre)
                            if lista[nuevo] != zombiex.nombre and lista[nuevo] != zombiey.nombre and lista[nuevo] != zombiez.nombre:
                                    
                                if lista[nuevo] != "obstaculo":
                                    lista[viejo] = 0
                                    lista[nuevo] = player3.nombre
                                    for x in tablero1.mapa:
                                        print(x)
                                    tablerogui(ventana,tablero1.mapa)
                                    cont += 1
                                    main1.zzombie()
                                    break
                                else:
                                    messagebox.showinfo(message = "invalid")



                            else:
                                 messagebox.showinfo(message = "invalid")



    def atacar(self,atq):
        
        
        if atq == 1:
            atk = True
            for lista in tablero1.mapa:
                if not atk:
                    break
                else:
                    for x in lista:
                        if x == player1.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player1.nombre) + 1
                            atras = lista.index(player1.nombre) - 1
                            print("entro")
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break

                            if lista[nuevo] == zombiey.nombre: 
                                lista[nuevo] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            
                            num = tablero1.mapa.index(lista) - 1
                            print("atq")
                            
                            try:
                                arriba = tablero1.mapa[num][i]
                                if arriba == zombiex.nombre: 
                                    arriba = zombiex.items
                                    zombiex.vida = False
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                    break
                                if arriba == zombiey.nombre: 
                                    arriba = zombiey.items
                                    zombiey.vida = False
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                    break
                                if arriba == zombiez.nombre: 
                                    arriba = zombiez.items
                                    zombiez.vida = False
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                    break
                            
                            
                            except IndexError:

                                try:
                                    num2 = tablero1.mapa.index(lista) + 1
                                    
                                    abajo = tablero1.mapa[num2][i]
                                    if abajo == zombiex.nombre: 
                                        abajo = zombiex.items
                                        zombiex.vida = False
                                        tablerogui(ventana,tablero1.mapa)
                                        atk = False
                                    if abajo == zombiey.nombre: 
                                        abajo = zombiey.items
                                        zombiey.vida = False
                                        tablerogui(ventana,tablero1.mapa)
                                        atk = False
                                    if abajo == zombiez.nombre: 
                                        abajo = zombiez.items
                                        zombiex.vida = False
                                        tablerogui(ventana,tablero1.mapa)
                                        atk = False
                                    break
                                except IndexError:
                                    print("no deberia llegar aqui")
                                    atk = False
                                    break        
                    
                    if player2.vida == False and player3.vida == False:
                        main1.zzombie()
                            

                                
        if atq ==2:
            atk = True
            for lista in tablero1.mapa:
                if not atk:
                    break
                else:
                    for x in lista:
                        if x == player2.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player2.nombre) + 1
                            atras = lista.index(player2.nombre) - 1
                            
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[nuevo] == zombiey.nombre: 
                                
                                lista[nuevo] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            num = tablero1.mapa.index(lista) - 1
                            
                            try:
                                
                                arriba = tablero1.mapa[num][i]
                                #rint(arriba)
                                if arriba == zombiex.nombre: 
                                    arriba = zombiex.items
                                    zombiex.vida = False
                                    tablero1.mapa[num][i] = "Latigo"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                print(arriba)
                                if arriba == zombiey.nombre: 
                                    arriba = zombiey.items
                                    tablero1.mapa[num][i] = "Espada"
                                    print("cambio")
                                    print(zombiey.items)
                                    zombiey.vida = False
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if arriba == zombiez.nombre: 
                                    arriba = zombiez.items
                                    zombiez.vida = False
                                    tablero1.mapa[num][i] = "Pocion"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                
                                break
                            except IndexError:
                                
                                num2 = tablero1.mapa.index(lista) + 1
                                
                                abajo = tablero1.mapa[num2][i]
                                if abajo == zombiex.nombre: 
                                    abajo = zombiex.items
                                    zombiex.vida = False
                                    tablero1.mapa[num][i] = "Latigo"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if abajo == zombiey.nombre: 
                                    abajo = zombiey.items
                                    zombiey.vida = False
                                    tablero1.mapa[num][i] = "Espada"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if abajo == zombiez.nombre: 
                                    abajo = zombiez.items
                                    zombiez.vida = False
                                    tablero1.mapa[num][i] = "Pocion"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                break
                                
                    if player3.vida == False:
                        main1.zzombie()


        if atq == 3:
            atk = True
            for lista in tablero1.mapa:
                if not atk:
                    break
                else:
                    for x in lista:
                        if x == player3.nombre:
                            aux = lista
                            i = lista.index(x)
                            nuevo = lista.index(player3.nombre) + 1
                            atras = lista.index(player3.nombre) - 1
                            
                            if lista[nuevo] == zombiex.nombre: 
                                lista[nuevo] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[nuevo] == zombiey.nombre: 
                                lista[nuevo] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[nuevo] == zombiez.nombre: 
                                lista[nuevo] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break

                            if lista[atras] == zombiex.nombre: 
                                lista[atras] = zombiex.items
                                zombiex.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiey.nombre: 
                                lista[atras] = zombiey.items
                                zombiey.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            if lista[atras] == zombiez.nombre: 
                                lista[atras] = zombiez.items
                                zombiez.vida = False
                                tablerogui(ventana,tablero1.mapa)
                                atk = False
                                break
                            num = tablero1.mapa.index(lista) - 1
                            print(num)
                            print(i)
                            try:
                                arriba = tablero1.mapa[num][i]
                                if arriba == zombiex.nombre: 
                                    arriba = zombiex.items
                                    zombiex.vida = False
                                    tablero1.mapa[num][i] = "Latigo"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if arriba == zombiey.nombre: 
                                    arriba = zombiey.items
                                    zombiey.vida = False
                                    tablero1.mapa[num][i] = "Espada"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if arriba == zombiez.nombre: 
                                    arriba = zombiez.items
                                    zombiez.vida = False
                                    tablero1.mapa[num][i] = "Pocion"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                
                                break
                            except IndexError:
                                
                                num2 = tablero1.mapa.index(lista) + 1
                                
                                abajo = tablero1.mapa[num2][i]
                                if abajo == zombiex.nombre: 
                                    abajo = zombiex.items
                                    zombiex.vida = False
                                    tablero1.mapa[num][i] = "Latigo"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if abajo == zombiey.nombre: 
                                    abajo = zombiey.items
                                    zombiey.vida = False
                                    tablero1.mapa[num][i] = "Espada"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                if abajo == zombiez.nombre: 
                                    abajo = zombiez.items
                                    zombiez.vida = False
                                    tablero1.mapa[num][i] = "Pocion"
                                    tablerogui(ventana,tablero1.mapa)
                                    atk = False
                                break
                                    
                    main1.zzombie()

                            

        
    
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
                            
                            main1.zzombieatq()
                            break
                        if lista[nuevo] == "obstaculo":
                            print("Invalido")

                        if lista[nuevo] == 0:
                            viejo = lista.index(zombiex.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = zombiex.nombre
                                    
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            #zombiey.mover()
                            
                            continue
                            #break                            
                        else: 
                            messagebox.showinfo(message = "invalido")
                            #break
                        
                    else:
                        #print("zombiex")
                        messagebox.showinfo(message = "ganaron los zombies")
                        break
    def ymover(self): 
        for lista in tablero1.mapa:
            for x in lista:           
                if x == zombiey.nombre:
                    nuevo = lista.index(zombiey.nombre) - 1
                    if lista[nuevo] != "Base":
                        if lista[nuevo] == player1.nombre or lista[nuevo] == player2.nombre or lista[nuevo]== player3.nombre:
                            main1.zzombieatq()
                            break
                        if lista[nuevo] == "obstaculo":
                            messagebox.showinfo(message = "invalido")
                        if lista[nuevo] == 0:
                            viejo = lista.index(zombiey.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = zombiey.nombre
                                    
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            #zombiey.mover()
                            
                            
                            break
                            
                        else: 
                            messagebox.showinfo(message = "invalido")
                            #break
                        
                    else:
                        messagebox.showinfo(message = "ganaron los zombies")
                        break
    def zmover(self):
        for lista in tablero1.mapa:
            for x in lista:            
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
                                tablerogui(ventana,tablero1.mapa)
                                #zombiey.mover()
                                
                                #main1.main()
                                break
                            else: 
                                messagebox.showinfo(message = "invalido")
                                #break
                    else:
                        messagebox.showinfo(message = "ganaron los zombies")
                        break
               

            
        
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
                        tablerogui(ventana,tablero1.mapa)
                        break
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                    num = tablero1.mapa.index(lista) - 1
                    
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba = player1.items
                            player1.vida = False
                            tablero1.mapa[num][i] = "Pistola"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            tablero1.mapa[num][i] = "Cuchillo"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            tablero1.mapa[num][i] = "Veneno"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                        
                        
                    except IndexError:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                            
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                tablero1.mapa[num][i] = "Pistola"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                tablero1.mapa[num][i] = "Cuchillo"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                tablero1.mapa[num][i] = "Veneno"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
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
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                        
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        break
                        
                    num = tablero1.mapa.index(lista) - 1
                    print(num)
                    print(i)
                    try:
                        arriba = tablero1.mapa[num][i]
                        if arriba == player1.nombre: 
                            arriba = player1.items
                            player1.vida = False
                            tablero1.mapa[num][i] = "Pistola"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            tablero1.mapa[num][i] = "Cuchillo"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            tablero1.mapa[num][i] = "Veneno"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            break
                            
                        
                    except IndexError:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                                
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
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
                        tablerogui(ventana,tablero1.mapa)
                        #main1.main()
                        break
                    if lista[nuevo] == player2.nombre: 
                        lista[nuevo] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        #main1.main()
                        break
                    if lista[nuevo] == player3.nombre: 
                        lista[nuevo] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        
                        
                        #main1.main()
                        break

                    if lista[atras] == player1.nombre: 
                        lista[atras] = player1.items
                        player1.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        #main1.main()
                        
                        break
                    if lista[atras] == player2.nombre: 
                        lista[atras] = player2.items
                        player2.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
                        #main1.main()
                        
                        break
                    if lista[atras] == player3.nombre: 
                        lista[atras] = player3.items
                        player3.vida = False
                        for x in tablero1.mapa:
                            print(x)
                        tablerogui(ventana,tablero1.mapa)
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
                            tablero1.mapa[num][i] = "Pistola"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            #main1.main()
                            
                            break
                        if arriba == player2.nombre: 
                            arriba = player2.items
                            player2.vida = False
                            tablero1.mapa[num][i] = "Cuchillo"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            #main1.main()
                            
                            break
                        if arriba == player3.nombre: 
                            arriba = player3.items
                            player3.vida = False
                            tablero1.mapa[num][i] = "Veneno"
                            for x in tablero1.mapa:
                                print(x)
                            tablerogui(ventana,tablero1.mapa)
                            #main1.main()
                            
                            break
                            
                        
                    except IndexError:
                        try:
                            num2 = tablero1.mapa.index(lista) + 1
                                
                            abajo = tablero1.mapa[num2][i]
                            if abajo == player1.nombre: 
                                abajo = player1.items
                                player1.vida = False
                                tablero1.mapa[num][i] = "Pistola"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                #main1.main()
                                
                                break
                            if abajo == player2.nombre: 
                                abajo = player2.items
                                player2.vida = False
                                tablero1.mapa[num][i] = "Cuchillo"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
                                #main1.main()
                                
                                break
                            if abajo == player3.nombre: 
                                abajo = player3.items
                                player3.vida = False
                                tablero1.mapa[num][i] = "Veneno"
                                for x in tablero1.mapa:
                                    print(x)
                                tablerogui(ventana,tablero1.mapa)
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
            ["Base",0,"obstaculo",0,0,0,0,"SpawnPoint"],
            ["Base",player2.nombre,0,0,0,0,0,zombiey.nombre],
            ["Base",0,"obstaculo",0,0,0,0,"Spawnpoint"],
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

        for lista in tablero1.mapa:
                if player1.vida == False:
                    if player2.vida == False:
                        if player3.vida == False:
                            messagebox.showinfo(message = "ganaron los zombies")
                            break
        for lista in tablero1.mapa:
                if zombiex.vida == False:
                    if zombiey.vida == False:
                        if zombiez.vida == False:
                            messagebox.showinfo(message = "ganaron los jugadores")
                            break

    
        if num == 1:
            
            
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
        zombiey.ymover()
        zombiez.zmover()

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
        moverp.place(x = 760,y = 0) 
        atqp = Label(ventana,text = "ATACAR")
        atqp.place(x = 850,y = 0)
        player1mover = Button(ventana, text="PLAYER1 m",
                        command=lambda: ventana.after(200, main1.main(1)))
        player1mover.place(x=760, y=20)
        player2mover = Button(ventana, text="PLAYER2 m",
                        command=lambda: ventana.after(200, main1.main(2)))
        player2mover.place(x=760, y=40)
        player3mover= Button(ventana, text="PLAYER3 m",
                        command=lambda: ventana.after(200, main1.main(3)))
        player3mover.place(x=760, y=60)

        player1atq = Button(ventana, text="PLAYER1 a",
                        command=lambda: ventana.after(200, player1.atacar(1)))
        player1atq.place(x=850, y=20)
        player2atq = Button(ventana, text="PLAYER2 a",
                        command=lambda: ventana.after(200, player2.atacar(2)))
        player2atq.place(x=850, y=40)
        player3atq = Button(ventana, text="PLAYER3 a",
                        command=lambda: ventana.after(200, player3.atacar(3)))
        player3atq.place(x=850, y=60)




"""def jugvivos():
    vivos = 0
    for i in players:
        if i.vida == True:
            vivos+=1

    return vivos

if jugadas == muertos:
    main1.zzombie()"""

  
         

        

    

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