numeros = [4.5, 2, 9.0, 7, 9.8]

def maior_num(vetor):
    if not vetor:
        return None
    
    maior = vetor[0]
    posicao = 0

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i
    return (maior, posicao)

print(maior_num(numeros))