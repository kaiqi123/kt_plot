import matplotlib.pyplot as plt
from readData import *

# method 1
# connect every time, add initialization
interval_1_add_initialization = save_data_to_list(read_data("method1_interval/interval_1_add_initialization"))
print("connect every time(add initialization): " + str(caculate_convergence_time(interval_1_add_initialization)))
plt.plot(interval_1_add_initialization, label="connect every time(add initialization)")

# connect every time, not initialization
interval_1_not_initialization = save_data_to_list(read_data("method1_interval/interval_1_not_initialization"))
#print("connect every time(not initialization): " + str(caculate_convergence_time(interval_1_not_initialization)))
#plt.plot(interval_1_not_initialization, label="connect every time(not initialization)")

# interval 10, add initialization
interval_10_add_initialization = save_data_to_list(read_data("method1_interval/interval_10_add_initialization"))
print("interval 10 (add initialization): " + str(caculate_convergence_time(interval_10_add_initialization)))
plt.plot(interval_10_add_initialization, label="interval: 10 (add initialization)")

# interval 10, not initialization
interval_10_not_initialization = save_data_to_list(read_data("method1_interval/interval_10_not_initialization"))
#print("interval 10 (not initialization): " + str(caculate_convergence_time(interval_10_not_initialization)))
#plt.plot(interval_10_not_initialization, label="interval: 10 (not initialization)")

# interval 10, not initialization
interval_10_add_initialization_newlayers = save_data_to_list(read_data("method1_interval/interval_10_add_initialization_newlayers"))
#print("interval 10 (add initialization, newlayers): " + str(caculate_convergence_time(interval_10_add_initialization_newlayers)))
#plt.plot(interval_10_add_initialization_newlayers, label="interval: 10 (add initialization, newlayers)")

# connect once, add initialization
interval_23400_add_initialization = save_data_to_list(read_data("method1_interval/interval_23400_add_initialization"))
print("connect once at the beginning (add initialization): " + str(caculate_convergence_time(interval_23400_add_initialization)))
plt.plot(interval_23400_add_initialization, label="connect once at the beginning (add initialization)")

# connect once, not initialization
interval_23400_not_initialization = save_data_to_list(read_data("method1_interval/interval_23400_not_initialization"))
#print("connect once at the beginning (not initialization): " + str(caculate_convergence_time(interval_23400_not_initialization)))
#plt.plot(interval_23400_not_initialization, label="connect once at the beginning (not initialization)")

# independent_student, add initialization
independent_student_add_initialization = save_data_to_list(read_data("method1_interval/independent_student_add_initialization"))
#print("independent_student_add_initialization: " + str(caculate_convergence_time(independent_student_add_initialization)))
#plt.plot(independent_student_add_initialization, label="independent_student_add_initialization")

# independent_student, not initialization
independent_student_not_initialization = save_data_to_list(read_data("method1_interval/independent_student_not_initialization"))
#print("independent_student_not_initialization: " + str(caculate_convergence_time(independent_student_not_initialization)))
#plt.plot(independent_student_not_initialization, label="independent_student_not_initialization")

# dependent_student, add initialization, connect_first_234iterations
connect_first_234iterations_add_initialization = save_data_to_list(read_data("method1_interval/connect_first_234iterations_add_initialization"))
#print("connect_first_234iterations_add_initialization: " + str(caculate_convergence_time(connect_first_234iterations_add_initialization)))
#plt.plot(connect_first_234iterations_add_initialization, label="connect_first_234iterations_add_initialization")

# dependent_student, add initialization, connect_first_468iterations
connect_first_468iterations_add_initialization = save_data_to_list(read_data("method1_interval/connect_first_468iterations_add_initialization"))
#print("connect_first_234iterations_add_initialization: " + str(caculate_convergence_time(connect_first_468iterations_add_initialization)))
#plt.plot(connect_first_468iterations_add_initialization, label="connect_first_468iterations_add_initialization")


plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()