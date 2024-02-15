def sum_of_processor(p):
    return sum(p)


def minimal_load_processor(arr_processors: list):
    _min = 0
    min_load_processor = sum_of_processor(arr_processors[0])
    for processor in arr_processors:
        if sum_of_processor(processor) < min_load_processor:
            min_load_processor = sum_of_processor(processor)

    return min_load_processor
