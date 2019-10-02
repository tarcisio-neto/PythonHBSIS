# - Ler as notas da 1ª e 2ª avaliações de um aluno. Calcular a média aritmética simples e 
# escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou 
# maior que 6 o aluno é aprovado). Escrever também a média calculada.



print ('Digite nota 1 ')
nota1 = int(input())

print ('Digite nota 2 ')
nota2 = int(input())

media = ((nota1 + nota2)/2)


if media < 6:
    print('Aluno reprovado com média {}'.format(media))
else:
    print('Aluno  aprovado com média {}'.format(media))

