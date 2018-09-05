import os
path = os.getcwd()
print([i for i in os.listdir() if not os.path.isdir(i)])
# with open(i, 'r') as f:
#     print

dir_path = os.path.join(path, 'Nmae_dir')
print('123')