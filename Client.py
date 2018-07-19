import unirest
import json

def getStudents():
    response = unirest.get("http://localhost:4567/rest/estudiantes/", headers={"Accept":"application/json"})
    return response.raw_body


def studentConsult(x):
    response = unirest.get("http://localhost:4567/rest/estudiantes/{}".format(x), headers={"Accept":"application/json"})
    return response.raw_body


def createStudent(nombre, correo, carrera):
    response = unirest.post("http://localhost:4567/rest/estudiantes/", headers={"Content-Type":"application/json", "Accept":"application/json"}, params=json.dumps({"nombre": "{}".format(nombre),
                                                                                                                            "correo": "{}".format(correo),
                                                                                                                            "carrera": "{}".format(carrera)}))
    return response.raw_body

print "Bienvenido al cliente REST"

while True:
    print("\nOpciones disponibles:")
    print("1- Obtener el listado de estudiantes")
    print("2- Consultar Estudiantes")
    print("3- Crear un nuevo estudiente")
    print("4- Salir")

    opcion = raw_input("Elige una opcion:")

    if opcion == "1":
        print getStudents()
    elif opcion == "2":
        matricula = raw_input("Introduce la matricula:")
        print studentConsult(matricula)
    elif opcion == "3":
        print("Crear Estudiante")
        nombre = raw_input("Introduce nombre de estudiante:")
        correo = raw_input("Introduce el correo del estudienate:")
        carrera = raw_input("Introduce carrera del estudiante:")
        print createStudent(nombre, correo, carrera)
    elif opcion == "4":
        break