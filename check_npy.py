# 각 Subject에 대한 각 Action들의 BBOX 개수가 30개(Action 종류)로 동일한지 체크
# 결과: S6, S9는 29개로 이미지 개수조차 동일한 Action이 존재

import numpy as np

data_npy = np.load('C:/Users/User/github/learnable-triangulation-pytorch/data/human36m/extra/bboxes-Human36M-GT_.npy', allow_pickle=True).item()

subject_list = list(data_npy.keys())
action_list = list(data_npy['S1'].keys())

camera_list = list(data_npy['S1']['TakingPhoto-1'].keys())

total_bbox_num = 0
for subject in subject_list:
    check_npy = []
    for action in action_list:
        for camera in camera_list:
            num_images = len(data_npy[subject][action][camera])
            check_npy.append(num_images)
    rm_check_npy = list(set(check_npy))
    total_bbox_num += sum(check_npy)
    if len(rm_check_npy) == 30:
        print(f'The number of {subject} bboxes: {sum(check_npy)}')
    else:
        print(f'The number of {subject} bboxes: {sum(check_npy)}')
print(f'The number of total bboxes: {total_bbox_num}')

'''
The number of S9 bboxes: 317668 / img: 317668
The number of S5 bboxes: 396316 / img: 396316
***The number of S11 bboxes: 232976 / img: 231151(1825?)
The number of S7 bboxes: 406484 / img: 406484
The number of S6 bboxes: 249864 / img: 249864
The number of S8 bboxes: 258712 / img: 258712
The number of S1 bboxes: 248376 / img: 248376
The number of total bboxes: 2110396 / img: 2108571
'''