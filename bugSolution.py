def function_with_closed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some processing ...
        contents = f.read()
        return contents
    except FileNotFoundError:
        return None
    finally:
        f.close()    