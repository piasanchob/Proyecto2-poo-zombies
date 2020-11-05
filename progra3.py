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
tablero1 = tablero([["Base",player1.nombre,0,0,0,"Spawnpoint",0,0,zombiex.nombre],
            [0,0,0,0,0,0,0,"Zombie"],
            ["Base",player2.nombre,0,0,0,0,0,zombiey.nombre],
            [0,0,0,0,0,0,0,"Zombie"],
            [player3.nombre,0,0,0,0,0,0,zombiez.nombre]])

print(tablero1.mapa)
while True:
    dir = int(input(("diga 1 para mover personaje1 hacia adelante,/n"
            "2 para mover personaje2 hacia adelante/n",
            "3 para mover personaje3 hacia adelante")))
    if dir == 1:
        player1.mover(dir)
    if dir == 2:
        player2.mover(dir)
    if dir == 3:
        player3.mover(dir)
    dirz = (input(("diga x para mover zombie x hacia adelante,/n"
            "y para mover zombie y hacia adelante/n",
            "z para mover zombie z hacia adelante")))
    if dirz == "x":
        zombiex.mover(dirz)
    if dirz == "y":
        zombiey.mover(dirz)
    if dirz == "z":
        zombiez.mover(dirz)
