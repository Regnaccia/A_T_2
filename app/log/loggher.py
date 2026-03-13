def log(mode,text:str,print_if):
    verbouse = False
    debug = False

    if mode == "verbouse":
        verbouse = True

    if mode == "debug":
        verbouse = True
        debug = True

    if print_if == "verbouse" and verbouse:
        print(text)

    if print_if == "debug" and debug:
        print(text)

