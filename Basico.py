#EXERCIO_1 SOLICITAR AO USUARIO SUA FUNCIONAL
# pergunta ao usuario  e guarda na variavel
Identificacao = input("Digite o numero da sua funcional: ")
# mostra a menssagen usando variavel 
print(f" Aguardo sua senha {Identificacao}")

#EXERCIO_2 SOLICITE AO USUARIO SUA SENHA
# 3 tentativas, so numeros inteiros
tentativa = 0
Valido = False
while tentativa < 3 and not Valido:
    senha = int(input("\nInsira sua senha: "))
    if senha == 1010:
        print (f"Acesso concedido {Identificacao}")
        Valido=  True
    else: print ("\nAcesso negado")
    tentativa =+ 1
