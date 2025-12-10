
with open('languages_Papunesia.txt', 'w') as lp:
    with open('languages_Australia.txt', 'w') as la:
        with open('languages.csv') as sheet:
            for line in sheet:
                split_line = line.split(',')
                if 'Australia' in split_line:
                    la.write(line)
                if 'Papunesia' in split_line:
                    lp.write(line)
