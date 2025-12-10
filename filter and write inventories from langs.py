lang_id_p = []
lang_id_a = []

with open('values_Papunesia.txt', 'w', encoding="utf8") as vp:

    with open('values_Australia.txt', 'w', encoding="utf8") as va:

        with open('languages_Papunesia.txt', 'r', encoding="utf8") as lp:

            for line in lp:
                split_line = line.split(',')
                if split_line[0] not in lang_id_p:
                    lang_id_p.append(split_line[0])

            with open('languages_Australia.txt', 'r', encoding="utf8") as la:

                for line in la:
                    split_line = line.split(',')
                    if split_line[0] not in lang_id_a:
                        lang_id_a.append(split_line[0])

                with open('values.csv', encoding="utf8") as sheet:

                    for line in sheet:
                        split_line = line.split(',')

                        if split_line[1] in lang_id_p:
                            print(line)
                            vp.write(line)

                        if split_line[1] in lang_id_a:
                            print(line)
                            va.write(line)


