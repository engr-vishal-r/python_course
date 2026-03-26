def flatten_list(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


data = [[1, 2], [3, 4, [5, 6]]]

print(flatten_list(data))