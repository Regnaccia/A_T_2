def check_duplicate_in_list(list:list):
    seen = []
    dupliacte = []
    for x in list:
        if x not in seen:
            seen.append(x)

        elif x not in dupliacte:
            dupliacte.append(x)

    return dupliacte


if __name__ == "__main__":
    d = check_duplicate_in_list([1,11,21,2,31,3,41,4,5])
    print(d)
