import os, shutil

base = os.path.dirname(os.path.abspath(__file__))
original_dataset_dir = os.path.join(base, 'Dataset')
folder_name = {"rock": 0, "scissor": 2, "paper": 5}

for key in folder_name.keys():
    print(folder_name[key])

    files = os.listdir(original_dataset_dir + "/" + str(folder_name[key]) + "/")

    for i in range(0, len(files)):
        print(files[i])
        extension = os.path.splitext(files[i])
        if extension == ".png" or ".jpeg" or ".jpg":
            shutil.move(original_dataset_dir + "/" + str(folder_name[key]) + "/" + files[i], original_dataset_dir + "/" + key + "/" + key + "_" + str(i) + ".jpg")