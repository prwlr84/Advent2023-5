from re import sub

from input import input_string


def create_range(range_lst):
    range_lst = list(map(int, range_lst))
    return [range(range_lst[0], range_lst[0] + range_lst[2]), range(range_lst[1], range_lst[1] + range_lst[2])]


def parse_input(string):
    def parse_map(map_string):
        return list(map(lambda x: create_range(x.split()), sub(r'[\w-]*\s*\w*:\s*', '', map_string).split('\n')))

    lst = string.split('\n\n')
    seeds = sub(r'seeds\s*:\s*', '', lst.pop(0)).split()
    maps = {}
    for i in range(len(lst)):
        maps['{}'.format(i + 1)] = parse_map(lst.pop(0))

    return [seeds, maps]


def find_closest_location(string):
    seeds, maps = parse_input(string)
    locations = []
    for s in seeds:
        current_id = s
        for m in range(1, len(maps) + 1):
            for ranges in maps[str(m)]:
                if s in ranges[1]:
                    index = ranges[1].index(current_id)
                    current_id = ranges[0][index]
                    break

        locations.append(current_id)
        print(current_id)

    print(locations)


if __name__ == '__main__':
    find_closest_location(input_string)
