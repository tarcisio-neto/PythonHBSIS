# Criar um programa que:
# 1. Leia uma frase digitada pelo usuário.
# 2. Leia uma letra digitada pelo usuário.
# 3. Informe para o usuário quantas vezes aparece na frase (passo 1) a letra (passo 2).
# 4. Informe para o usuário a posição em que a letra aparece a primeira vez na frase.
# 5. Informe para o usuário a posição em que a letra aparece pela última vez na frase.

print ('='*60)
frase = input('{}Digite uma frase: '.format(' '*5))
letra = input('{}Digite uma letra: '.format(' '*5))

# conta letras  digitadas 
print('{0}A letra foi encontrada {1} vezes'.format(' '*5, frase.count(letra)))

#procura a letra do inicio para fim
print('{0}A letra foi encontrada pela primeira vez na posição: {1}'.format(' '*5, frase.find(letra)+1))

# procura a letra do fim para o início 
print('{0}A letra foi encontrada pela última vez na posição: {1}'.format(' '*5, frase.rfind(letra)+1))
print ('='*60)

