import matplotlib.pyplot as plt
from readData import *


#dependent_student,0.001
path="cifar10_results/Dependent_student_learning_rate_0.001/"


#dependent_student_conv4_fc1
dependent_student_conv4_fc1_1epoch = save_data_to_list(read_data(path+"conv4_fc1_1epoch"))
print("dependent_student_conv4_fc1_1epoch: " + str(caculate_convergence_time(dependent_student_conv4_fc1_1epoch)))
plt.plot(dependent_student_conv4_fc1_1epoch, label="dependent_student_conv4_fc1_1epoch")

#dependent_student_conv4_fc1, new method
dependent_student_conv4_fc1_new_1epoch = save_data_to_list(read_data(path+"conv4_fc1_newMethod_1epoch"))
print("dependent_student_conv4_fc1_new_1epoch: " + str(caculate_convergence_time(dependent_student_conv4_fc1_new_1epoch)))
plt.plot(dependent_student_conv4_fc1_new_1epoch, label="dependent_student_conv4_fc1_new_1epoch(new method)")


plt.xlabel("iteration")
plt.ylabel("accuracy")
plt.legend().draggable()
plt.show()