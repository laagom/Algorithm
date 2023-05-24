def solution(arr, delete_list):
    # for remove_num in delete_list:
    #     if remove_num in arr:
    #         arr.remove(remove_num)
            
    return [num for num in arr if num not in delete_list]