def hash2(words):
    hash_map = {
        'op': 1,
        'punct': 2,
        'id': 3,
        'num': 4,
        '$': 5
    }
    return [hash_map[word] if word in hash_map else None for word in words]

def parsing_table2(secuencia):
    fila = 1
    table = [
        [0, 1,  2,  3,  4,  5],
        [1, 0,  0,  4,  5,  0],
        [2, 0,  0,  0,  0,  9],
        [3, 6,  0,  0,  0,  0],
        [4, 12, 12, 12, 12, 12],
        [5, 13, 13, 13, 13, 13],
        [6, 0,  0,  0,  5,  0],
        [7, 0,  8,  0,  0,  0],
        [8, 11, 11, 11, 11, 11],
    ]
    stack = []
    stack.append(1)

    for i in range(len(secuencia)):
        if stack:
            fila = table[stack[-1]][secuencia[i]]
        stack.append(secuencia[i])
        stack.append(fila)
        #Reduce 2
        if fila == 4:
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            if stack and stack[-1] == 1:
                stack.append(7)
                stack.append(3)
        #Reduce 3
        elif fila == 5:
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            if stack and stack[-1] == 6:
                stack.append(8)
                stack.append(7)
        #Reduce 1
        elif fila == 8:
            if len(stack) >= 8:
                for _ in range(8):
                    stack.pop()
            if stack and stack[-1] == 1:
                stack.append(6)
                stack.append(2)
        #Error en caso de que se haga un movimiento ilegal en el automatas
        elif fila==0:
            return "Error en el parsing"
    #Accept    
    if fila == 9:
        return "Proceso de parsing exitoso"
    else:
        return "Error en el parsing"