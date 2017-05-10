
search_files = ['\gmara','\Rashi','\Tosafot']


def Search(text):
    for j, makor in enumerate(mapping):
        if len(makor) > 0:
            for i, m in enumerate(makor):
                if type(m) == tuple:
                    path = my_dir + '%s.json' % m[0]
                    f_in = open(path, 'r', encoding='utf8')
                    js = json.load(f_in)
                    f_in.close()

                    txt = js['text']
                    daf = m[1]
                    for line in txt[daf]:
                        if type(line) == list:
                            t = ''
                            for i in line:
                                if type(i) == int:
                                    continue
                                t += i
                                if text in t:
                                    mak.append([t, daf_num, m[0]])

                        elif text in line:
                            mak.append([line, daf, m[0]])
                else:
                    path = my_dir + '%s.json' % m
                    f_in = open(path, 'r', encoding='utf8')
                    js = json.load(f_in)
                    f_in.close()
                    txt = js['text']
                    for daf_num, daf in enumerate(txt):
                        for line in daf:
                            if type(line) == list:
                                t = ''
                                for i in line:
                                    if type(i) == int:
                                        continue
                                    t += i
                                    if text in t:
                                        mak.append([t, daf_num, m])

                            elif text in line:
                                mak.append([line, daf_num, m])
    print('mak:', len(mak))
    return mak
