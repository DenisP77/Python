



def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so skip them
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                #arr[j], arr[j + 1] = arr[j + 1], arr[j]
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

def count_occurrences(arr):
    occurrence_dict = {}
    for num in arr:
        if num in occurrence_dict:
            occurrence_dict[num] += 1
        else:
            occurrence_dict[num] = 1
    return occurrence_dict

def add_elements_to_the_dic(arr):
    occurrence_dict = {}
    for key in arr:
        occurrence_dict[key] = 1
    return occurrence_dict

def main():
    example_list = [64, 34, 64, 25, 9, 34, 90, 11, 12, 22, 11, 11, 9, 56, 8, 11, 90, 9]
    print("Original list:", example_list)
    sorted_list = bubble_sort(example_list)
    print("Sorted list:", sorted_list)
    occurrences = count_occurrences(sorted_list)
    for key, count in occurrences.items():
        print(f"The number {key} appears {count} {'time' if count == 1 else 'times'}")

    single_dictionary = add_elements_to_the_dic(sorted_list)
    print("\nsingle_occurrences dictionary:" , single_dictionary);


if __name__ == "__main__":
    main()
