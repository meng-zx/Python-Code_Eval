import unittest
import time
import io
from GraphUnion_test import TestMakeConnected as test_class  # Modify the file and class name

def run_test_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    dummy_stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=dummy_stream, verbosity=0)
    start_time = time.time()
    runner.run(suite)
    end_time = time.time()
    return end_time - start_time 

def main(runs=1000):
    total_time = 0
    for _ in range(runs):
        total_time += run_test_suite()
    average_time = total_time / runs
    print(f"Average running time over {runs} runs: {average_time:.8f} seconds")

if __name__ == '__main__':
    main()
