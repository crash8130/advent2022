import pathlib  
work_dir = pathlib.Path.cwd()
path =  'example.txt'
f = open(path, 'r')

data_array = []
for i in f:
    data_array.append(i.strip())


check_data = data_array[0:3]

def count_chars(data):
    