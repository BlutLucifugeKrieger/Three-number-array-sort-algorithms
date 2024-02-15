

import time
import matplotlib.pyplot as plt
import memory_profiler



class selection:

    def __init__(self):

        self.arr = []
        self.elapsed_times = []
        self.memory_usages = []

    def selection_sort(self,arr):

        n = len(arr)
        self.arr.append(n)

        for i in range(n):

            start_time = time.time()
            memory_used = memory_profiler.memory_usage()[0]

            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]



            end_time = time.time()
            elapsed_time = end_time - start_time
            self.elapsed_times.append(elapsed_time)
            self.memory_usages.append(memory_used)

        return arr



    def plot_graphs(self): # pragma: no cover

        len_arr = len(self.arr)

        if len_arr != 0:
            # graph time and memory
            plt.figure(figsize=(10, 5))

            # time graph
            plt.subplot(2, 1, 1)
            plt.plot(self.elapsed_times, label='Elapsed Time')
            plt.xlabel('Iteration')
            plt.ylabel('Time (seconds)')
            plt.title('Elapsed Time in Each Iteration')
            plt.legend()

            # memory graph
            plt.subplot(2, 1, 2)
            plt.plot(self.memory_usages, label='Memory Used')
            plt.xlabel('Iteration')
            plt.ylabel('Memory (MB)')
            plt.title('Memory Used in Each Iteration')
            plt.legend()

            plt.tight_layout()
            plt.show()

        else:
            print(f"Please, try again")