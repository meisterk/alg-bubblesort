import unittest

# Function bubblesort:
# Parameter: unsoertiertes Array mit Zahlen
# Result: sortiertes Array


def bubblesort(unsortiert):
    laenge = len(unsortiert)
    for n in range(laenge, 1, -1):
        for i in range(0, n-1):
            if unsortiert[i] > unsortiert[i+1]:
                temp = unsortiert[i]
                unsortiert[i] = unsortiert[i+1]
                unsortiert[i+1] = temp
    return unsortiert


# Testcases
class TestBubblesort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bubblesort([1, 2, 3]), [1, 2, 3])

    def test_2(self):
        self.assertEqual(bubblesort([3, 2, 1]), [1, 2, 3])

    def test_3(self):
        self.assertEqual(bubblesort([-3, 2, 1]), [-3, 1, 2])


# Run Tests
if __name__ == "__main__":
    unittest.main()
