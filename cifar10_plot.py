import matplotlib.pyplot as plt
from readData import *

# cifar10

# teacher
teacher = save_data_to_list(read_data("cifar10_results/teacher"))
print("teacher: " + str(caculate_convergence_time(teacher)))
plt.plot(teacher, label="teacher")


#plt.title("Dependent Student")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()