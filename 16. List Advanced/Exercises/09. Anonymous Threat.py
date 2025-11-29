def merge(some_list:list, current_command:list) -> list:
    start_index, end_index = int(current_command[1]), int(current_command[2])
    if start_index not in range(len(some_list)):
        start_index = 0
    if end_index not in range(len(some_list)):
        end_index = len(some_list)
    some_list[start_index] = ''.join(some_list[start_index: end_index + 1])
    some_list = some_list[:start_index + 1] + some_list[end_index + 1:]
    return some_list

def divide(some_list:list, current_command:list) -> list:
    index, partitions = int(current_command[1]), int(current_command[2])
    element = some_list[index]
    partition_size = len(element) // partitions
    partitioned_element = []
    nr_partition = 0
    for current_index in range(0, len(element), partition_size):
        nr_partition += 1
        if nr_partition == partitions:
            current_partition = element[current_index:]
            partitioned_element.append(current_partition)
            break
        else:
            current_partition = element[current_index:current_index + partition_size]
            partitioned_element.append(current_partition)
    some_list = some_list[:index] + partitioned_element + some_list[index + 1:]
    return some_list

input_array = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]
    if action == "merge":
        input_array = merge(input_array, command)
    elif action == "divide":
        input_array = divide(input_array, command)

    command = input()

print(' '.join(input_array))
