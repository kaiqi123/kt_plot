
import numpy as np

def change_path(oldFile, newFile):
    f = open(oldFile)
    lines = f.readlines()
    lines_new = []
    for line in lines:
        line1 = line.replace("/home/users/saman/VGG19-TF/", "./")
        lines_new.append(line1)
        # print(line1)
    print(len(lines))
    f.close()

    f = open(newFile, "w")
    f.writelines(lines_new)
    f.close()

def select_subset_of_every_category(openFile, writeFile):
    f = open(openFile)
    lines = f.readlines()

    content_dict = {}
    for i in range(102):
        content_dict[str(i)] = []

    labelValue = '0'
    for line in lines:
        label_temp = line.split(',')[0]
        content_dict[str(label_temp)].append(line)

    remain_lines = []
    for i in range(102):
        content_list = content_dict[str(i)]
        remain_size = int(len(content_list) * 1.0)
        for j in range(remain_size):
            remain_lines.append(content_list[j])

    print(len(lines))
    print(len(remain_lines))

    f = open(writeFile, "w")
    f.writelines(remain_lines)

    f.close()

def shuttle(openFile, writeFile):
    f = open(openFile)
    content = f.readlines()
    np.random.shuffle(content)

    f = open(writeFile, "w")
    f.writelines(content)

    f.close()

def create_train_and_test_dataset(openFile, trainFile, testFile):

    f = open(openFile)
    content = f.readlines()

    list_size = len(content)

    train_size = list_size * (60)
    train_size = train_size // 100

    test_size = int(list_size * 0.2)

    #print(test_size)

    train_images = content[:train_size]
    test_images = content[train_size:train_size+test_size]

    f1 = open(trainFile, "w")
    f1.writelines(train_images)

    f2 = open(testFile, "w")
    f2.writelines(test_images)

    print(list_size)
    print(train_size)
    print(test_size)
    print(list_size-train_size-test_size)

    f.close()
    f1.close()
    f2.close()

"""
change_path("caltech101/caltech101-train-old.txt", "caltech101/caltech101-train.txt")
change_path("caltech101/caltech101-test-old.txt", "caltech101/caltech101-test.txt")
change_path("caltech101/caltech101-validation-old.txt", "caltech101/caltech101-validation.txt")
change_path("caltech101/dataset-old.txt", "caltech101/dataset.txt")


select_subset_of_every_category("caltech101/dataset.txt", "caltech101/dataset_remain.txt")
shuttle("caltech101/dataset_remain.txt", "caltech101/dataset_remain_shuttle.txt")
create_train_and_test_dataset("caltech101/dataset_remain_shuttle.txt", "caltech101/caltech101-subset-train.txt", "caltech101/caltech101-subset-test.txt")

shuttle("caltech101/dataset_delete_categories.txt", "caltech101/dataset_delete_categories_shuttle.txt")
create_train_and_test_dataset("caltech101/dataset_delete_categories_shuttle.txt", "caltech101/caltech101-delete-categories-train.txt", "caltech101/caltech101-delete-categories-test.txt")
83 categories
"""

#select_subset_of_every_category("new_caltech101/caltech101-train.txt", "new_caltech101/caltech101-train-remain.txt")
#shuttle("new_caltech101/caltech101-train-remain.txt", "new_caltech101/caltech101-subset-train.txt")
#create_train_and_test_dataset("new_caltech101/dataset_remain_shuttle.txt", "new_caltech101/caltech101-subset-train.txt", "new_caltech101/caltech101-subset-test.txt")

#select_subset_of_every_category("new_caltech101/caltech101-train.txt", "new_caltech101/caltech101-delete-categories-train.txt")
#select_subset_of_every_category("new_caltech101/caltech101-test.txt", "new_caltech101/caltech101-delete-categories-test-73.txt")

#shuttle("new_caltech101/caltech101-delete-categories-train.txt", "new_caltech101/caltech101-delete-categories-train.txt")
shuttle("new_caltech101/caltech101-delete-categories-test-29.txt", "new_caltech101/caltech101-delete-categories-test-29.txt")