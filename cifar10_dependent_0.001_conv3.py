import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher,0.01
teacher = save_data_to_list(read_data("cifar10_results/teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

#dependent_student,0.001
path="cifar10_results/Dependent_student_learning_rate_0.001/"

#dependent_student_conv3_fc1
dependent_student_conv3_fc1 = save_data_to_list(read_data(path+"conv3_fc1"))
print("dependent_student_conv3_fc1: " + str(caculate_convergence_time(dependent_student_conv3_fc1)))
plt.plot(dependent_student_conv3_fc1, label="dependent_student_conv3_fc1(0.001)")

#dependent_student_conv3_fc1, add softmaxRMSE
dependent_student_conv3_fc1_softmax = save_data_to_list(read_data(path+"conv3_fc1_softmax"))
print("dependent_student_conv3_fc1_softmax: " + str(caculate_convergence_time(dependent_student_conv3_fc1_softmax)))
plt.plot(dependent_student_conv3_fc1_softmax, label="dependent_student_conv3_fc1_add_softmaxRMSE(0.001)")

#dependent_student_conv3_fc1, add softCrossentropy, add newMethod
dependent_student_conv3_fc1_softCrossentropy_newMethod = save_data_to_list(read_data(path+"conv3_fc1_softCrossentropy_newMethod"))
print("dependent_student_conv3_fc1_softCrossentropy_newMethod: " + str(caculate_convergence_time(dependent_student_conv3_fc1_softCrossentropy_newMethod)))
plt.plot(dependent_student_conv3_fc1_softCrossentropy_newMethod, label="dependent_student_conv3_fc1_add_softCrossentropy(0.001)")

#independent_student
path="cifar10_results/indepentStudent_lerning_rate_0.001/"

#independent_student_conv3_fc1
independent_student_conv3_fc1_new = save_data_to_list(read_data(path+"independent_student_conv3_fc1_0.001"))
print("independent_student_conv3_fc1_new: " + str(caculate_convergence_time(independent_student_conv3_fc1_new)))
plt.plot(independent_student_conv3_fc1_new, label="independent_student_conv3_fc1(0.001)")

#independent_student,0.0001
path="cifar10_results/indepentStudent_lerning_rate_0.0001/"

#independent_student_conv3_fc1
independent_student_conv3_fc1 = save_data_to_list(read_data(path+"independent_student_conv3_fc1"))
print("independent_student_conv3_fc1: " + str(caculate_convergence_time(independent_student_conv3_fc1)))
plt.plot(independent_student_conv3_fc1, label="independent_student_conv3_fc1(0.0001)")

#independent_student,0.0001
path="cifar10_results/indepentStudent_lerning_rate_0.0001/"

plt.title("Cifar10: Dependent Student---conv3_fc1 (lerning rate: 0.001)")

plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()