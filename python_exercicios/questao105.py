from statistics import median

def nota(*num,sit=False):
    notas = {}     
    notas["Maior"] = max(num)
    notas["Menor"] = min(num)
    notas["Total"] = len(num)   
    notas["Média"] = sum(num)/len(num)
    if sit:
        if notas["Média"] >= 7:
            notas["Situação"] = 'Aprovado'
        else:
            notas["Situação"] = 'Reprovado'
    return notas
    

print(nota(5.6, 4.2,5.3,6.4))



