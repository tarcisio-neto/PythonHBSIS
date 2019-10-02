# 45- Ler 10 valores e escrever quantos desses valores
#  lidos estão no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo)
#  e quantos deles estão fora deste intervalo.



contador_dentro_intervalo = 0
contador_fora_intervalo = 0

for num_atual in range(0,10,1):
    print('digite o {}º'.format(num_atual + 1))
    num = int(input())
    if num >=10 and num <=20:
        contador_dentro_intervalo = contador_dentro_intervalo + 1
    else:
        contador_fora_intervalo = contador_fora_intervalo + 1
    
       
print('{} números dentro do intervalo 10-20'.format(contador_dentro_intervalo))
print('{} números fora do intervalo 10-20'.format(contador_fora_intervalo))