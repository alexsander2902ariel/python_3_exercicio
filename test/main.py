def sum_numbers_sequence(vet):
    cont=0
    for i in range(len(vet)):
       cont= cont+(vet[i]*10)
    return(cont/10)

def div_numbers_sequence(x,y):
    cont=0
    if (y!= 0):
        cont=(x*10)/(y*10)
    return(cont)