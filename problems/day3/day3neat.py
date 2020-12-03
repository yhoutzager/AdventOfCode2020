import time


def create_coordinates(slope_x, slope_y, width, height):
    return [[slope_x * i % width, i] for i in range(0, height, slope_y)]


if __name__ == '__main__':
    start = time.time()
    with open("input", "r") as file:
        array = [line.strip() for line in file.readlines()]

    slopes = [[3, 1]]
    answer = 0
    for slope in slopes:
        for coordinate in create_coordinates(slope[0], slope[1], len(array[0]), len(array)):
            if array[coordinate[1]][coordinate[0]] == '#':
                answer += 1


    print('Answer part 1: {}'.format(answer))
    slopes = {[1, 1]: 0, [3, 1]: 0, [5, 1]: 0, [7, 1]: 0, [1, 2]: 0}

    for slope in slopes.keys():
        for coordinate in create_coordinates(slope[0], slope[1], len(array[0]), len(array)):
            if array[coordinate[1]][coordinate[0]] == '#':
                slopes[slope] += 1

    answer2 = 1
    answer2 = [answer2 * i for i in slopes.values()]
    print('Answer part 2: {}'.format(answer2))

    end = time.time()
    print('Time: {:.3f}ms'.format(end - start))
