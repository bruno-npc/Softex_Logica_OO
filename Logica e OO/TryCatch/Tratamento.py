#Crie uma situação em que ocorra uma exceção dentro de um código. 
#Utilize try/catch para realizar a captura e tratamento dessa exceção. 


#x = 55 #Para o erro funcionar, a variavel precisa ser comentada ou removida.

try:
  print(x)
except NameError:
  print("Variavel x não foi definida.")
except:
  print("Erro inesperado no sistema.")