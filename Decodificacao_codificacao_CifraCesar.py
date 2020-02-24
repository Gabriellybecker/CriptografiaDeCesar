def criptografia():
   mensagem = input('Digite a mensagem:')
   cifra = 2
   for i in range(len(mensagem)):
       print (chr(ord(mensagem[i]) + cifra), end='')
   decisao()
       
def descodificacao():
    mensagem = input('Digite a mensagem:')
    cifra = 2
    for i in range(len(mensagem)):
       print (chr(ord(mensagem[i]) - cifra), end='')
    decisao()
    
def decisao(): 
   decisao = input('\nDeseja fazer a criptografia ou a descodificacao? Digite C para criptografia ou D para descodificacao.\n')

   if decisao == 'C' or decisao == 'c':
    criptografia()
   elif decisao == 'D' or decisao == 'd':
    descodificacao()
   else:
    print("Escolha uma das duas opçoes")
decisao()
