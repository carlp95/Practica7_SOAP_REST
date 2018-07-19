from zeep import Client

client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

op = ""
while op != "S":

    print("PYTHON - SOAP CLIENT\nElige que mostrar:\n")
    print("ET - Todos los estudiantes")
    print("A - Una asignatura")
    print("P - Un profesor")
    print("S - salir")

    op = input("Opcion elegida:").lower()

    if op == "et":
        print(client.service.getAllEstudiante())
    elif op == "a":
        print(client.service.getAsignatura(int(input("Id de la asignatura:"))))
    elif op == "p":
        print(client.service.getProfesor(int(input("Id del profesor:"))))

