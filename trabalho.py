nome = []
idade = []
cpf = []
telefone = []
email = []
todos = [nome,idade,cpf,telefone,email]
i=0
while i!=5:
			arquivo = open('arquivo.txt', 'w')
			print('****************************** MENU PRINCIPAL ******************************')
			print(' [1] - CADASTRO:')
			print(' [2] - LER:')
			print(' [3] - DELETAR:')
			print(' [4] - ATUALIZAR:')
			print(' [5] - SAIR:')
			
			opcao = int(input('\n Digite sua opcao: '))

		
			if opcao == 1:
				print(' \n ********************************* CADASTRO ********************************* \n')
				nome = (input('Nome:'))
				idade = (input('Idade:'))
				cpf = (input('Cpf:'))
				telefone = (input('Telefone:'))
				email = (input('Email:'))
				emailnv = (input('Confirmar email:'))
				print(' \n >>> Confira seus dados e digite confirmar ou excluir o cadastro:\n')
				print(' 1 - Sim, para confirmar')
				print(' 2 - Excluir cadastro')
				opcao = int(input('Digite sua opcao: '))
				print(' \n Cadastro concluído. \n')
			

		
				arquivo = open('arquivo.txt', 'r')
				cadastro = arquivo.read()
				print(cadastro)
			elif opcao == 2:
						print(' \n *********************************** LER *********************************** \n')
						print(nome)
						print(idade)
						print(cpf)
						print(telefone)
						print(email)
						print(' \n >>> Confira seus dados para a leitura.')
						print(' 1 - Sim')
						print(' 2 - Não')

						opcao = int(input('Digite sua opcao:'))

						if i==1:
								print('Leitura concluída.')
						elif i > 1:
								print('Resultado inválido.')
						if i < 1:
								print('Leitura concluída.')
						


			elif opcao == 3:
						print(' \n ***************************** MENU DE DELETAR *****************************')
						print(' \n Dados cadastrados: \n')
						print((' 1 - Nome: %s') %nome)
						print((' 2 - Idade: %s') %idade)
						print((' 3 - Cpf: %s') %cpf)
						print((' 4 - Telefone: %s') %telefone)
						print((' 5 - Email: %s') %email)

						opcao = int(input(' \n Selecione qual campo deseja excluir \n ( Se desejar excluir tudo digite (6):'))
						if opcao == 1:

							nome = ('Excluído')
							print('Nome será excluído: \n ')
							print(('Idade: %s') %idade)
							print(('Cpf: %s') %cpf)
							print(('Telefone: %s') %telefone)
							print(('Email: %s \n ') %email)


						elif opcao == 2:

							idade = ('Excluído')
							print('Idade será excluído: \n ')
							print(('Nome: %s') %nome)
							print(('Cpf: %s') %cpf)
							print(('Telefone: %s') %telefone)
							print(('Email: %s \n ') %email)


						elif opcao == 3:
							cpf = ('Exclluído')
							print('Cpf será excluído: \n ')
							print(('Nome: %s') %nome)
							print(('Idade: %s') %idade)
							print(('Telefone: %s') %telefone)
							print(('Email: %s \n ') %email)
					

						elif opcao == 4:

							telefone = ('Excluído')
							print('Telefone será excluído: \n ')
							print(('Nome: %s') %nome)
							print(('Idade: %s') %idade)
							print(('Cpf: %s') %cpf)
							print(('Email: %s \n ') %email)


						elif opcao == 5:

							email = ('Excluído')
							print('Email será excluído: \n ')
							print(('Nome: %s') %nome)
							print(('Idade: %s') %idade)
							print(('Cpf: %s') %cpf)
							print(('Telefone: %s \n ') %telefone)


						elif opcao == 6:

							print(' Todos os dados foram excluído.')
							print('...\n...\n...\n...\n...')
							nome = ('Excluído')
							idade = ('Excluído')
							cpf = ('Excluído')
							telefone = ('Excluído')
							email = ('Excluído')



			elif opcao == 4:
							print(' *************************** MENU DE ATUALIZAÇÃO ***************************')
							print((' 1 - Nome: %s') %nome)
							print((' 2 - Idade: %s') %idade)
							print((' 3 - Cpf: %s') %cpf)
							print((' 4 - Telefone: %s') %telefone)
							print((' 5 - Email: %s') %email)

							opcao = int(input(' \n Selecione qual campo deseja atualizar \n (Se deseja atualizar todos digite (6):'))

							if opcao == 1:

								nome = input('Nome:')
								print(nome)
								print(idade)
								print(cpf)
								print(telefone)
								print(email)

							if opcao == 2:

								idade = input('Idade:')
								print('Dados listados:')
								print(nome)
								print(idade)
								print(cpf)
								print(telefone)
								print(email)

							if opcao == 3:

								cpf = input('Cpf:')
								print(nome)
								print(idade)
								print(cpf)
								print(telefone)
								print(email)

							if opcao == 4:

								telefone = input('Telefone:')
								print(nome)
								print(idade)
								print(cpf)
								print(telefone)
								print(email)

							if opcao == 5:

								email = input('Email:')
								print(nome)
								print(idade)
								print(cpf)
								print(telefone)
								print(email)


							if opcao == 6:

								nome = input('Nome:')
								idade = input('Idade:')
								cpf = input('Cpf:')
								telefone = input('Telefone:')
								email = input('Email:')


						
			elif opcao == 5:
						print(' ************************ MENU DE SAÍDA DO CADASTRO ************************')
						print(' Caso tenha realizado seu cadastro, ou não, selecione: \n')
						print(' 1 - Sair do cadastro e encerrar.')
						print(' 2 - Voltar ao Menu Principal. \n')

						saida = int(input('Digite sua opcao:'))

						if saida == 1:
								print(' Você saiu do sistema de cadastro.')
								exit()

						if saida == 2:
								print(' Voltando ao Menu...')
						if opcao > 6:
								print('Resultado inválido.')








arquivo = open ('arquivo.txt', 'w')
arquivo.write(' MENU DE DADOS SALVOS \n')
arquivo.write(' Dados: \n Nome: %s \n Idade: %s \n Cpf: %s \n Telefone: %s \n Email: %s' %(nome, idade, cpf, telefone, email))
arquivo.close()															