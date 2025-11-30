import qrcode

nombres1 = ["Lic_Juan_Ramon_y_fam", "Gloria_Shaul", "Ing_Andrea", "Ing_Rodolfo", "Lic_Gabriela"]
nombres2 = ["Maria_Elena_Shaul", "Sr_Leonardo", "Profe_Rolando", "Lic_Saul", "Inge_Rolando"]
nombres3 = ["Lic_Manolita", "Profa_Karla", "Sra_Marcela", "Profa_Eunice", "Ing_Ivan"]
nombres4 = ["Prof_Bernardo", "Anita_Perez", "Ing_Miguel", "Javier", "Julio"]
nombres5 = ["Prof_Roberto", "Sharon", "Ing_Mario", "Profa_Anita", "Rony"]
nombres6 = ["Ing_Carlos", "Scarleth", "Liliana", "Ing_Herman", "Profa_Magnolia"]
nombres7 = ["Lica_Dedy", "Lica_Evelyn", "Sra_Elena", "Ing_Jovany", "Ing_Hector", "Karla_Monroy"]


"""
for nombre in nombres1:
    print("https://juanpablodeleon.github.io/Invitaciones/"+nombre+".html")
"""

#for nombre in nombres:
#    print("./QRs\\"+nombre+".png")

#Modificar por el numero por cada lista
for nombre in nombres7:
    url ="https://juanpablodeleon.github.io/Invitaciones/"+nombre+".html"
    file_path = "./QRs\\qr"+nombre+".png"

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)

    print(url)
    print("Creado")



"""
nombr= "invitacion"
url ="https://juanpablodeleon.github.io/Invitaciones/"+nombr+".html"
#input("Enter URL: ").strip()
file_path = "./QRs\\qr"+nombr+".png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(url)
print("Creado")
"""