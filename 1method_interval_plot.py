import matplotlib.pyplot as plt
from readData import *

# method 1
# connect every time
interval_1 = save_data_to_list(read_data("method1_interval/interval_1"))
print("connect every time: " + str(caculate_convergence_time(interval_1)))
plt.plot(interval_1, label="connect every time")

# interval 10, add initialization
interval_10_add_initialization = save_data_to_list(read_data("method1_interval/interval_10_add_initialization"))
print("interval 10 (add initialization): " + str(caculate_convergence_time(interval_10_add_initialization)))
#plt.plot(interval_10_add_initialization, label="interval: 10 (add initialization)")

# interval 10, not initialization
interval_10_not_initialization = save_data_to_list(read_data("method1_interval/interval_10_not_initialization"))
print("interval 10 (not initialization): " + str(caculate_convergence_time(interval_10_not_initialization)))
#plt.plot(interval_10_not_initialization, label="interval: 10 (not initialization)")

# connect once, add initialization
interval_23400_add_initialization = save_data_to_list(read_data("method1_interval/interval_23400_add_initialization"))
print("connect once at the beginning (add initialization): " + str(caculate_convergence_time(interval_23400_add_initialization)))
plt.plot(interval_23400_add_initialization, label="connect once at the beginning (add initialization)")

# connect once, not initialization
interval_23400_not_initialization = save_data_to_list(read_data("method1_interval/interval_23400_not_initialization"))
print("connect once at the beginning (not initialization): " + str(caculate_convergence_time(interval_23400_not_initialization)))
plt.plot(interval_23400_not_initialization, label="connect once at the beginning (not initialization)")

# independent_student
independent_student = save_data_to_list(read_data("method1_interval/independent_student"))
print("independent_student: " + str(caculate_convergence_time(independent_student)))
plt.plot(independent_student, label="independent_student")


plt.legend()
plt.show()