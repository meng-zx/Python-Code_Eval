from memory_profiler import memory_usage
import unittest
import io
import sys
from SW_test import TestMaxSlidingWindow as test_class  # Modify the file and class name
import numpy as np  

def run_test_suite():
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=0, stream=sys.stdout)
    runner.run(suite)

    sys.stdout = original_stdout

def main(runs=100):
    mem_usages = []
    for _ in range(runs):
        mem_usage = memory_usage((run_test_suite, ), interval=0.1, timeout=120, max_usage=True)
        mem_usages.append(mem_usage)

    average_mem_usage = np.mean(mem_usages)
    print(f"Average memory usage over {runs} runs: {average_mem_usage:.2f} MiB")

if __name__ == '__main__':
    main()
