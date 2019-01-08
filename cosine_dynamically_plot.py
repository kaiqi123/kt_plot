
import matplotlib.pyplot as plt
from readData import *

# dependent student
# origin, interval 10, not initialization
interval_10_not_initialization = save_data_to_list(read_data("method1_interval/interval_10_not_initialization"))
print("interval 10 (not initialization): " + str(caculate_convergence_time(interval_10_not_initialization)))
plt.plot(interval_10_not_initialization, label="interval: 10 (not initialization)")

# dynamic cosine similarity, interval 10, not initialization
new_interval_10_not_initialization = save_data_to_list(read_data("cosine_dynamically/interval_10_not_initialization"))
print("new interval 10 (not initialization): " + str(caculate_convergence_time(new_interval_10_not_initialization)))
plt.plot(new_interval_10_not_initialization, label="interval: 10 (not initialization, new)")

# dynamic cosine similarity, interval 10, add initialization
new_interval_10_add_initialization = save_data_to_list(read_data("cosine_dynamically/interval_10_add_initialization"))
print("new interval 10 (add initialization): " + str(caculate_convergence_time(new_interval_10_add_initialization)))
#plt.plot(new_interval_10_add_initialization, label="interval: 10 (add initialization, new)")

# origin, interval 10, add initialization
interval_10_add_initialization = save_data_to_list(read_data("method1_interval/interval_10_add_initialization"))
print("interval 10 (add initialization): " + str(caculate_convergence_time(interval_10_add_initialization)))
#plt.plot(interval_10_add_initialization, label="interval: 10 (add initialization)")

# dynamic cosine similarity, connect every time, not initialization
new_connectEveryTime_not_initialiation = save_data_to_list(read_data("cosine_dynamically/connectEveryTime_not_initialiation"))
print("new connectEveryTime (not initialization): " + str(caculate_convergence_time(new_connectEveryTime_not_initialiation)))
#plt.plot(new_connectEveryTime_not_initialiation, label="connect every time(not initialization, new)")

# origin, connect every time, not initialization
interval_1_not_initialization = save_data_to_list(read_data("method1_interval/interval_1_not_initialization"))
print("connect every time(not initialization): " + str(caculate_convergence_time(interval_1_not_initialization)))
#plt.plot(interval_1_not_initialization, label="connect every time(not initialization)")


plt.title("Dependent Student")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()