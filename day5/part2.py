import math
from typing import List, Set, Tuple



def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().split("\n\n")

def intersect_intervals(
        interval_1_start,
        interval_1_size,
        interval_2_start,
        interval_2_size,
        offset: int
):
    interval_1_end = interval_1_start + interval_1_size - 1
    interval_2_end = interval_2_start + interval_2_size - 1
    # No intersection -> Interval 1 no change
    if interval_2_end < interval_1_start:
        return [(interval_1_start, interval_1_size, False)]
    if interval_2_start  > interval_1_end:
        return [(interval_1_start, interval_1_size, False)]
    # Interval 2 starts before and ends inside -> Break in 2
    if (interval_2_start < interval_1_start and interval_2_end <= interval_1_end):
        part1_start = interval_1_start + offset
        part1_size = interval_2_end - interval_1_start + 1
        part2_start = interval_1_start + part1_size 
        part2_size = interval_1_end - interval_2_end
        return [(part1_start, part1_size, True), (part2_start, part2_size, False)]
    # Interval 2 starts inside and ends inside -> Break in 3
    if (interval_2_start >= interval_1_start and interval_2_end <= interval_1_end):
        part1_start = interval_1_start
        part1_size = interval_2_start - interval_1_start + 1
        part2_start = interval_2_start + offset
        part2_size = interval_2_end - interval_2_start + 1
        part3_start = interval_2_end  + 1
        part3_size = interval_1_end - interval_2_end
        return [(part1_start, part1_size, False), (part2_start, part2_size, True), (part3_start, part3_size, False)]
    # Interval 2 starts inside and ends outside -> Break in 2
    if (interval_2_start > interval_1_start
        and interval_2_start <= interval_1_end 
         and interval_2_end > interval_1_end):
        part1_start = interval_1_start
        part1_size = interval_2_start - interval_1_start
        part2_start = interval_2_start + offset
        part2_size = interval_1_end - interval_2_start + 1
        return [(part1_start, part1_size, False), (part2_start, part2_size, True)]
    # Interval 2 covers completely interval 1 -> No break, just transform
    if (interval_2_start <= interval_1_start and interval_2_end >= interval_1_end):
        return [(interval_1_start + offset, interval_1_size, True)]
    print(interval_1_start, interval_1_end, interval_2_start, interval_2_end)


def map_source_to_destination(sources: List[Tuple[int, int]], destination_map: List[List[int]]) -> List[int]:
    final_intervals = []
    for seed, size in sources:
        current_intervals = [(seed, size)]
        for destination_mappping_start, source_mapping_start, mapping_range in destination_map:
            new_intervals_to_map = []
            for interval_start, interval_size in current_intervals:
                print("**** mapping ", source_mapping_start, mapping_range, destination_mappping_start)
                intersected_intervals = intersect_intervals(
                    interval_start,
                    interval_size,
                    source_mapping_start,
                    mapping_range,
                    destination_mappping_start - source_mapping_start
                )
                for interval in intersected_intervals:
                    if interval[2]:
                        print("Seed ", seed, size)
                        print("Interval", interval)
                        if interval[1] > 0:
                            final_intervals.append((interval[0], interval[1]))
                    else:
                        new_intervals_to_map.append((interval[0], interval[1]))
        if new_intervals_to_map:
            final_intervals += new_intervals_to_map
    return final_intervals


def str_to_int_list(str_list: str) -> List[int]:
    return [int(e) for e in str_list.strip().split()]


def get_seeds_range(seeds: List[int]) -> List[int]:
    seeds_ranges = []
    for index in range(0, len(seeds), 2):
        seeds_ranges.append((seeds[index], seeds[index + 1]))
    return seeds_ranges



def do_mapping(input: List[str]) -> List[int]:
    seeds = input[0].replace("seeds: ", "")
    seeds = str_to_int_list(seeds)
    seeds_ranges = get_seeds_range(seeds)
    for input_line in input[1:]:
        destination_map = input_line.split("\n")[1:]
        destination_map = [str_to_int_list(d) for d in destination_map]
        print("Seed ranges ", seeds_ranges)
        seeds_ranges = map_source_to_destination(seeds_ranges, destination_map)
    return min(seed_range[0] for seed_range in seeds_ranges)


if __name__ == '__main__':
    input = get_input("input.txt")
    print(do_mapping(input))
