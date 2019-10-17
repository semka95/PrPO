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
        random.seed(2)
        data_num = 100
        charset = string.ascii_letters
        length = 5

        got = gen_str(data_num, charset, length)

        for i in charset:
            self.assertIn(i, got)

    def test_random_str(self):
        """
        Test if generated strings are random
        """
        random.seed(0)
        data_num = 10
        charset = string.ascii_letters
        length = 5

        got = [gen_str(data_num, charset, length) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))

    def test_seed_str(self):
        """
        Test if seed change affects output
        """
        data_num = 10
        charset = string.ascii_letters
        length = 5

        random.seed(1)
        got1 = gen_str(data_num, charset, length)
        random.seed(2)
        got2 = gen_str(data_num, charset, length)
        random.seed(1)
        got3 = gen_str(data_num, charset, length)

        self.assertTrue(got1 == got3 and got1 != got2)


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
        random.seed(0)
        data_num = 10

        got = [gen_int(data_num) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))

    def test_seed_int(self):
        """
        Test if seed change affects output
        """
        data_num = 10

        random.seed(1)
        got1 = gen_int(data_num)
        random.seed(2)
        got2 = gen_int(data_num)
        random.seed(1)
        got3 = gen_int(data_num)

        self.assertTrue(got1 == got3 and got1 != got2)


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
        random.seed(0)
        data_num = 10
        distribution = 'uniform'
        min_value = 0
        max_value = 1

        got = [gen_float(data_num, distribution, min_value,
                         max_value, 0, 0) for _ in range(1000)]

        self.assertTrue(len(set(got)) == len(got))

    def test_seed_float(self):
        """
        Test if seed change affects output
        """
        random.seed(1)
        data_num = 10
        distribution = 'uniform'
        min_value = 0
        max_value = 1

        got1 = gen_float(data_num, distribution, min_value, max_value, 0, 0)
        random.seed(2)
        got2 = gen_float(data_num, distribution, min_value, max_value, 0, 0)
        random.seed(1)
        got3 = gen_float(data_num, distribution, min_value, max_value, 0, 0)

        self.assertTrue(got1 == got3 and got1 != got2)

    def test_uniform(self):
        """
        Test uniform distribution
        Value N should be [a; b]
        """
        data_num = 10000
        distribution = 'uniform'
        a = 0
        b = 1

        got = gen_float(data_num, distribution, a, b, 0, 0).split('\n')
        del got[-1]
        float_arr = [float(x) for x in got]

        flag = False
        for i in float_arr:
            if i < a or i > b:
                flag = True

        self.assertFalse(flag)

    def test_normal(self):
        """
        Test normal distribution
        Value should be (x-3σ; x+3σ) - three-sigma rule (99.7%)
        """
        random.seed(0)
        data_num = 100000
        distribution = 'normal'
        mean = 5
        std = 0.5

        got = gen_float(data_num, distribution, 0, 0, mean, std).split('\n')
        del got[-1]
        float_arr = [float(x) for x in got]

        counter = 0
        for i in float_arr:
            if i < mean-3*std or i > mean+3*std:
                counter += 1

        self.assertTrue(counter <= data_num * 0.3 / 100)


if __name__ == "__main__":
    unittest.main()
