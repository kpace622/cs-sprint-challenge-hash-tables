def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    
    # Your code here
    hash_table = {}

    if len(weights) <= 1:
        return None

    for x in weights:
            hash_table[x] = x

    for x in hash_table:
        

    print(hash_table)
    return None
