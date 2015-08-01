import sys
to_do_dct = {}
number = 0

if 'add' in sys.argv:
    number += 1
    to_do_dct[str(number)] = ' '.join(sys.argv[2:])
    with open('to_do', "w+") as f:
        for k, v in to_do_dct.items():
            l = "{0}: {1}\n".format(k, v)
            f.write(l)

elif 'delete' or 'remove' in sys.argv:
    num = sys.argv[2:]
    for i in to_do_lst:
        if i[0] == num:
            to_do_lst.remove(i)
    with open('to_do', "w+") as f:
        doc = f.read()
        to_do_str = str(to_do_lst)[2:-2]
        f.write(to_do_str)
        f.write('\n')

elif 'print' in sys.argv:
    with open('to_do', "w+") as f:
        doc = f.read()
        print doc

else:
    print "please entre a valid command."



