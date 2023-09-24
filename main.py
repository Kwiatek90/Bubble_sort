import time 

def bubble_sort(sorting_list):
    number_of_sorted_numbers = 1
    while number_of_sorted_numbers > 0:
        number_of_sorted_numbers = 0
        for i in range(len(sorting_list) - 1):
            if sorting_list[i] > sorting_list[i + 1]:
                cookie_sort = sorting_list[i]
                sorting_list[i] = sorting_list[i + 1]
                sorting_list[i + 1] = cookie_sort
                number_of_sorted_numbers += 1
    return sorting_list
                

#lists to test
sort_lists = [
    [],
    [1,2,5,3,1,7,9,1,12,83,1,5,3,2],
    [1,1,1,1,1,1,1,2,1,1,1],
    [2,2,2,2],
    [1,2],
    [2,1]
    ]            


for i in range(len(sort_lists)):
    print(f"List to sort:{sort_lists[i]}, Sorted list: {bubble_sort(sort_lists[i])}")    
    time.sleep(1)
