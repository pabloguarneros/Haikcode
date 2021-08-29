import unittest

def merge(a, b):
    sorted_list = ['None']* (len(a)+len(b))
    a_pointer = 0
    b_pointer = 0
    for i in range(len(sorted_list)):
        print(a,a_pointer,b,b_pointer,i)
        if b_pointer >= len(b): 
            sorted_list[i] = a[a_pointer]
            a_pointer += 1
        elif a_pointer >= len(a): 
            sorted_list[i] = a[b_pointer]
            b_pointer += 1
        elif a[a_pointer] <= b[b_pointer]:
            sorted_list[i] = a[a_pointer]
            a_pointer += 1
        else:
            sorted_list[i] = b[b_pointer]
            b_pointer += 1
    return sorted_list

def test_merge(list):
    if len(list) > 1:
        mid_point = len(list)//2
        a = test_merge(list[:mid_point])
        b = test_merge(list[mid_point:])
        list = merge(a,b)
    return list


class TestMergeSort(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(test_merge([1,4,2]), [1,2,4])


if __name__ == "__main__":
    TestMergeSort().test_basic()
    print("Everything passed")