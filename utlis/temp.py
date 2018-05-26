import scipy.io as io
from pprint import pprint

class_mat = io.loadmat('../data/annotations/cars_meta')
class_name_mat= class_mat['class_names'][0]# this is array format

class_name = []
for name in class_name_mat:
    class_name.append(name[0])

for idx,name in enumerate(class_name):
    # print(str(idx)+':\''+name.split(' ')[0]+'\'')
    print('\''+name.split(' ')[0]+ '\''+': {}')

class_dict = {}

for idx, name in enumerate(class_name) :
    name = name.split(' ')[0]
    try :
        class_dict[name].append(idx)
    except:
        class_dict[name] = []
        class_dict[name].append(idx)

# pprint(class_dict)
# pprint(class)
