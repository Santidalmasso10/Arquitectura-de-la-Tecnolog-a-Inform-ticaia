contra="12345"
entrada=""
intentos=0

while entrada!=contra and intentos < 3:
    entrada=input("ingrese su contraseña: ")
    if entrada != contra:
        print("inconrrecta siga intentando")
        intentos +=1
    if entrada == contra:
        print("correcto!!!")
    else:
        print("no hay mas intentos.")
        
