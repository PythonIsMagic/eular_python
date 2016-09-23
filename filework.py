def import_names(filename):
    # Each name is contained in quotes ("NAME")
    # and also separated by commas("NAME1", "NAME2, "NAME3")

    names = []
    newname = ''
    with open(filename) as f:

        while True:
            char = f.read(1)
            if not char:
                break  # Empty string means EOF

            # Start a new name with each quote
            if char == "\"" and newname != '':
                names.append(newname)
                newname = ''
            elif char == "\"" or char == ',':
                # Ignore formatting characters
                continue
            else:
                newname += char

    # To sort we can merely use the builtin sorted()
    return sorted(names)
