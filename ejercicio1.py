def ingreso_de_contrasena ():
    #1. Guarde la contraseña correcta en una variable 
    login = "*admin123*"

    # 2.Pida al usuario que ingrese una contraseña
    login_usuario = input("Ingrese su login ")

    # 3. Crear un ciclo para que le vuelva a preguntar al usuario si no ingresa la contraseña correcta       
    while login_usuario != login:
        print("Contraseña incorrecta, intente de nuevo. ")
        login_usuario = input("Ingrese su login: ")    
    
    #Si sale del ciclo, la contraseña es correcta
    print("¡Bienvenido a su correo! ")

ingreso_de_contrasena ()