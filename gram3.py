def hash3(words):
    hash_map = {
        'id': 1,
        '=': 2,
        'op': 3,
        'punct': 4,
        '$': 5
    }
    return [hash_map[word] if word in hash_map else None for word in words]

def parsing_table3(secuencia):
    fila = 1
    table = [
        [0,  1,  2,  3,  4,  5],
        [1,  5,  0,  4,  0,  0],
        [2,  0,  0,  0,  0,  20],
        [3,  0,  0,  0,  6,  0],
        [4,  13, 13, 13, 13, 13],
        [5,  0,  7,  0,  0,  0],
        [6,  11, 11, 11, 11, 11],
        [7,  8,  0,  0,  0,  0],
        [8,  0,  0,  4,  0,  0],
        [9,  10,  0,  0,  0,  0],
        [10, 12, 12, 12, 12, 12],
    ]
    stack = []
    stack.append(1)

    for i in range(len(secuencia)):
        if stack:
            fila = table[stack[-1]][secuencia[i]]
        
        stack.append(secuencia[i])
        stack.append(fila)

        #Reduce 3
        if fila == 4:
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            if stack and stack[-1] == 8:
                stack.append(8)
                stack.append(9)
        #Reduce 1
        elif fila == 6:
            if len(stack) >= 4:
                for _ in range(4):
                    stack.pop()
            if stack and stack[-1] == 1:
                stack.append(6)
                stack.append(2)
        #Reduce 2
        elif fila == 10:
            if len(stack) >= 10:
                for _ in range(10):
                    stack.pop()
            if stack and stack[-1] == 1:
                stack.append(7)
                stack.append(3)
        #
        elif fila==0:
            return "Error en el parsing"
    #Accept
    if fila == 20:
        return "Proceso de parsing exitoso"
    else:
        return "Error en el parsing"