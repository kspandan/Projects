def int_to_8bit(a):
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr

def add2(a):
    decimal = 0
    for digit in a:
        decimal = decimal * 2 + int(digit)
    return decimal

def listToInt(integers):
    strings = [str(integer) for integer in integers]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

def chunks(l, n):
    final = [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n)]
    return final

def single_bit_permutation(a):
    rows = []
    for i in range(4):
        a_list = [int(x) for x in str(int_to_8bit(a[i]))]
        rows.append(a_list)
    list = []
    for i in range(8):
        for j in range(4):
            list.append((rows[j][i]))
    k = chunks(list, 8)

    for i in range(4):
        a = listToInt(k[i])
        k[i] = add2(str(a))
    return (k)
    
def inv_single_bit_permutation(a):
    rows = []
    for i in range(4):
        a_list = [int(x) for x in str(int_to_8bit(a[i]))]
        rows.append(a_list)
    list = []
    for i in range(4):
        for k in range(4):
            list.append(rows[k][i])
            list.append(rows[k][(i + 4) % 8])

    k = chunks(list, 8)
    for i in range(4):
        a = listToInt(k[i])
        k[i] = add2(str(a))
    return(k)
    
print("Input : [98, 5, 29, 142]" ) 
print("Output after Operation : " ,  single_bit_permutation([98, 5, 29, 142]))
print("Output after Reverse Operation on  [24, 130, 55, 150] : " , inv_single_bit_permutation([24, 130, 55, 150])  )
