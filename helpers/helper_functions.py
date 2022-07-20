def is_float(input: str) -> bool:
    flag = False
    try:
        float(input)
        flag = True
    except ValueError as _:
        pass

    return flag
