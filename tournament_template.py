def solve(names, powers):
    while len(names) > 1:
        next_round_names = []
        next_round_powers = []
        for i in range(0, len(names), 2):
            name1, name2 = names[i], names[i+1]
            power1, power2 = powers[i], powers[i+1]

            if power1 > power2:
                new_name = name1
                new_power = power1 + power2
            elif power2 > power1:
                new_name = name2
                new_power = power2 + power1
            else:  # Equal powers: fusion
                new_name = name1 + name2
                new_power = power1 + power2

            next_round_names.append(new_name)
            next_round_powers.append(new_power)

        names = next_round_names
        powers = next_round_powers

    return names[0]

# Driver code
if __name__ == "__main__":
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        names = input().strip().split()
        powers = list(map(int, input().strip().split()))
        winner = solve(names, powers)
        results.append(winner)
    
    print("\n".join(results))