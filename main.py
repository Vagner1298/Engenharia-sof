print('Calculadora simples de dois números')
#Pedindo o primeiro número para o usuário e armasenando isso na vareável num1
#Convertendo a String da vareável num1 para float
num1 = float(input('Digite um número: '))
#Pedindo o segundo número para o usuário e armasenando isso na vareável num2
#Convertendo a String da vareável num2 para float
num2 = float(input('Digite outro número: '))
#Realizando os cálculos e imprindo os resultados
print(num1,' + ',num2,' = ',num1+num2,';\n',num1,' - ',num2,' = ',num1-num2,';\n',num1,' / ',num2,' = ',num1/num2,';\n',num1,' * ',num2,' = ',num1*num2,';\n',num1,' ^',num2,' = ',num1**num2,';\nResto da divisão de ',num1,' / ',num2,' = ',num1%num2,'.')