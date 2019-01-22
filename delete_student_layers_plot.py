import matplotlib.pyplot as plt
from readData import *

"""
# independent_student, not initialization, 7 layers
independent_student_not_initialization = save_data_to_list(read_data("method1_interval/independent_student_not_initialization"))
print("independent_student: " + str(caculate_convergence_time(independent_student_not_initialization)))
plt.plot(independent_student_not_initialization, label="independent_student(7 layers)")

# independent_student, not initialization, 5 layers
independent_student_5layers = save_data_to_list(read_data("delete_student_layers/independent_student_5layers"))
print("independent_student(5): " + str(caculate_convergence_time(independent_student_5layers)))
plt.plot(independent_student_5layers, label="independent_student(5 layers)")

# independent_student, not initialization, 3 layers
independent_student_3layers = save_data_to_list(read_data("delete_student_layers/independent_student_3layers"))
print("independent_student(3): " + str(caculate_convergence_time(independent_student_3layers)))
plt.plot(independent_student_3layers, label="independent_student(3 layers)")
"""
# teacher
teacher = save_data_to_list(read_data("teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")

# independent_student, not initialization, 4 conv + 1 fc
conv4_fc1 = save_data_to_list(read_data("delete_student_layers/conv4_fc1"))
print("independent_student(4 conv + 1 fc): " + str(caculate_convergence_time(conv4_fc1)))
plt.plot(conv4_fc1, label="independent_student(4 conv + 1 fc)")

# independent_student, not initialization, 3 conv + 1 fc
conv3_fc1 = save_data_to_list(read_data("delete_student_layers/conv3_fc1"))
print("independent_student(3 conv + 1 fc): " + str(caculate_convergence_time(conv3_fc1)))
plt.plot(conv3_fc1, label="independent_student(3 conv + 1 fc)")

# independent_student, not initialization, 2 conv + 1 fc
conv2_fc1 = save_data_to_list(read_data("delete_student_layers/conv2_fc1"))
print("independent_student(2 conv + 1 fc): " + str(caculate_convergence_time(conv2_fc1)))
plt.plot(conv2_fc1, label="independent_student(2 conv + 1 fc)")

# independent_student, not initialization, 1 conv + 1 fc
conv1_fc1 = save_data_to_list(read_data("delete_student_layers/conv1_fc1"))
print("independent_student(1 conv + 1 fc): " + str(caculate_convergence_time(conv1_fc1)))
plt.plot(conv1_fc1, label="independent_student(1 conv + 1 fc)")

# independent_student, not initialization, 1 fc
fc1 = save_data_to_list(read_data("delete_student_layers/1fc"))
#print("independent_student(2): " + str(caculate_convergence_time(fc1)))
#plt.plot(fc1, label="independent_student(1 fc)")

plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()