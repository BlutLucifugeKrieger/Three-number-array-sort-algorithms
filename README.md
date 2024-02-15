![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Matplotlib Version](https://img.shields.io/badge/matplotlib-3.8.2-blue.svg)
![Memory Profiler Version](https://img.shields.io/badge/memory__profiler-0.61.0-blue)

## Three number array sort algorithms

### Made by: Juan Camilo Castro Velasquez

__________________________________________

## Description

This repository can organize an entry array of numbers using three methods (Bubble sort, Selection sort and Insertion sort).

### What's bubble sort?

The bubble sort algorithm is a simple but inefficient algorithm for sorting a list or an array of elements. It gets its name from the way larger elements gradually "rise" toward the desired final position, much like bubbles in a glass of water.

**The basic operation of the bubble algorithm is as follows:**

* Compare each pair of adjacent elements in the list.
* If they are in the wrong order (for example, the current element is greater than the next one), it swaps them.
* Continue this process for each pair of items in the list, going from left to right.
* Repeat this process several times until no more exchanges are made in a complete pass through the list. This ensures that the largest element is moved to the last position.
* The process is repeated for the remaining elements, excluding the last element already sorted.

### What's selection sort?

The selection sort algorithm, known as Selection, is another simple but less inefficient algorithm than Bubble Sort, used to sort a list or an array of elements.

**The basic operation of the selection algorithm is as follows:**

* Splits the list into two sub-lists: an ordered sub-list and an unordered sub-list.
* In each iteration, it finds the smallest element in the unordered sub-list.
* Swaps this smallest element with the first element of the unordered sub-list, placing it in its correct position in the ordered sub-list.
* Advances the boundary between the ordered and unordered sublists to the next element.
* Repeat this process until the entire list is sorted.
  
### What's insertion sort?

The insertion sort algorithm, known as Insertion, is another simple but efficient method for sorting a list or an array of elements.

**The basic operation of the insertion algorithm is as follows:**
* Splits the list into two sub-lists: an ordered sub-list and an unordered sub-list.
* In each iteration, it takes the first element of the unordered sub-list and compares it with the elements in the ordered sub-list, starting from the end.
* If the element is smaller than the current element in the sorted sub-list, it shifts it to the right to make room for the new element.
* Repeat this process until you find the correct position to insert the element into the ordered sub-list.
* Advances the boundary between the ordered and unordered sublists to the next element.
* Repeat this process until the entire list is sorted.

___________________________________________________________________________________

## How to use this repository

 First clone this repository and install the requirements.txt.

   **-> For clone this repository use:** git clone https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms.git

   **-> And, to install all the dependencies use:** pip install -r requirements.txt
    
  * Second, run the main.py file
    
**Then, you should got this:**

![image](https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms/assets/130005378/0db4e618-2421-48e6-bcaa-79d703119f43)

**In this screen, you should type a number to choose the method**

![image](https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms/assets/130005378/d28d1d8c-5197-418b-8345-a4adc22d41e2)

In this case, i wanna use the linear method, and as entry array i type: [99, 80 , 100, 2 , 31, 65, 12, 45, 67, 31, 87, 52, 11, 95, 49, 66, 71, 74, 10]
Then pull the enter key.

Finally, the result array appears (sorted array) and at the same time two graphics will appear too (time elapsed and memory usage)

![image](https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms/assets/130005378/2c22b37c-a0ae-41d6-8232-b7fc59780515)

![image](https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms/assets/130005378/435c1e93-b4b4-4a11-b847-c2d00ffe31c2)

___________________________________________________________

### Coverage report

![3_sort](https://github.com/BlutLucifugeKrieger/Three-number-array-sort-algorithms/assets/130005378/3ad73b48-09de-4953-93df-994741e01432)

___________________________________________________________

## Related info

 * https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
 * https://www.codecademy.com/resources/docs/general/algorithm/selection-sort
 * https://www.programiz.com/dsa/insertion-sort
