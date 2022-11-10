riosPrincipales = { "rios":{"Nilo","Amazonas","Magdalena","Mississippi","Yangtaze Kiang"}, "paises":{"Egipto","Latinoamerica","Colombia","Estados unidos","China"}}
#Primer punto
for i in riosPrincipales["paises"]:
    for a in riosPrincipales["rios"]:
        print(a + " Es un rio ubicado en " + i)
print("-----------------")
#SegundoPunto
for i in riosPrincipales["rios"]:
    print(i)
print("-------------------")
#Tercer punto
for i in riosPrincipales["paises"]:
    print(i)