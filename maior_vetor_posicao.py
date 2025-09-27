numeros = [100, 2, 100, 7, 9, 100]

def maior_num(vetor):
    if not vetor:
        return None
    
    maior = vetor[0]
    posicao = []

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = [i]
        elif vetor[i] == maior:
            posicao.append(i)
    return (maior, posicao)

print(maior_num(numeros))