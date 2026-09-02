import random
import time
Start_algo_time = time.perf_counter()
end_algo_time = time.perf_counter()
time_finish = end_algo_time - Start_algo_time
def main():
    element_menu_prompt()

# Generates elements by selected amount
def genList100():
    global List100
    List100 = [random.randint(1, 100)for i in range(100)]
    return List100

def genList1000():
    global List1000
    List1000 = [random.randint(1, 100)for i in range(1000)]
    return List1000

def genList10000():
    global List10000
    List10000 =[random.randint(1, 100) for i in range(10000)]
    return List10000


# Select screen
def element_menu_prompt():
    global SelectOptions
    global SelectChoice
    SelectOptions=("1", "2", "3")
    while True:
        print("""please select element amount: 
            1) 100 
            2) 1000 
            3) 10000""")
        print()
        SelectChoice = input("Enter here: ")
        if SelectChoice in SelectOptions:
            if SelectChoice == "1":
                genList100()
                algorithm_menu_prompt()

            elif SelectChoice == "2":
                genList1000()
                algorithm_menu_prompt()

            elif SelectChoice == "3":
                genList10000()
                algorithm_menu_prompt()    
        else:
             print("Unacceptable value input. Please try again and select option 1, 2 or 3.")
            
# Algorithm selection screen with the option to see the contents of the generated list
def algorithm_menu_prompt():
    AlgorithmOptions = ("1", "2", "3", "4", "5", "v")
    while True:
        print("""please select algorithm: 
                1) BubbleSort 
                2) Insertion
                3) Quicksort
                4) Merge
                5) pythonsort
                
                View element list?
                v) View List""")
                
        AlgorithmChoice = input("Enter here: ")
        if AlgorithmChoice in AlgorithmOptions:
            if AlgorithmChoice == "1":
                if SelectChoice =="1":
                    Start_algo_time
                    n = len(List100)
                    for i in range(n-1):
                        for j in range(n-i-1):
                            if List100[j] > List100[j+1]:
                                List100[j], List100[j+1] = List100[j+1],List100[j]
                    end_algo_time
                    time_finish
                    print(List100)
                    print(f"Time: {time_finish: .10f} Seconds")
                    
                
        if AlgorithmChoice == "1":
                if SelectChoice =="2":
                    Start_algo_time
                    n = len(List1000)
                    for i in range(n-1):
                        for j in range(n-i-1):
                            if List1000[j] > List1000[j+1]:
                                List1000[j], List1000[j+1] = List1000[j+1],List1000[j]
                    end_algo_time
                    time_finish
                    print(List1000)
                    print(f"Time: {time_finish: .10f} Seconds")
                    

        if AlgorithmChoice == "1":
                if SelectChoice =="3":
                    Start_algo_time
                    n = len(List10000)
                    for i in range(n-1):
                        for j in range(n-i-1):
                            if List10000[j] > List10000[j+1]:
                                List10000[j], List10000[j+1] = List10000[j+1],List10000[j]
                    end_algo_time
                    time_finish
                    print(List10000)
                    print(f"Time: {time_finish: .10f} Seconds")
                    



        if AlgorithmChoice == "2":
            if SelectChoice == "1":
                Start_algo_time
                n = len(List100)
                for i in range(1,n):
                    insert_index = i
                    current_value = List100.pop(i)
                    for j in range(i-1, -1, -1):
                        if List100[j] > current_value:
                            insert_index = j
                        List100.insert(insert_index, current_value)
                end_algo_time
                time_finish
                print(List100)
                print(f"Time: {time_finish: .10f} Seconds")
                



        if AlgorithmChoice == "2":
            if SelectChoice == "2":
                Start_algo_time
                n = len(List1000)
                for i in range(1,n):
                    insert_index = i
                    current_value = List1000.pop(i)
                    for j in range(i-1, -1, -1):
                        if List1000[j] > current_value:
                            insert_index = j
                        List1000.insert(insert_index, current_value)
                end_algo_time
                time_finish
                print(List1000)
                print(f"Time: {time_finish: .10f} Seconds")
                



        if AlgorithmChoice == "2":
            if SelectChoice == "3":
                Start_algo_time
                n = len(List10000)
                for i in range(1,n):
                    insert_index = i
                    current_value = List10000.pop(i)
                    for j in range(i-1, -1, -1):
                        if List10000[j] > current_value:
                            insert_index = j
                        List10000.insert(insert_index, current_value)
                end_algo_time
                time_finish
                print(List10000)
                print(f"Time: {time_finish: .10f} Seconds")

        if AlgorithmChoice == "3":
            if SelectChoice =="1":
                Start_algo_time
                def partition(array, low, high):
                    pivot = array[high]
                    i = low - 1

                    for j in range(low, high):
                        if array[j] <= pivot:
                            i += 1
                            array[i], array[j] = array[j], array[i]

                        array[i+1], array[high] = array[high], array[i+1]
                        return i+1

                def quicksort(array, low=0, high=None):
                    if high is None:
                        high = len(array) - 1

                    if low < high:
                        pivot_index = partition(array, low, high)
                        quicksort(array, low, pivot_index-1)
                        quicksort(array, pivot_index+1, high)

                quicksort(List100)
                end_algo_time
                time_finish
                print(List100)
                print(f"Time: {time_finish: .10f} Seconds")


        if AlgorithmChoice == "3":
            if SelectChoice =="1":
                Start_algo_time
                def partition(array, low, high):
                    pivot = array[high]
                    i = low - 1

                    for j in range(low, high):
                        if array[j] <= pivot:
                            i += 1
                            array[i], array[j] = array[j], array[i]

                        array[i+1], array[high] = array[high], array[i+1]
                        return i+1

                def quicksort(array, low=0, high=None):
                    if high is None:
                        high = len(array) - 1

                    if low < high:
                        pivot_index = partition(array, low, high)
                        quicksort(array, low, pivot_index-1)
                        quicksort(array, pivot_index+1, high)

                quicksort(List1000)
                end_algo_time
                time_finish
                print(List1000)
                print(f"Time: {time_finish: .10f} Seconds")


        if AlgorithmChoice == "3":
            if SelectChoice =="1":
                Start_algo_time
                def partition(array, low, high):
                    pivot = array[high]
                    i = low - 1

                    for j in range(low, high):
                        if array[j] <= pivot:
                            i += 1
                            array[i], array[j] = array[j], array[i]

                        array[i+1], array[high] = array[high], array[i+1]
                        return i+1

                def quicksort(array, low=0, high=None):
                    if high is None:
                        high = len(array) - 1

                    if low < high:
                        pivot_index = partition(array, low, high)
                        quicksort(array, low, pivot_index-1)
                        quicksort(array, pivot_index+1, high)

                quicksort(List10000)
                end_algo_time
                time_finish
                print(List10000)
                print(f"Time: {time_finish: .10f} Seconds")

                                       


    
    
    
    

if __name__ == "__main__":
    main()