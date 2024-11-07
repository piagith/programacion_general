# Dos equipos de futbol están disputando 
# el saque inicial del juego. 
# Los capitanes de cada equipo deciden
#  jugar el clásico juego "Piedra, papel o tijera"
#  para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a 
# Tijera, Tijera vence a Papel y Papel vence a
#  Piedra.
# Juegan una sola vez.



jugador1=input("jugador 1, elija Piedra, Papel o Tijera: ")
jugador2=input("jugador 2, elija Piedra, Papel o Tijera: ")



def jugar (jugador1: str, jugador2: str) -> str:
    mensaje = ""
    if jugador1==jugador2:
        mensaje = "empate"
    elif (jugador1=="Piedra" and jugador2=="Tijera") or (jugador1=="Tijera" and jugador2=="Papel") or (jugador1 == "Papel" and jugador2 == "Piedra"):
         ("gana el jugador 1")
         mensaje = "gana el jugador 1"
    else: 
        mensaje = "gana el jugador 2"
        
        return mensaje 
    
jugar(jugador1, jugador2)
