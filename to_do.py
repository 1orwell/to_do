import os
import errno

import sys
to_do_dct = {}
number = 0

def create_todo_file():
    # create TODO file if one does not already exist
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

    try:
        os.open('to_do', flags)
    except OSError as e:
        if e.errno == errno.EEXIST:  # Failed as the file already exists.
            pass
        else:  # Something unexpected went wrong so reraise the exception.
            raise
    else:  # No exception, so the file must have been created successfully.
        pass

def read_file_to_dict():
    global to_do_dct
    # if no file exits print error and exit
    with open('to_do', "r") as f:
        for line in f:
            #print line,
            l = line.split(':')
            l[1] = l[1].strip()
            to_do_dct[int(l[0])] = l[1]

def find_num():
    number = 0
    keys_list = [i for i in to_do_dct.keys()]
    missing_num_list = [i+2 for i in range(len(keys_list)-1) if keys_list[i+1] - keys_list[i] != 1]
    if missing_num_list == []:
        if keys_list == []:
            number = 1
        else:
            number = int(keys_list[-1]) + 1
    else:
        number = missing_num_list[0]
    return number

def write_dict_to_file():
    with open('to_do', "w") as f:
        for k, v in to_do_dct.items():
            l = "{0}: {1}\n".format(k, v)
            f.write(l)

def update_dict():
    number = find_num()
    to_do_dct[str(number)] = ' '.join(sys.argv[2:])

def delete_a_todo(num):
    read_file_to_dict()
    if int(num) in to_do_dct.keys():
        to_do_dct.pop(num)
        write_dict_to_file()
    else:
        print "you did not entre a valid number"

#read_file_to_dict()
#write_dict_to_file()

if 'add' in sys.argv:
    read_file_to_dict()
    update_dict()
    write_dict_to_file()

if 'print' in sys.argv:
    with open('to_do', 'r') as f:
        for line in f:
            print line,

if 'delete' in sys.argv:
    delete_a_todo(int(sys.argv[-1]))
    write_dict_to_file()

