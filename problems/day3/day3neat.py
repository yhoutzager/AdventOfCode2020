import time


def create_coordinates(slope_x, slope_y, width, height):
    return [[slope_x * (i//slope_y) % width, i] for i in range(0, height, slope_y)]


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

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    answer2 = 1
    for slope in slopes:
        trees = 0
        for coordinate in create_coordinates(slope[0], slope[1], len(array[0]), len(array)):
            if array[coordinate[1]][coordinate[0]] == '#':
                trees += 1
        answer2 *= trees

    print('Answer part 2: {}'.format(answer2))

    end = time.time()
    print('Time: {:.3f}ms'.format(end - start))
