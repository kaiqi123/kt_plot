import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher,0.01
teacher = save_data_to_list(read_data("cifar10_results/teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

#dependent_student,0.001
path="cifar10_results/Dependent_student_learning_rate_0.001/"

#dependent_student_conv2_fc1
dependent_student_conv2_fc1 = save_data_to_list(read_data(path+"conv2_fc1"))
print("dependent_student_conv2_fc1: " + str(caculate_convergence_time(dependent_student_conv2_fc1)))
#plt.plot(dependent_student_conv2_fc1, label="dependent_student_conv2_fc1")

#dependent_student_conv2_fc1, add softmax
dependent_student_conv2_fc1_softmax = save_data_to_list(read_data(path+"conv2_fc1_softmax"))
print("dependent_student_conv2_fc1_softmax: " + str(caculate_convergence_time(dependent_student_conv2_fc1_softmax)))
#plt.plot(dependent_student_conv2_fc1_softmax, label="dependent_student_conv2_fc1_softmax")

#dependent_student_conv3_fc1
dependent_student_conv3_fc1 = save_data_to_list(read_data(path+"conv3_fc1"))
print("dependent_student_conv3_fc1: " + str(caculate_convergence_time(dependent_student_conv3_fc1)))
plt.plot(dependent_student_conv3_fc1, label="dependent_student_conv3_fc1")

#dependent_student_conv3_fc1, add softmax
dependent_student_conv3_fc1_softmax = save_data_to_list(read_data(path+"conv3_fc1_softmax"))
print("dependent_student_conv3_fc1_softmax: " + str(caculate_convergence_time(dependent_student_conv3_fc1_softmax)))
plt.plot(dependent_student_conv3_fc1_softmax, label="dependent_student_conv3_fc1_softmax")

#dependent_student_conv4_fc1
dependent_student_conv4_fc1 = save_data_to_list(read_data(path+"conv4_fc1"))
print("dependent_student_conv4_fc1: " + str(caculate_convergence_time(dependent_student_conv4_fc1)))
#plt.plot(dependent_student_conv4_fc1, label="dependent_student_conv4_fc1")

#dependent_student_conv4_fc1, new method
dependent_student_conv4_fc1_new = save_data_to_list(read_data(path+"conv4_fc1_newMethod"))
print("dependent_student_conv4_fc1_new: " + str(caculate_convergence_time(dependent_student_conv4_fc1_new)))
#plt.plot(dependent_student_conv4_fc1_new, label="dependent_student_conv4_fc1(new method)")

#dependent_student_conv5_fc2
dependent_student_conv5_fc2 = save_data_to_list(read_data(path+"conv5_fc2"))
print("dependent_student_conv5_fc2: " + str(caculate_convergence_time(dependent_student_conv5_fc2)))
#plt.plot(dependent_student_conv5_fc2, label="dependent_student_conv5_fc2")

#dependent_student_conv5_fc2, new method
dependent_student_conv5_fc2 = save_data_to_list(read_data(path+"conv5_fc2_newMethod"))
print("dependent_student_conv5_fc2: " + str(caculate_convergence_time(dependent_student_conv5_fc2)))
#plt.plot(dependent_student_conv5_fc2, label="dependent_student_conv5_fc2(new method)")

#independent_student
path="cifar10_results/indepentStudent_lerning_rate_0.001/"

#independent_student_conv2_fc1
independent_student_conv2_fc1_new = save_data_to_list(read_data(path+"independent_student_conv2_fc1_0.001"))
print("independent_student_conv2_fc1_new: " + str(caculate_convergence_time(independent_student_conv2_fc1_new)))
#plt.plot(independent_student_conv2_fc1_new, label="independent_student_conv2_fc1")

#independent_student_conv3_fc1
independent_student_conv3_fc1_new = save_data_to_list(read_data(path+"independent_student_conv3_fc1_0.001"))
print("independent_student_conv3_fc1_new: " + str(caculate_convergence_time(independent_student_conv3_fc1_new)))
plt.plot(independent_student_conv3_fc1_new, label="independent_student_conv3_fc1")

#independent_student_conv4_fc1
independent_student_conv4_fc1_new = save_data_to_list(read_data(path+"independent_student_conv4_fc1_0.001"))
print("independent_student_conv4_fc1_new: " + str(caculate_convergence_time(independent_student_conv4_fc1_new)))
#plt.plot(independent_student_conv4_fc1_new, label="independent_student_conv4_fc1")

#independent_student_conv5_fc2
independent_student_conv5_fc2 = save_data_to_list(read_data(path+"independent_student_conv5_fc2_0.001"))
print("independent_student_conv5_fc2: " + str(caculate_convergence_time(independent_student_conv5_fc2)))
#plt.plot(independent_student_conv5_fc2, label="independent_student_conv5_fc2")

#plt.title("Cifar10: Dependent Student---conv5_fc2 (lerning rate: 0.001)")
#plt.title("Cifar10: Dependent Student---conv4_fc1 (lerning rate: 0.001)")
#plt.title("Cifar10: Dependent Student---conv3_fc1 (lerning rate: 0.001)")
plt.title("Cifar10: Dependent Student---conv2_fc1 (lerning rate: 0.001)")

plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()