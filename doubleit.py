def solve(num_decisions: int, decision_sequence: str) -> int:
    current_offer = 1
    total_points = 0
    for decision in decision_sequence:
        if decision == 'T':
            total_points += current_offer
            current_offer = 1
        else:
            current_offer *= 2
    return total_points

def main():
    try:
        num_test_cases = int(input())
        results = []
        
        for _ in range(num_test_cases):
            num_decisions = int(input())
            decision_sequence = input().strip()
            result = solve(num_decisions, decision_sequence)
            results.append(result)
        
        for result in results:
            print(result)

    except ValueError as error:
        print(f"Invalid input: {error}")

if __name__ == '__main__':
    main()