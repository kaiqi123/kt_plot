import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher,0.01
teacher = save_data_to_list(read_data("cifar10_results/teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

#independent_student,0.001
path="cifar10_results/indepentStudent_lerning_rate_0.001/"

#independent_student_conv6_fc3
independent_student_conv6_fc3 = save_data_to_list(read_data(path+"independent_student_conv6_fc3_0.001"))
print("independent_student_conv6_fc3: " + str(caculate_convergence_time(independent_student_conv6_fc3)))
plt.plot(independent_student_conv6_fc3, label="independent_student_conv6_fc3")

#independent_student_conv5_fc2
independent_student_conv5_fc2 = save_data_to_list(read_data(path+"independent_student_conv5_fc2_0.001"))
print("independent_student_conv5_fc2: " + str(caculate_convergence_time(independent_student_conv5_fc2)))
plt.plot(independent_student_conv5_fc2, label="independent_student_conv5_fc2")

#independent_student_conv4_fc1
independent_student_conv4_fc1_new = save_data_to_list(read_data(path+"independent_student_conv4_fc1_0.001"))
print("independent_student_conv4_fc1_new: " + str(caculate_convergence_time(independent_student_conv4_fc1_new)))
plt.plot(independent_student_conv4_fc1_new, label="independent_student_conv4_fc1")

#independent_student_conv3_fc1
independent_student_conv3_fc1_new = save_data_to_list(read_data(path+"independent_student_conv3_fc1_0.001"))
print("independent_student_conv3_fc1_new: " + str(caculate_convergence_time(independent_student_conv3_fc1_new)))
plt.plot(independent_student_conv3_fc1_new, label="independent_student_conv3_fc1")

#independent_student_conv2_fc1
independent_student_conv2_fc1_new = save_data_to_list(read_data(path+"independent_student_conv2_fc1_0.001"))
print("independent_student_conv2_fc1_new: " + str(caculate_convergence_time(independent_student_conv2_fc1_new)))
plt.plot(independent_student_conv2_fc1_new, label="independent_student_conv2_fc1")

#independent_student_conv1_fc1
independent_student_conv1_fc1_new = save_data_to_list(read_data(path+"independent_student_conv1_fc1_0.001"))
print("independent_student_conv1_fc1_new: " + str(caculate_convergence_time(independent_student_conv1_fc1_new)))
plt.plot(independent_student_conv1_fc1_new, label="independent_student_conv1_fc1")

plt.title("Cifar10: Independent Student, Learning Rate 0.001")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()