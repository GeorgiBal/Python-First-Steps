def assign_holes(mice, holes):
    if len(mice) != len(holes):
        return "Number of mice and holes should be the same"

    mice.sort()
    holes.sort()

    max_diff = 0
    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])

    return max_diff

mice = [-4, 2, 4]
holes = [4, 0, 5]

print(assign_holes(mice, holes))