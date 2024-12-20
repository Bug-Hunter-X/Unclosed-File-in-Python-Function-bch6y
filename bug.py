def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some processing ...
    # forgot to close the file
    return