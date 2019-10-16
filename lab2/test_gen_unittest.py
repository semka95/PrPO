import unittest
import random
import string

from gen import gen_str, gen_int, gen_float


class TestGenStr(unittest.TestCase):
    def test_len_str(self):
        """
        Test length of the generated string
        """
        data_num = 10
        charset = string.ascii_letters
        length = 5

        got = gen_str(data_num, charset, length)
        result = got.find("\n")

        self.assertEqual(result, length)

    def test_num_str(self):
        """
        Test number of generated strings
        """
        data_num = 10
        charset = string.ascii_letters
        length = 5

        got = gen_str(data_num, charset, length)
        result = got.count('\n')

        self.assertEqual(result, data_num)

    def test_charset(self):
        """
        Test if charset affects output
        """
        data_num = 10
        charset1 = "abcd"
        charset2 = "efgh"
        length = 5

        got1 = gen_str(data_num, charset1, length)
        got2 = gen_str(data_num, charset2, length)

        self.assertNotIn(got1, charset2)
        self.assertNotIn(got2, charset1)

    def test_random_str(self):
        """
        Test if generated strings are random
        """
        data_num = 10
        charset = string.ascii_letters
        length = 5

        got = [gen_str(data_num, charset, length) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))


class TestGenInt(unittest.TestCase):
    def test_num_int(self):
        """
        Test number of generated integers
        """
        data_num = 10

        got = gen_int(data_num)
        result = got.count('\n')

        self.assertEqual(result, data_num)

    def test_random_int(self):
        """
        Test if generated integers are random
        """
        data_num = 10

        got = [gen_int(data_num) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))


class TestGenFloat(unittest.TestCase):
    def test_num_float(self):
        """
        Test number of generated floats
        """
        data_num = 10
        distribution = 'uniform'
        min_value = 0
        max_value = 1

        got = gen_float(data_num, distribution, min_value, max_value, 0, 0)
        result = got.count('\n')

        self.assertEqual(result, data_num)

    def test_random(self):
        """
        Test if generated floats are random
        """
        data_num = 10
        distribution = 'uniform'
        min_value = 0
        max_value = 1

        got = [gen_float(data_num, distribution, min_value,
                         max_value, 0, 0) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))

    def test_uniform(self):
        """
        Test uniform distribution
        Value N should be a <= N <= b for a <= b and b <= N <= a for b < a
        """
        data_num = 100
        distribution = 'uniform'
        a = 0
        b = 1

        got = gen_float(data_num, distribution, a, b, 0, 0).split('\n')
        del got[-1]
        float_arr = [float(x) for x in got]

        flag = False
        for i in float_arr:
            if i < a and i > b and a <= b:
                flag = True

        self.assertFalse(flag)

    def test_normal(self):
        """
        Test normal distribution
        Value should be (x-3σ;x+3σ)
        """
        data_num = 10
        distribution = 'normal'
        mean = 5
        std = 1

        got = gen_float(data_num, distribution, 0, 0, mean, std).split('\n')
        del got[-1]
        float_arr = [float(x) for x in got]

        flag = False
        for i in float_arr:
            if i < mean-3*std and i > mean+3*std:
                flag = True

        self.assertFalse(flag)


if __name__ == "__main__":
    unittest.main()
