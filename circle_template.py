def solve(N: int, X: list[float], Y: list[float]) -> float:
    """
    Return the area of the rectangle described by the given points.
    
    N: the number of given points
    X: a list containing the x-coordinate of each point
    Y: a list containing the y-coordinate of each point
    """
    
    min_x = min(X)
    max_x = max(X)
    min_y = min(Y)
    max_y = max(Y)
    
    
    width = max_x - min_x
    height = max_y - min_y
    
    
    return width * height


def main():
    try:
        
        num_test_cases = int(input())
        results = []
        
        
        for _ in range(num_test_cases):
            
            N = int(input())
            
            
            X, Y = zip(*(map(float, input().split()) for _ in range(N)))
            
            
            result = solve(N, X, Y)
            results.append(result)
        
        
        for result in results:
            print(result)

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == '__main__':
    main()
