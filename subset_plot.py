import matplotlib.pyplot as plt
from readData import *

def dependent_student_plot():

    # 80_percent_of_every_category_dependent_student(1829)
    dependent_student_80_percent_of_every_category = save_data_to_list(read_data("subset/80_percent_of_every_category_dependent_student"))
    print("dependent_student_80_percent_of_every_category: " + str(caculate_convergence_time(dependent_student_80_percent_of_every_category)))
    #plt.plot(dependent_student_80_percent_of_every_category, label="80_percent_of_every_category(1829)")

    # 73_categories_dependent_student, test dataset 102 categories(1829)
    dependent_student_73_categories_test102 = save_data_to_list(read_data("subset/73_categories_dependent_student_test102"))
    print("dependent_student_73_categories_test102: " + str(caculate_convergence_time(dependent_student_73_categories_test102)))
    #plt.plot(dependent_student_73_categories_test102, label="73_categories, test dataset 102 categories(1829)")

    # 73_categories_dependent_student, test dataset 73 categories(1478)
    dependent_student_73_categories_test73 = save_data_to_list(read_data("subset/73_categories_dependent_student_test73"))
    print("dependent_student_73_categories_test73: " + str(caculate_convergence_time(dependent_student_73_categories_test73)))
    #plt.plot(dependent_student_73_categories_test73, label="73_categories, test dataset 73 categories(1478)")

    # 73_categories_dependent_student, test dataset 29 categories(351)
    dependent_student_73_categories_test29 = save_data_to_list(read_data("subset/73_categories_dependent_student_test29"))
    print("dependent_student_73_categories_test29: " + str(caculate_convergence_time(dependent_student_73_categories_test29)))
    plt.plot(dependent_student_73_categories_test29, label="73_categories, test dataset 29 categories(351)")

    # 73_categories_dependent_student, test dataset 29 categories(351), delete student train itself
    dependent_student_73_categories_test29_deleteStudentTrainItself = save_data_to_list(read_data("subset/73_categories_dependent_student_test29_deleteStudentTrainItself"))
    print("dependent_student_73_categories_test29: " + str(caculate_convergence_time(dependent_student_73_categories_test29_deleteStudentTrainItself)))
    plt.plot(dependent_student_73_categories_test29_deleteStudentTrainItself, label="73_categories, test dataset 29 categories(351), \ndelete student train itself")

    # complete set, dependent student
    interval_1 = save_data_to_list(read_data("method1_interval/interval_1_add_initialization"))
    print("connect every time: " + str(caculate_convergence_time(interval_1)))
    #plt.plot(interval_1, label="complete set(1829)")

    plt.title("Dependent Student")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.legend().draggable()
    plt.show()

dependent_student_plot()
# 80_percent_of_every_category_dependent_student
# independent_student_80_percent_of_every_category = save_data_to_list(read_data("subset/80_percent_of_every_category_independent_student"))
# print("independent_student_80_percent_of_every_category: " + str(caculate_convergence_time(independent_student_80_percent_of_every_category)))
# plt.plot(independent_student_80_percent_of_every_category, label="independent student, 80_percent_of_every_category")

# 83_categories_independent_student
#independent_student_83_categories = save_data_to_list(read_data("subset/83_categories_independent_student"))
#print("independent_student_83_categories: " + str(caculate_convergence_time(independent_student_83_categories)))
#plt.plot(independent_student_83_categories, label="independent_student_83_categories")

# complete set, independent_student
#independent_student = save_data_to_list(read_data("method1_interval/independent_student_not_initialization"))
#print("independent_student: " + str(caculate_convergence_time(independent_student)))
# plt.plot(independent_student, label="independent_student, complete set")