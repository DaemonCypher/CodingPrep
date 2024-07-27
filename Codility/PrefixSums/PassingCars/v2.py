def solution(A):
    east_count = 0  # Count of cars traveling east
    passing_cars = 0  # Count of pairs of passing cars

    for car in A:
        if car == 0:  # Car traveling east
            east_count += 1
        else:  # Car traveling west
            passing_cars += east_count
            if passing_cars > 1000000000:
                return -1

    return passing_cars