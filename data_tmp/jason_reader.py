import json # import json module

# with statement
path = "C:/Users/User/github/learnable-triangulation-pytorch/data_tmp/labels/Human36M_subject1_joint_3d.json"
with open(path) as json_file:
    json_data = json.load(json_file)

asdasd