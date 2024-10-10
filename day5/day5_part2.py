import math
from typing import List, Set, Tuple



def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.read().split("\n\n")


def map_source_to_destination(sources: List[int], destination_map: List[List[int]]) -> List[int]:
    new_sources = {source:source for source in sources}
    for destination_mappping_start, source_mapping_start, mapping_range in destination_map:
        for source in sources:
            if source >= source_mapping_start and source <= source_mapping_start + mapping_range:
                new_sources[source] = (
                    destination_mappping_start + 
                    (source - source_mapping_start)
                )
    return list(new_sources.values())


def str_to_int_list(str_list: str) -> List[int]:
    return [int(e) for e in str_list.strip().split()]


def get_seeds_range(seeds: List[int]) -> List[int]:
    seeds_ranges = []
    for index in range(0, len(seeds), 2):
        seeds_ranges.append((seeds[index], seeds[index + 1]))
    return seeds_ranges


def get_cut_points(destination_map):
    cut_points = {0, math.inf}
    for _, source_start, size in destination_map:
        cut_points.add(source_start + size)
        cut_points.add(source_start)
    return cut_points

def do_mapping(input: List[str]) -> List[int]:
    seeds = input[0].replace("seeds: ", "")
    seeds = str_to_int_list(seeds)
    seeds_ranges = get_seeds_range(seeds)
    for input_line in input[1:]:
        print("line")
        destination_map = input_line.split("\n")[1:]
        destination_map = [str_to_int_list(d) for d in destination_map]
        seeds = map_source_to_destination(seeds, destination_map)
    return seeds

if __name__ == '__main__':
    input = get_input("input.txt")
    print(min(do_mapping(input)))
