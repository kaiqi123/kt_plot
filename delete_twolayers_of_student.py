import matplotlib.pyplot as plt
from readData import *

# original,interval 10
original_interval_10 = save_data_to_list(read_data("interval/original_interval_10"))
print("original_interval_10: " + str(caculate_convergence_time(original_interval_10)))
plt.plot(original_interval_10, label="original_interval_10")

# original,interval 1
original_dependent_student = save_data_to_list(read_data("interval/original_dependent_student"))
print("original_dependent_student: " + str(caculate_convergence_time(original_dependent_student)))
plt.plot(original_dependent_student, label="original_dependent_student")

# original,interval 1
original_interval_1 = save_data_to_list(read_data("interval/original_interval_1"))
print("original_interval_1: " + str(caculate_convergence_time(original_interval_1)))
plt.plot(original_interval_1, label="original_interval_1")

plt.legend()
plt.show()