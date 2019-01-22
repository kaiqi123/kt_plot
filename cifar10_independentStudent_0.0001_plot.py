import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher,0.01
teacher = save_data_to_list(read_data("cifar10_results/teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

#independent_student,0.0001
path="cifar10_results/indepentStudent_lerning_rate_0.0001/"

#independent_student_conv1_fc1
independent_student_conv1_fc1 = save_data_to_list(read_data(path+"independent_student_conv1_fc1"))
print("independent_student_conv1_fc1: " + str(caculate_convergence_time(independent_student_conv1_fc1)))
plt.plot(independent_student_conv1_fc1, label="independent_student_conv1_fc1")

#independent_student_conv2_fc1
independent_student_conv2_fc1 = save_data_to_list(read_data(path+"independent_student_conv2_fc1"))
print("independent_student_conv2_fc1: " + str(caculate_convergence_time(independent_student_conv2_fc1)))
plt.plot(independent_student_conv2_fc1, label="independent_student_conv2_fc1")

#independent_student_conv3_fc1
independent_student_conv3_fc1 = save_data_to_list(read_data(path+"independent_student_conv3_fc1"))
print("independent_student_conv3_fc1: " + str(caculate_convergence_time(independent_student_conv3_fc1)))
plt.plot(independent_student_conv3_fc1, label="independent_student_conv3_fc1")

#independent_student_conv4_fc1
independent_student_conv4_fc1 = save_data_to_list(read_data(path+"independent_student_conv4_fc1"))
print("independent_student_conv4_fc1: " + str(caculate_convergence_time(independent_student_conv4_fc1)))
plt.plot(independent_student_conv4_fc1, label="independent_student_conv4_fc1")

#independent_student_conv5_fc1
independent_student_conv5_fc2 = save_data_to_list(read_data(path+"independent_student_conv5_fc2"))
print("independent_student_conv5_fc2: " + str(caculate_convergence_time(independent_student_conv5_fc2)))
plt.plot(independent_student_conv5_fc2, label="independent_student_conv5_fc2")

plt.title("Cifar10: Independent Student")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()