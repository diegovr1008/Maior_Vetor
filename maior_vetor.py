numeros = [4, 2, 9, 7, 5, 50]

def maior_num(vetor):
    if not vetor:
        return None
    maior = vetor[0]
    for num in vetor:
        if num > maior:
            maior = num
    return maior

print(maior_num(numeros))