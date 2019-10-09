#criar uma list int ou string  , escrever a lista no arquivo, ler o arquivo e mostrar na tela


with open('nomes.txt', 'a') as arquivo:
    arquivo.write(input('Digite nome:') + ',')

with open ('nomes.txt', 'r') as arquivo:
    for l in arquivo:
        nomes = l.strip().split(',')
        for i in range (0,len(nomes)):
            print(f'{nomes[i]}')


