def filter_pairs(numbers, sum_filter): 
    pairs = []
    for i in numbers:
        remove = numbers.pop(1)
        diff=sum_filter-remove
        if diff in numbers:
            pairs.append((remove, diff))
    return print(pairs)

if __name__ == '__main__':
 
    numbers = [1, 2, 3, 4, 5, 5, 6, 7]
    sum_filter = 10
    filter_pairs(numbers, sum_filter)
