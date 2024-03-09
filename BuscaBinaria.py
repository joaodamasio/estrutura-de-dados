def busca_binaria(array, item, inicio=0, fim=None):
    if fim is None:
        fim = len(array)-1
    if inicio <= fim:
        m = (inicio + fim)//2
        if array[m] == item:
            return m
        if item < array[m]:
            return busca_binaria(array, item, inicio, m-1)
        else:
            return busca_binaria(array, item, inicio, m+1, fim)
        
    return None