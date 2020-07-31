import random
import pickle

def generate_test_case(N = 100, limit = 1000):
        test_case = []
        for i in range(N):
                test_case.append(random.randint(0, limit))

        a_file = open("test_case.pkl", "wb")
        pickle.dump(test_case, a_file)
        a_file.close()

        test_case.sort()

        a_file = open("sorted_test_case.pkl", "wb")
        pickle.dump(test_case, a_file)
        a_file.close()

