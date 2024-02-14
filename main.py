from Algorithms.bubble_sort import bubble
from Algorithms.insertion_sort import insertion
from Algorithms.selection_sort import selection


def main():
    init()


def init():

    print()
    print("Welcome to sort algoritms")
    print()
    print("1.) Bubble sort")
    print()
    print("2.) Selection sort")
    print()
    print("3.) Insertion sort")
    print()

    val = input("please type a number to proceed: ")
    value = int(val)

    if value == 1:
        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]

        _bubble = bubble()
        print("Input array: ", array)
        print("Result: ", _bubble.bubble_sort(array))

        _bubble.plot_graphs()

    elif value == 2:
        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]


        _selection = selection()

        print("Input array: ", array)
        print("Result: ", _selection.selection_sort(array))
        _selection.plot_graphs()

    elif value == 3:

        entry_values = input("Please type the numbers of the array with spaces between each other: ")
        array = [int(number) for number in entry_values.split()]

        _insertion = insertion()

        print("Input array: ", array)
        print("Result: ", _insertion.insertion_sort(array))
        _insertion.plot_graphs()


    else:

        print("Invalid entry, please try again")


if __name__ == "__main__":
    main()
