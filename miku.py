test_cases = int(input())

results = []
for _ in range(test_cases):
    string = input().strip()
    length = len(string)
    
    prefix_sum_w = [0] * (length + 1)
    
    for index in range(length):
        prefix_sum_w[index + 1] = prefix_sum_w[index] + (1 if string[index] == 'w' else 0)

    indices_u = []
    for position in range(length):
        if string[position] == 'u':
            indices_u.append(position)
    
    valid_count = 0
    total_u = len(indices_u)

    for i in range(total_u):
        for j in range(i + 1, total_u):
            left_bound = indices_u[i] + 1
            right_bound = indices_u[j] - 1
            if left_bound <= right_bound:
                count_w = prefix_sum_w[right_bound + 1] - prefix_sum_w[left_bound]
                if count_w > 0:
                    valid_count += 1

    results.append(valid_count)

print("\n".join(map(str, results)))