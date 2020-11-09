def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []

    for x in a:
        hash_table[x] = x

    for x in a:
        if x < 0:
            i = -x
            print("i", i)
            if hash_table.get(i) == None:
                continue
            else:
                result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
