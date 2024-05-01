def hash1(words):
    hash_map = {
        'kw': 1,
        'id': 2,
        'punct': 3,
        '$': 4
    }
    return [hash_map[word] if word in hash_map else None for word in words]

def parsing_table1(secuencia):
    fila = 1
    table = [
        [0, 1,  2,  3,  4],
        [1, 3,  4,  0,  0],
        [2, 0,  0,  0,  7],
        [3, 0,  4,  0,  0],
        [4, 12, 12, 12, 12],
        [5, 0,  0,  6,  0],
        [6, 11, 11, 11, 11],
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
            if stack and stack[-1] == 3:
                stack.append(12)
                stack.append(5)
        #Reduce 1
        elif fila == 6:
            if len(stack) >= 6:
                for _ in range(6):
                    stack.pop()
            if stack and stack[-1] == 1:
                stack.append(11)
                stack.append(2)
        #Error en caso de que se haga un movimiento ilegal en el automata
        elif fila==0:
            return "Error en el parsing"
    #Accept    
    if fila == 7:
        return "Proceso de parsing exitoso"
    else:
        return "Error en el parsing"