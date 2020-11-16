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
        
        
        if dir == 1:
            for x in tablero1.mapa[0]:
                if x == player1.nombre:
                    
                    nuevo = tablero1.mapa[0].index(player1.nombre) + 1
                    viejo = tablero1.mapa[0].index(player1.nombre)
                    tablero1.mapa[0][viejo] = 0
                    tablero1.mapa[0][nuevo] = player1.nombre
                    print(tablero1.mapa)
                    break
        if dir == 2:
            for x in tablero1.mapa[2]:
                if x == player2.nombre:
                    
                    nuevo = tablero1.mapa[2].index(player2.nombre) + 1
                    viejo = tablero1.mapa[2].index(player2.nombre)
                    tablero1.mapa[2][viejo] = 0
                    tablero1.mapa[2][nuevo] = player2.nombre
                    print(tablero1.mapa)
                    break
        if dir == 3:
            for x in tablero1.mapa[4]:
                if x == player3.nombre:
                    
                    nuevo = tablero1.mapa[4].index(player3.nombre) + 1
                    viejo = tablero1.mapa[4].index(player3.nombre)
                    tablero1.mapa[4][viejo] = 0
                    tablero1.mapa[4][nuevo] = player3.nombre
                    print(tablero1.mapa)
                    break

                
        


                                viejo = lista.index(player3.nombre)
                                lista[viejo] = 0
                                
                                lista = tablero1.mapa[c-1]
                                lista[viejo] = player3.nombre
                                for x in tablero1.mapa:
                                    print(x)
                                m = False
                                
                                main1.main()
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
                        main1.main()
                        break
                        

    def atacar(self):
        atq = input(("Diga 1 para que persoanje1 ataque, 2 para que personaje2 ataque, 3 para que personaje3 ataque "))
        
        if atq == 1:
            for lista in tablero1.mapa:
                    for x in lista:
                        if x == player1.nombre:
                            
                            nuevo = lista.index(player1.nombre) + 1
                            if nuevo == zombiex.nombre: 
                                nuevo == zombiex.items
                                
        if atq ==2:
            pass
        if atq == 3:
            pass
        
    
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
                    if nuevo != "Base":
                        if nuevo != player1.nombre and nuevo != player2 and nuevo != player3.nombre:
                            if nuevo != "obstaculo":
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
                            print("invalido")
                    else:
                        print("ganaron los zombies")
                
                if x == zombiey.nombre:
                    nuevo = lista.index(zombiey.nombre) - 1
                    if nuevo != "Base":
                        if nuevo != player1.nombre and nuevo != player2 and nuevo != player3.nombre:
                            if nuevo != "obstaculo":
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
                            print("invalido")
                    else:
                        print("ganaron los zombies")
                
                if x == zombiez.nombre:
                    nuevo = lista.index(zombiez.nombre) - 1
                    if nuevo != "Base":
                        if nuevo != player1.nombre and nuevo != player2 and nuevo != player3.nombre:
                            if nuevo != "obstaculo":
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
        
        print("atacar")


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
