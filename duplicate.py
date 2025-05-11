import shutil
import os
import json
import subprocess

print("Este programa duplica a app base (my-app) e insere o teu website na pasta 'src' da nova app.")
print("Certifica-te de que a tua pasta tem o ficheiro index.html e só subpastas para css, js ou imagens.")
print("⚠️ Nota: Se existir um ficheiro 'index.js' no teu site, vais poder manter e renomear o da app base.")

# Inputs
nomePastaNova = input("Nome da nova app (nome da duplicação da my-app): ").strip()
pastaDoWebsite = input("Nome da pasta do teu website (a copiar para dentro da src): ").strip()

# Caminhos
pasta_original = 'my-app'
pasta_duplicada = nomePastaNova
destino_src = os.path.join(pasta_duplicada, 'src')
caminho_package_json = os.path.join(pasta_duplicada, 'package.json')
index_js_app_base = os.path.join(destino_src, 'index.js')

# Verificar se a pasta base existe
if not os.path.exists(pasta_original):
    print(f"Erro: A pasta base '{pasta_original}' não existe.")
    exit()

# Duplicar a pasta my-app
if os.path.exists(pasta_duplicada):
    print(f"A pasta '{pasta_duplicada}' já existe.")
    resposta = input("Queres sobrescrevê-la? (s/n): ").strip().lower()
    if resposta == 's':
        shutil.rmtree(pasta_duplicada)
    else:
        print("Operação cancelada.")
        exit()

shutil.copytree(pasta_original, pasta_duplicada)
print(f"Pasta '{pasta_original}' duplicada como '{pasta_duplicada}'.")

# Verificar se a pasta do website existe
if not os.path.exists(pastaDoWebsite):
    print(f"Erro: A pasta do website '{pastaDoWebsite}' não existe.")
    shutil.rmtree(pasta_duplicada)
    exit()

# Procurar por 'index.js' no website do utilizador
index_js_encontrado = None
for root, dirs, files in os.walk(pastaDoWebsite):
    for file in files:
        if file.lower() == 'index.js':
            index_js_encontrado = os.path.join(root, file)
            break
    if index_js_encontrado:
        break

# Se existir index.js no site do utilizador, perguntar se quer renomear o da app base
novo_nome = None
if index_js_encontrado and os.path.exists(index_js_app_base):
    print(f"⚠️ O teu website contém um ficheiro 'index.js'.")
    print(f"Para evitar conflito com o 'index.js' da app base, este último vai ter de ser renomeado.")
    resposta = input("Queres mudar o nome do ficheiro da app base? (s/n): ").strip().lower()
    if resposta != 's':
        print("Operação cancelada.")
        shutil.rmtree(pasta_duplicada)
        exit()
    novo_nome = input("Novo nome para o ficheiro da app base (sem .js): ").strip()

    # Renomear o index.js da app base
    novo_path = os.path.join(destino_src, f"{novo_nome}.js")
    os.rename(index_js_app_base, novo_path)

    # Atualizar package.json
    if os.path.exists(caminho_package_json):
        try:
            with open(caminho_package_json, 'r', encoding='utf-8') as f:
                package_data = json.load(f)

            if "main" in package_data and package_data["main"] == "src/index.js":
                package_data["main"] = f"src/{novo_nome}.js"
                with open(caminho_package_json, 'w', encoding='utf-8') as f:
                    json.dump(package_data, f, indent=2)
                print(f"📝 package.json atualizado: main -> src/{novo_nome}.js")
            else:
                print("⚠️ Campo 'main' não encontrado ou já foi modificado.")
        except Exception as e:
            print(f"Erro ao atualizar package.json: {e}")

# Copiar conteúdo da pasta do website para dentro de src
for root, dirs, files in os.walk(pastaDoWebsite):
    rel_path = os.path.relpath(root, pastaDoWebsite)
    destino_atual = os.path.join(destino_src, rel_path) if rel_path != '.' else destino_src
    os.makedirs(destino_atual, exist_ok=True)

    for file in files:
        origem = os.path.join(root, file)
        destino_final = os.path.join(destino_atual, file)
        shutil.copy2(origem, destino_final)

print(f"✅ Conteúdo da pasta '{pastaDoWebsite}' copiado com sucesso para '{destino_src}'.")
print("\n⚠️ Para correr a aplicação é só mudar para a diretoria do projeto novo criado e correr 'npm start', precisas de ter o Node.js e o npm instalados no sistema.")
