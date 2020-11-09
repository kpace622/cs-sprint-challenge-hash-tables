def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # Your code here
    hash_table = {}
    result = []

    if len(weights) <= 1:
        return None
        
    weight_num = 1
    weight_num2 = 1
    weight_num3 = 1

    for x in range(0, length - 1):
        hash_table[weights[x] + weights[weight_num]] = f"{x} {x + 1}"
        weight_num += 1

    for x in range(1, length - 1):
        if weights[x] + weights[weight_num2] in hash_table:
            continue
        else:
            hash_table[weights[x] + weights[weight_num2]] = f"{x} {x + 1}"
            weight_num2 += 1

    for x in range(2, length - 1):
        if weights[x] + weights[weight_num3] in hash_table:
            continue
        else:
            hash_table[weights[x] + weights[weight_num3]] = f"{x} {x + 1}"
            weight_num3 += 1

    print("Hash table", hash_table)
        
    string = hash_table[limit]
    string2 = string.split( )

    string2.sort(reverse=True)

    for i in range(0, len(string2)): 
        string2[i] = int(string2[i]) 
    
    return string2
    # return None
