import os, shutil

base = os.path.dirname(os.path.abspath(__file__))
original_dataset_dir = os.path.join(base, 'Dataset')
base_dir = os.path.join(base, 'preprocessed_dataset')
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')
os.mkdir(train_dir)
os.mkdir(validation_dir)
os.mkdir(test_dir)

hands_names = ["rock", "scissor", "paper"]

for h_name in hands_names:
    os.mkdir(os.path.join(train_dir, h_name))
    os.mkdir(os.path.join(validation_dir, h_name))
    os.mkdir(os.path.join(test_dir, h_name))

    file_names =  [h_name + '_{}.jpg'.format(i) for i in range(0, 100)]
    for f_name in file_names:
        src = os.path.join(original_dataset_dir, h_name, f_name)
        dst = os.path.join(train_dir, h_name, f_name)
        shutil.copyfile(src, dst)

    file_names = [h_name + '_{}.jpg'.format(i) for i in range(100, 150)]
    for f_name in file_names:
        src = os.path.join(original_dataset_dir, h_name, f_name)
        dst = os.path.join(validation_dir, h_name, f_name)
        shutil.copyfile(src, dst)

    file_names = [h_name + '_{}.jpg'.format(i) for i in range(150, 200)]
    for f_name in file_names:
        src = os.path.join(original_dataset_dir, h_name, f_name)
        dst = os.path.join(validation_dir, h_name, f_name)
        shutil.copyfile(src, dst)