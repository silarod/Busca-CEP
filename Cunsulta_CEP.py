import requests

def buscar_cep_por_rua():
    v_lagradouro = input("Digite o nome do Lagradouro:")
    v_cidade = input("Digite o nome da Cidade:")
    v_uf = input("Digite  UF: ")

    url = "https://viacep.com.br/ws/" + v_uf + "/" + v_cidade + "/" + v_lagradouro + "/json/"
    response = requests.get(url)

    while (response.status_code != 200):
        print("houve um erro!  Tente novamente!")

        v_lagradouro = input("Digite o valor do Lagradouro:")
        v_cidade = input("Digite o valor da Cidade:")
        v_uf = input("Digite de UF")

        url = "https://viacep.com.br/ws/" + v_uf + "/" + v_cidade + "/" + v_lagradouro + "/json/"
        response = requests.get(url)

    endereco = response.json()

    # laco de repecição na lista de dicionários
    print('\nEncontramos '+str(len(endereco))+' Resultado(s)\n')

    for i in range(0, len(endereco)):
        print(".::Resuldado - "+str(i+1)+"::.\n")
        for r in endereco[i]:
            print(r.upper(), ": ", endereco[i][r])
        print('\n\n')
        
def buscar_rua_por_cep():
  v_cep=input("Digite o valor do CEP:")
  url="http://viacep.com.br/ws/"+v_cep + "/json/"
  #print(url)
  response = requests.get(url)

  while (response.status_code!=200):
      print("Digite um CEP valido!")
      v_cep=input("Digite o valor do CEP:")
      url="http://viacep.com.br/ws/"+v_cep + "/json/"
      response = requests.get(url)
    
  endereco=response.json()
  rua=endereco['logradouro']
  print('Este CEP é correspondente a ' +rua+"\n")

  for i in endereco:
      print( i.upper(), ": ", endereco[i])


  funcao = int(input("Ola Tudo bom!\nEscolha umas das opções abaixo: \n\n  -Digite 1 para buscar CEP\n\n  -Digite 2 Para buscar RUA\n\n\n"))
  if funcao == 2:
    print("\n BUSCA DE LAGRADOURO\n_______________________\n")
    buscar_cep_por_rua()
  else:
    print("\n BUSCA DE CEP
    \n_______________________\n")
    buscar_rua_por_cep()

    
