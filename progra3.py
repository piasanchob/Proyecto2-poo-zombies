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
        
        
        if dir == 1:
            for lista in tablero1.mapa:
                for x in lista:
                    if x == player1.nombre:
                        
                        nuevo = lista.index(player1.nombre) + 1
                        if nuevo != 8:
                            viejo = lista.index(player1.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player1.nombre
                            
                            for x in tablero1.mapa:
                                print(x)
                            main1.main()
                            break
                        else:
                            print("invalido")
        if dir == 2:
            for lista in tablero1.mapa:
                for x in lista:
                    if x == player2.nombre:
                        
                        nuevo = lista.index(player2.nombre) + 1
                        if nuevo != 8:
                            viejo = lista.index(player2.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player2.nombre
                            for x in tablero1.mapa:
                                print(x)
                            main1.main()
                            break
                        else:
                            print("invalido")
        if dir == 3:
            for lista in tablero1.mapa:
                for x in lista:
                    if x == player3.nombre:
                        
                        nuevo = lista.index(player3.nombre) + 1
                        if nuevo != 8:
                            viejo = lista.index(player3.nombre)
                            lista[viejo] = 0
                            lista[nuevo] = player3.nombre
                            for x in tablero1.mapa:
                                print(x)
                            main1.main()
                            break
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
                                m = False
                                
                                main1.main()
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
        atq = input(("Diga 3 para que persoanje ataque, 4 para que zombie ataque"))
        print("atacar")
        
    
class zombie(tablero,peon):
    def __init__(self,nombre,vida,items):
        self.nombre = nombre
        self.vida = vida
        self.items = items
        
    def mover(self,dirz):
        print("mover")
        if dirz == "x":
            for x in tablero1.mapa[0]:
                if x == zombiex.nombre:
                    
                    nuevo = tablero1.mapa[0].index(zombiex.nombre) - 1
                    viejo = tablero1.mapa[0].index(zombiex.nombre)
                    tablero1.mapa[0][viejo] = 0
                    tablero1.mapa[0][nuevo] = zombiex.nombre
                    print(tablero1.mapa)
                    break
        if dirz == "y":
            for x in tablero1.mapa[2]:
                if x == zombiey.nombre:
                    
                    nuevo = tablero1.mapa[2].index(zombiey.nombre) - 1
                    viejo = tablero1.mapa[2].index(zombiey.nombre)
                    tablero1.mapa[2][viejo] = 0
                    tablero1.mapa[2][nuevo] = zombiey.nombre
                    print(tablero1.mapa)
                    break
        if dirz == "z":
            for x in tablero1.mapa[4]:
                if x == zombiez.nombre:
                    
                    nuevo = tablero1.mapa[4].index(zombiez.nombre) - 1
                    viejo = tablero1.mapa[4].index(zombiez.nombre)
                    tablero1.mapa[4][viejo] = 0
                    tablero1.mapa[4][nuevo] = zombiez.nombre
                    print(tablero1.mapa)
                    break

        
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
main1 = main()
main1.main()