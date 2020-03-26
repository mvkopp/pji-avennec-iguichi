from lxml import etree

def main():
    users = etree.Element("users")
    user = etree.SubElement(users, "user")
    user.set("data-id", "101")
    nom = etree.SubElement(user, "nom")
    nom.text = "imad"
    metier = etree.SubElement(user, "metier")
    metier.text = "Etudiant"
    fichier = open ("result.xml","w")
    fichier.write(etree.tostring(users, pretty_print=True))

if __name__ == "__main__" :
    main();
