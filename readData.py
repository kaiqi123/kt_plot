def read_data(file_name):
    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    return data


def save_data_to_list(original_data):
    data = []
    for sentence in original_data:
        list_temp = str(sentence).strip().strip(' ').split(',')
        for item in list_temp:
            if item:
                data.append(float(item))
    return data


def caculate_convergence_time(data):
    max_num = max(data)
    #max_num = 0.7781
    iteration = 0
    for i in range(len(data)):
        #if data[i] == max_num:
        if data[i] >= max_num * 0.9:
            iteration = i
            break
    return iteration,max_num