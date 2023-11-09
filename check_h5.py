# import numpy as np
# np.load('nnot.h5',allow_pickle=True)

import h5py
# filename = "annot.h5"
filename = "/data/human36m/extra/una-dinosauria-data/h36m/S1/MyPoses/3D_positions/Directions 1.h5"

import h5py

def explore_h5_file(file_path, indent=0):
    with h5py.File(file_path, 'r') as file:
        for name in file:
            item = file[name]
            if isinstance(item, h5py.Group):
                print(' ' * indent + f'Group: {name}/')
                explore_h5_file(file_path + '/' + name, indent + 4)
            elif isinstance(item, h5py.Dataset):
                print(' ' * indent + f'Dataset: {name} (shape={item.shape}, dtype={item.dtype})')

# Replace 'your_file.h5' with the path to your .h5 file
# explore_h5_file(filename)



with h5py.File(filename, "r") as f:
    print("Keys: %s" % list(f.keys()))
    # get first object name/key; may or may NOT be a group
    a_group_key = list(f.keys())[0]
    # get the object type for a_group_key: usually group or dataset
    print(type(f[a_group_key]))

    print(f['3D_positions'])