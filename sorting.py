import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    num_li = numbers[:]
    for min_index in range(len(num_li)):
        #print(num_li)
        min_value = numbers[min_index]
        min_ind = min_index
        for i in range(min_index, len(numbers)):
            if numbers[i] < min_value:
                min_ind = i
                min_value = numbers[i]
        numbers[min_ind], numbers[min_index] = numbers[min_index], numbers[min_ind]

def bubble_sort(numbers):
    num_li = numbers[:]
    plt.ion()
    plt.show()
    while True:
        for i in range(1,len(numbers)):
            print(numbers)
            if numbers[i] < numbers[i-1]:
                numbers[i],numbers[i-1] = numbers[i-1],numbers[i]

            index_highlight1 = i
            index_highlight2 = i - 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

        sort_num = list(sorted(num_li))
        if sort_num == numbers:
            break
    plt.ioff()
    plt.show()


def main():
    numbers = random_numbers(20,low=0,high=20)
    #select_sort = selection_sort(numbers)
    buble = bubble_sort(numbers)
    #print(numbers)
    #print(select_sort)
    print(buble)

if __name__ == "__main__":
    main()