import sys
to_do_lst = []

if 'add' in sys.argv:
    to_do_lst.append(' '.join(sys.argv[2:]))
    with open('to_do', "r+") as f:
        doc = f.read()
        to_do_str = str(to_do_lst)[2:-2]
        f.write(to_do_str)
        f.write('\n')

elif 'print' in sys.argv:
    with open('to_do', "r+") as f:
        doc = f.read()
        print doc

else:
    print "please entre a valid command."



