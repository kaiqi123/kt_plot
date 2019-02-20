import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher,0.01
teacher = save_data_to_list(read_data("resnet/teacher.txt"))
print("teacher: " + str(caculate_convergence_time(teacher)))
#plt.plot(teacher, label="teacher")

independent_student_conv1fc1 = save_data_to_list(read_data("resnet/independent_student_conv1fc1.txt"))
print("independent_student_conv1fc1: " + str(caculate_convergence_time(independent_student_conv1fc1)))
plt.plot(independent_student_conv1fc1, label="independent_student_conv1fc1")

plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()