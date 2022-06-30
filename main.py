# - Modulo necessário para realizar as operações de CRUD no mongodb.
import pymongo	   							  # pip install pymongo

# Função - CREATE.
def fCreate():
	nome = input('Insira o nome: ')
	departamento = input('Informe o departamento: ')
	empresa = input('Informe a empresa: ')
	documento = {'nome':f'{nome}','departamento':f'{departamento}','empresa':f'{empresa}'}
	collection.insert_one(documento)
	fContinuar()

# Função - READ.
def fRead():
	nome = input('Informe o nome do funcionario: ')
	print(collection.find_one({'nome':f'{nome}'}))
	fContinuar()

# Função - UPDATE.
def fUpdate():
	print('Qual atributo deseja atualizar?\n1 - nome.\n2 - departamento.\n3 - empresa.\n')
	escolha = input('Digite o numero da opcao: ')

	if escolha == '1':
		oldNome = input('Insira o nome atual: ')
		newNome = input('Insira o novo nome: ')
		oldValor = {"nome":f"{oldNome}"}
		newValor = {"$set":{'nome':f'{newNome}'}}
		collection.update_one(oldValor,newValor)
		fContinuar()
	
	elif escolha == '2':
		oldDept = input('Informe o departamento atual: ')
		newDept = input('Informe o novo departamento: ')
		oldValor = {"departamento":f"{oldDept}"}
		newValor = {"$set":{"departamento":f"{newDept}"}}
		collection.update_one(oldValor,newValor)
		fContinuar()

	elif escolha == '3':
		oldEmpresa = input('Informe o empresa atual: ')
		newEmpresa = input('Informe o novo empresa: ')
		oldValor = {"empresa":f"{oldEmpresa}"}
		newValor = {"$set":{"empresa":f"{newEmpresa}"}}
		collection.update_one(oldValor,newValor)
		fContinuar()

	else:
		print('Opcao invalida!')
		fContinuar()

# Função - DELETE.
def fDelete():
	chave = input('Infome a chave: ')
	valor = input('Informe o valor: ')
	query = {f"{chave}":f"{valor}"}
	collection.delete_one(query)
	fContinuar()

# Função - Continuar.
def fContinuar():
	vContinuar = input('deseja realizar outra consulta? s - sim. n - nao.')
	if vContinuar.lower() == 's':
		fMenu()
	elif vContinuar.lower() == 'n':
		exit()
	else:
		print('Opcao invalida!')
		fContinuar()

# Função - Menu.
def fMenu():
	print('Escolha uma das opções abaixo.')
	print('1 - CREATE.\n2 - READ.\n3 - UPDATE.\n4 - DELETE.\n5 - SAIR.')
	escolha = input('Digite o numero da opcao: ')
	if escolha == '1':
		fCreate()
	elif escolha == '2':
		fRead()
	elif escolha == '3':
		fUpdate()
	elif escolha == '4':
		fDelete()
	elif escolha == '5':
		exit()
	else:
		print('opcao invalida!')
		fContinuar()

# - Conexão com o mongodb.
conexao = "mongodb://localhost:27017/"
client = pymongo.MongoClient(conexao)

# - Conexão com o banco de dados empresa.
dbName = 'empresa'
collectionName = 'funcionario'

mydatabase = client[dbName]
collection = mydatabase[collectionName]

# - Chama a função fMenu.
fMenu()