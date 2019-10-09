class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return '{}.{}'.format(self.nome, self.sobrenome)

print('='*50)
print('\n'*5)

nome = 'Maykon'
sobrenome = 'Granemann'

p = Pessoa(nome, sobrenome)

with  open('pessoas.txt','a') as arquivo:
    arquivo.write( str(p) +'\n')

with  open('pessoas.txt','r') as arquivo:
    for l in arquivo:
        ps = l.strip().split('')
        psa = Pessoa( ps[0], ps[1] )
        print( 'Nome:{} Sobrenome: {}'.format(psa.nome, psa.sobrenome   ) )

print('\n'*5)
print('='*50)
