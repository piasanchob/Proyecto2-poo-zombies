class tablero():
    def __init__(self,mapa):
        self.mapa = mapa
        super().__init__(mapa)
    
class player(tablero):
    def __init__(self,arma,nombre,mapa,player,zombie):
        self.arma = arma
        self.nombre =  nombre
    
    def mover(self,tablero):
        
        print(2)
        dir = int(input(("diga 1 para mover personaje1 hacia adelante,"
        "2 para mover personaje2 hacia adelante",
        "3 para mover personaje3 hacia adelante")))
        
        if dir == 1:
            for x in mapa[0]:
                if x == player1.nombre:
                    nuevo = player1.nombre.index(mapa) + 1
                    viejo = player1.nombre.index(mapa)
                    mapa[viejo] == 0
                    mapa.insert(nuevo,player1.nombre)
                    print(mapa)
                    
        atq = input(("Diga 3 para que persoanje ataque, 4 para que zombie ataque"))
        print("mover")

    def atacar(self,tablero):
        print("atacar")
        
    
class zombie(tablero):
    def __init__(self,item):
        self.item = item
    def mover(self,tablero):
        print("mover")
        
    def atacar(self):
        
        print("atacar")


zombie1 = zombie("Pistola")
zombie2 = zombie("Medicina")
zombie3 = zombie("Pocion")
player1 = player("Cuchillo","Player1")
player2 = player("Escudo","Player2")
player3 = player("PocionCorazones","Player3")
tablero1 = tablero([[player1.nombre,0,0,0,"Spawnpoint",0,0,"Zombie"],
            [0,0,0,0,0,0,0,"Zombie"],
            ["Base",player2.nombre,0,0,0,0,0,"Zombie"],
            [0,0,0,0,0,0,0,"Zombie"],
            [player3.nombre,0,0,0,0,0,0,"Zombie"]],player,zombie)