def add_and_sorted_dict(word_count, full_list):
    dict1={}
    for t in range(1, word_count+1):
        prioritet= full_list[t].find(' ')
        dict1.setdefault(int(full_list[t][prioritet+1:-1]),[]).append(full_list[t][:prioritet])

    sorted_dict = dict(sorted(dict1.items(), reverse = True, key=lambda x: x[0]))
    return sorted_dict

def print_result(word_count, number_of_options, sorted_dict):
    for index_element in range(word_count+2, word_count+number_of_options+2):
        list_result=[]
        for priority_value in sorted_dict:
            #сортировка внутри списка значений
            sorted_list_elements = sorted(sorted_dict[priority_value])
            for element_from_priority_value in sorted_list_elements:
                for input_size in range(len(full_list[index_element])):
                    if full_list[index_element][input_size] == element_from_priority_value[input_size]:
                        if len(list_result)<10:
                            if element_from_priority_value in list_result:
                                pass
                            else:
                                list_result.append(element_from_priority_value)    
                    else:
                        if full_list[index_element][input_size]=='\n':
                            break
                        elif element_from_priority_value in list_result:
                            list_result.remove(element_from_priority_value)
                            break
                        else:
                            break
        print('\n'. join(list_result), '\n')

if __name__ == '__main__':
    full_list = open('static.txt').readlines()
    word_count=int(full_list[0]) #Сколько слов обработано (N)
    number_of_options=int(full_list[word_count+1]) # Сколько совпадений нужно проверить(M)

    sorted_dict=add_and_sorted_dict(word_count, full_list) #Получение отсортированного словаря 
    print_result(word_count, number_of_options, sorted_dict) 