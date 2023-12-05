from re import sub
from input import input_string
from itertools import chain


def create_range(range_lst):
    range_lst = list(map(int, range_lst))
    return [range(range_lst[0], range_lst[0] + range_lst[2]), range(range_lst[1], range_lst[1] + range_lst[2])]


def parse_input(string):
    def parse_map(map_string):
        return list(map(lambda x: create_range(x.split()), sub(r'[\w-]*\s*\w*:\s*', '', map_string).split('\n')))

    lst = string.split('\n\n')
    seeds = [int(item) for item in sub(r'seeds\s*:\s*', '', lst.pop(0)).split()]
    maps = {}
    for i in range(len(lst)):
        maps['{}'.format(i + 1)] = parse_map(lst.pop(0))

    return [seeds, maps]


def get_seed_ranges(data_list):
    seeds = [data_list[i] if i % 2 == 0 else data_list[i] + data_list[i - 1] for i in range(len(data_list))]
    return [range(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


def split_ranges(ranges, size):
    sub_ranges = []
    for r in ranges:
        # Iterate over the range in steps of 'size'
        sub_ranges.extend(range(i, min(i + size, r.stop)) for i in range(r.start, r.stop, size))
    return sub_ranges


def find_closest_location(data, is_range):
    if is_range:
        seeds, maps = data
    else:
        seeds, maps = parse_input(data)

    locations = []
    for s in seeds:
        current_id = s
        for m in range(1, len(maps) + 1):
            for ranges in maps[str(m)]:
                if current_id in ranges[1]:
                    index = ranges[1].index(current_id)
                    current_id = ranges[0][index]
                    break

        locations.append(current_id)

    print('.') if is_range else print(min(locations))
    return min(locations)


def find_closest_location_for_seed_range(string):
    seeds, maps = parse_input(string)
    locations = []
    seed_ranges = split_ranges(get_seed_ranges(seeds), 1000000)

    for i in range(len(seed_ranges)):
        data = [seed_ranges[i], maps]
        locations.append(find_closest_location(data, True))

    print(min(locations))


if __name__ == '__main__':
    # find_closest_location(input_string, False)
    find_closest_location_for_seed_range(input_string)
