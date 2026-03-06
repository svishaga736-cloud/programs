if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Extract all scores and find the unique second-lowest
    scores = sorted({s[1] for s in students})
    second_lowest_score = scores[1]

    # Filter names that match the second lowest score and sort them
    result_names = sorted([s[0] for s in students if s[1] == second_lowest_score])

    # Print each name on a new line
    for name in result_names:
        print(name)
