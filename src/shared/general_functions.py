def sum_all_initialized_int_attributes(class_object) -> int:
    total_sum = 0
    for field in vars(class_object):
        value = getattr(class_object, field)
        if isinstance(value, int):
            total_sum += value
    return total_sum
