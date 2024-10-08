usuarios =["Erica", "Diana", "Ben", "Lucas", "Matheus", "Simone"]
senhas = ["2202","2910","0710","2707","0*566","0,77"]
usuario = input("informe o nome de acesso: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        resp = "Usuário encontrado"
    break
else:
    resp = "Usuário não encontrado"
print(resp)
    

