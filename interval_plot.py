import matplotlib.pyplot as plt
from readData import *

# interval 1
interval_1 = save_data_to_list(read_data("interval/interval_1"))
print("connect every time: " + str(caculate_convergence_time(interval_1)))
plt.plot(interval_1, label="connect every time")

# interval 10
interval_10 = save_data_to_list(read_data("interval/interval_10"))
print("interval 10: " + str(caculate_convergence_time(interval_10)))
plt.plot(interval_10, label="interval: 10")

# interval once
interval_23400 = save_data_to_list(read_data("interval/interval_23400"))
print("connect once at the beginning: " + str(caculate_convergence_time(interval_23400)))
plt.plot(interval_23400, label="connect once at the beginning")

# independent_student
independent_student = save_data_to_list(read_data("interval/independent_student"))
print("independent_student: " + str(caculate_convergence_time(independent_student)))
plt.plot(independent_student, label="independent_student")


plt.legend()
plt.show()