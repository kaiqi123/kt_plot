import matplotlib.pyplot as plt
from readData import *

# origin, add two layers

# independent_student
addTwoLayers_independent_student = save_data_to_list(read_data("method1_interval/add_two_layers_independent_student"))
print("independent_student (add two layers): " + str(caculate_convergence_time(addTwoLayers_independent_student)))
plt.plot(addTwoLayers_independent_student, label="independent_student (add two layers)")

# connect once, not initialization
addTwoLayers_interval_23400 = save_data_to_list(read_data("method1_interval/add_two_layers_interval_234000"))
print("connect once at the beginning (add two layers, not initialization): " + str(caculate_convergence_time(addTwoLayers_interval_23400)))
plt.plot(addTwoLayers_interval_23400, label="connect once at the beginning (add two layers, not initialization)")

# connect once, add initialization
add_two_layers_interval_234000_addInitialization = save_data_to_list(read_data("method1_interval/add_two_layers_interval_234000_addInitialization"))
print("connect once at the beginning (add two layers, add initialization): " + str(caculate_convergence_time(add_two_layers_interval_234000_addInitialization)))
plt.plot(add_two_layers_interval_234000_addInitialization, label="connect once at the beginning (add two layers, add initialization)")

# connect every time, add initialization
add_two_layers_interval_1_add_Initialization = save_data_to_list(read_data("method1_interval/add_two_layers_interval_1_add_Initialization"))
print("connect every time (add two layers, add initialization): " + str(caculate_convergence_time(add_two_layers_interval_1_add_Initialization)))
plt.plot(add_two_layers_interval_1_add_Initialization, label="connect every time (add two layers, add initialization)")


plt.legend()
plt.show()