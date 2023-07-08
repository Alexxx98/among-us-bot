def sorter(list: list) -> list:
    llen = len(list)
    sorted = ["_" for _ in range(llen)]
    for path in list:
        filename = path.split("\\")[-1]
        n = ""
        for char in filename:
            try:
                int(char)
                n += char
            except ValueError:
                pass
        try:
            sorted[int(n)] = path
        except ValueError:
            sorted[0] = path
    return sorted
