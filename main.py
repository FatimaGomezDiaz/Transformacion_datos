import pandas as pd

alumnos= {"nombre":["Juan","Maria","Josue", "Selene"],
          "genero":["IN","F","M","F"],
          "escolaridad":["Universidad","Universidad","Prepa","Secundaria"]

        }

data= pd.DataFrame(alumnos)
data["nombre"] = data.nombre.str.strip().str.upper()
data["nom_min"] = data.nombre.str.lower()
data["nom_may"] = data.nombre.str.upper()
data["X"] = data.nombre.str.lower().str.replace("a","x")


#Transformacion de datos nominales
start_m= data.nombre.str.startswith("M")
#print(start_m)
#print(dta[start_m])

end_e = data.nombre.str.endwith("E")
#print(end_e)
#print(data[end_e])

contiene_a = data.nombre.str.contains("A")
#print(contiene_a)
#print(data[contiene_a])

print(data)

#Transformacion de datos nominales
one_hot_encoder= pd.get_dummies(data.genero)
print(one_hot_encoder)

data= data.join(one_hot_encoder)


