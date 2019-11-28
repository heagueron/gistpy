ans=True
while ans:
    print ("""
    1. Calculo de Sueldo
    2. Ordenar Lista
    3. Nombres con Menos Vocales
    4. Cambiar Numeros de Documentos
    5. Aplicacion Particular
    6. Salir
    """)
    ans=input("Ingrese una opcion: ") 
    if ans=="1": 
      print("\n Calcular Sueldo") 
    elif ans=="2":
      print("\n Ordenar Lista") 
    elif ans=="3":
      print("\n Nombres con Menos Vocales")
    elif ans=="4":
      print("\n Cambiar Numeros de Documentos")
    elif ans=="5":
      print("\n Aplicacion Particular") 
    elif ans=="6":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 