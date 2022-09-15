import soma
import subtracao
import divisao
import multiplicacao

class operacoes:
  def operar(Valor1, Valor2, entrada):
   if entrada == 1:
      final = resul = soma.soma.somar(Valor1, Valor2)

   elif entrada == 2:
      final = resul = subtracao.subtracao.subtrair(Valor1, Valor2)

   elif entrada == 3:
      final = resul = divisao.divisao.dividir(Valor1, Valor2)

   elif entrada == 4:
      final = resul = multiplicacao.multiplicacao.multiplicar(Valor1, Valor2)
   else:
       print("Escolha Invalida!!")

   print("Valor 1 complexo: ", complex(Valor1))
   print("Valor 2 complexo: ", complex(Valor2))

   return final
