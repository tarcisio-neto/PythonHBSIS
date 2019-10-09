print('='*60)

salario = float(input('{}Digite o salario liquido: '.format( ' '*5)))
#Imprimindo salario
print('{}O salario liquido é:{}R${:8.2f}'.format( ' '*5,' '*10, salario ) )

print('{}Gastos E:{} R${:8.2f}'.format(' '*5,' '*20, salario*0.5 ) )
print('{}Investimestos LP:{} R${:8.2f}'.format(' '*5,' '*12, salario*0.2 ) )
print('{}Investimestos CP:{} R${:8.2f}'.format(' '*5,' '*12, salario*0.1 ) )
print('{}Livre:{} R${:8.2f}'.format(' '*5,' '*23, salario*0.2 ) )

print('='*60)