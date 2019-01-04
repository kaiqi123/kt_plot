import matplotlib.pyplot as plt
from readData import *

# 80_percent_of_every_category_dependent_student
dependent_student_80_percent_of_every_category = save_data_to_list(read_data("subset/80_percent_of_every_category_dependent_student"))
print("dependent_student_80_percent_of_every_category: " + str(caculate_convergence_time(dependent_student_80_percent_of_every_category)))
#plt.plot(dependent_student_80_percent_of_every_category, label="dependent student, 80_percent_of_every_category")

# 80_percent_of_every_category_dependent_student
independent_student_80_percent_of_every_category = save_data_to_list(read_data("subset/80_percent_of_every_category_independent_student"))
print("independent_student_80_percent_of_every_category: " + str(caculate_convergence_time(independent_student_80_percent_of_every_category)))
plt.plot(independent_student_80_percent_of_every_category, label="independent student, 80_percent_of_every_category")

# 83_categories_dependent_student
dependent_student_83_categories = save_data_to_list(read_data("subset/83_categories_dependent_student"))
print("dependent_student_83_categories: " + str(caculate_convergence_time(dependent_student_83_categories)))
#plt.plot(dependent_student_83_categories, label="dependent student, 83_categories")

# 83_categories_independent_student
independent_student_83_categories = save_data_to_list(read_data("subset/83_categories_independent_student"))
print("independent_student_83_categories: " + str(caculate_convergence_time(independent_student_83_categories)))
plt.plot(independent_student_83_categories, label="independent_student_83_categories")

# complete set, dependent student
interval_1 = save_data_to_list(read_data("method1_interval/interval_1"))
print("connect every time: " + str(caculate_convergence_time(interval_1)))
#plt.plot(interval_1, label="dependent student, complete set")

# complete set, independent_student
independent_student = save_data_to_list(read_data("method1_interval/independent_student"))
print("independent_student: " + str(caculate_convergence_time(independent_student)))
plt.plot(independent_student, label="independent_student, complete set")

plt.legend()
plt.show()