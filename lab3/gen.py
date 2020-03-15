"""Random string/number generator

This script allows the user to generate random strings or numbers
(each on a new line) and write it to the file. User can specify
seed, type of generated data and output execution time.

For strings user can specify length of the strings, and character set.

For float numbers user can specify distribution - uniform or normal, and
parameters of distribution - min and max value for uniform, mean and
standard deviation for normal distribution.

This file can also be imported as a module and contains the following
functions:

    * argparser - returns parsed arguments and data read time
    * gen_str - returns random generated strings
    * gen_int - returns random generated integers
    * gen_float - returns random generated floats
    * main - the main function of the script
"""
import argparse
import string
import random
import sys
import time


def argparser() -> dict:
    """Parses command-line options and arguments and returns them as a dictioanary

    Returns
    -------
    dict
        a dict of parsed command-line arguments and options
    """
    parser = argparse.ArgumentParser(
        description='Generate some random strings or integers.', prog='GEN', usage='%(prog)s [options]')
    parser.add_argument('data_num', type=int,
                        help='number of strings or integers to generate')
    parser.add_argument('-s', '--seed', type=int,
                        default=0,
                        help='initial seed value (default: 0)')
    parser.add_argument('-t', '--type',
                        choices=['int', 'float', 'str'],
                        default='int',
                        help='data type (default: int)')
    parser.add_argument('--timeit',
                        action='store_true',
                        help='print execution time')
    group1 = parser.add_argument_group(
        'floats', 'parameters only for float numbers')
    group1.add_argument('-d', '--distribution',
                        choices=['uniform', 'normal'],
                        help='distribution type')
    group1.add_argument('--mean', type=float,
                        help='normal distribution mean (any value)')
    group1.add_argument('--std', type=float,
                        help='normal distribution standard deviation (greater than zero)')
    group1.add_argument('--min_value', type=float,
                        help='uniform distribution min value (should be less than or equal to max value)')
    group1.add_argument('--max_value', type=float,
                        help='uniform distribution max value (should be greater than or equal to min value)')
    group2 = parser.add_argument_group(
        'strings', 'parameters only for strings')
    group2.add_argument('-l', '--length', type=int,
                        default=100,
                        help='length of the strings (default: 100)')
    group2.add_argument('-c', '--charset',
                        default=string.ascii_letters + string.digits + string.punctuation,
                        help='acceptable character set (default: all letters, digits and punctuation marks)')
    parser.add_argument('-f', '--filename', type=str,
                        default='',
                        help='output file name (default: output to console)')

    args = parser.parse_args()

    if args.type == 'float':
        if args.distribution == None:
            sys.exit("GEN: error: distribution must be specified")
        if args.distribution == 'uniform':
            if args.min_value == None or args.max_value == None:
                sys.exit("GEN: error: min value and max value must be specified")
            if args.max_value < args.min_value:
                sys.exit(
                    "GEN: error: max value must be greater or equal to min_value")
        if args.distribution == 'normal':
            if args.mean == None or args.std == None:
                sys.exit(
                    "GEN: error: mean value and standard deviation must be specified")
            if args.std <= 0:
                sys.exit('GEN: error: std must be greater than zero')
    return args


def gen_str(data_num: int, charset: str, length: int) -> str:
    """Returns random generated strings

    Parameters
    ----------
    data_num : int
        The number of strings to generate
    charset : str
        Acceptable character set
    length : int
        Length of the generated strings

    Returns
    -------
    str
        a string of randomly generated strings
    """
    res = ''
    for _ in range(data_num):
        res += ''.join(random.choice(charset) for i in range(length)) + '\n'
    return res


def gen_int(data_num: int) -> str:
    """Returns random generated integer numbers

    Parameters
    ----------
    data_num : int
        The number of integer numbers to generate

    Returns
    -------
    str
        a string of randomly generated integer numbers
    """
    res = ''
    for _ in range(data_num):
        res += f'{random.randint(-sys.maxsize - 1, sys.maxsize)}\n'
    return res


def gen_float(data_num: int, distribution: str, min_value: float, max_value: float, mean: float, std: float) -> str:
    """Returns random generated float numbers

    Parameters
    ----------
    data_num : int
        The number of float numbers to generate
    distribution : str
        Distribution type (uniform or normal)
    min_value : float
        Uniform distribution min value
    max_value : float
        Uniform distribution max value
    mean : float
        normal distribution mean
    std : float
        Normal distribution standard deviation

    Returns
    -------
    str
        a string of randomly generated float numbers
    """
    res = ''
    if distribution == 'uniform':
        for _ in range(data_num):
            res += f'{random.uniform(min_value, max_value)}\n'
    else:
        for _ in range(data_num):
            res += f'{random.normalvariate(mean, std)}\n'
    return res


def main():
    args = argparser()
    random.seed(a=args.seed)

    alg = 0.0
    if args.type == 'str':
        start = time.process_time()
        result = gen_str(args.data_num, args.charset, args.length)
        end = time.process_time()
        alg = end - start
    elif args.type == 'int':
        start = time.process_time()
        result = gen_int(args.data_num)
        end = time.process_time()
        alg = end - start
    elif args.type == 'float':
        start = time.process_time()
        result = gen_float(args.data_num, args.distribution,
                           args.min_value, args.max_value, args.mean, args.std)
        end = time.process_time()
        alg = end - start

    if args.filename != '':
        with open(args.filename, "w") as f:
            f.write(result)
    else:
        print(f'Generated data:\n{result}')

    if args.timeit:
        print(f'Algorithm execution time: {alg} seconds')


if __name__ == "__main__":
    main()
