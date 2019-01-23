import matplotlib.pyplot as plt
from readData import *

#caltech101

# teacher
teacher = save_data_to_list(read_data("teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

# independent_student, not initialization, 5 conv + 2 fc
independent_student_not_initialization = save_data_to_list(read_data("method1_interval/independent_student_not_initialization"))
print("independent_student: " + str(caculate_convergence_time(independent_student_not_initialization)))
plt.plot(independent_student_not_initialization, label="independent_student(5 conv + 2 fc)")

path = "delete_student_layers/independentStudent/"
# independent_student, not initialization, 4 conv + 1 fc
conv4_fc1 = save_data_to_list(read_data(path+"conv4_fc1"))
print("independent_student(4 conv + 1 fc): " + str(caculate_convergence_time(conv4_fc1)))
plt.plot(conv4_fc1, label="independent_student(4 conv + 1 fc)")

# independent_student, not initialization, 3 conv + 1 fc
conv3_fc1 = save_data_to_list(read_data(path+"conv3_fc1"))
print("independent_student(3 conv + 1 fc): " + str(caculate_convergence_time(conv3_fc1)))
plt.plot(conv3_fc1, label="independent_student(3 conv + 1 fc)")

# independent_student, not initialization, 2 conv + 1 fc
conv2_fc1 = save_data_to_list(read_data(path+"conv2_fc1"))
print("independent_student(2 conv + 1 fc): " + str(caculate_convergence_time(conv2_fc1)))
#plt.plot(conv2_fc1, label="independent_student(2 conv + 1 fc)")

# independent_student, not initialization, 1 conv + 1 fc
conv1_fc1 = save_data_to_list(read_data(path+"conv1_fc1"))
print("independent_student(1 conv + 1 fc): " + str(caculate_convergence_time(conv1_fc1)))
#plt.plot(conv1_fc1, label="independent_student(1 conv + 1 fc)")

# independent_student, not initialization, 1 fc
fc1 = save_data_to_list(read_data(path+"1fc"))
#print("independent_student(2): " + str(caculate_convergence_time(fc1)))
#plt.plot(fc1, label="independent_student(1 fc)")

# dependent_student, connect every time, add initialization, 5 conv + 2 fc
interval_1_add_initialization = save_data_to_list(read_data("method1_interval/interval_1_add_initialization"))
print("dependent_student(5 conv + 2 fc): " + str(caculate_convergence_time(interval_1_add_initialization)))
plt.plot(interval_1_add_initialization, label="dependent_student(5 conv + 2 fc)")

path = "delete_student_layers/DependentStudent/"

# dependent_student, add initialization, 3 conv + 1 fc
dependent_student_conv3_fc1 = save_data_to_list(read_data(path+"conv3_fc1"))
print("dependent_student(3 conv + 1 fc): " + str(caculate_convergence_time(dependent_student_conv3_fc1)))
plt.plot(dependent_student_conv3_fc1, label="dependent_student(3 conv + 1 fc)")

# dependent_student, add initialization, 4 conv + 1 fc
dependent_student_conv4_fc1 = save_data_to_list(read_data(path+"conv4_fc1"))
print("dependent_student(4 conv + 1 fc): " + str(caculate_convergence_time(dependent_student_conv4_fc1)))
plt.plot(dependent_student_conv4_fc1, label="dependent_student(4 conv + 1 fc)")

plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()