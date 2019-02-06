
def string_to_floatlist(parsable: str, separator='\t'):
    string_list = parsable.split(separator)
    return [float(i) for i in string_list]


def floatlist_to_string(flist: list, round_to_int=True):
    string = ''
    for f in flist:
        if round_to_int:
            value_str = str(int(round(f, 0)))
        else:
            value_str = str(f)
        string = string + value_str + '\t'
    return string[0:-1]  # cut off the last \t character