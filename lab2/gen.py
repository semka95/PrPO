import argparse
import string
import random
import sys
import time


def argparser():
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

    start = time.process_time()
    args = parser.parse_args()
    end = time.process_time()
    read = end - start

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
    return args, read


def main():
    args, read = argparser()
    random.seed(a=args.seed)
    alg = calc(args)

    if args.timeit:
        print(f'Data parse time: {read} seconds')
        print(f'Algorithm execution time: {alg} seconds')
    return


def calc(args):
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
        print(result)

    return alg


def gen_str(data_num, charset, length):
    res = ''
    for _ in range(data_num):
        res += ''.join(random.choice(charset) for i in range(length)) + '\n'
    return res


def gen_int(data_num):
    res = ''
    for _ in range(data_num):
        res += f'{random.randint(-sys.maxsize - 1, sys.maxsize)}\n'
    return res


def gen_float(data_num, distribution, min_value, max_value, mean, std):
    res = ''
    if distribution == 'uniform':
        for _ in range(data_num):
            res += f'{random.uniform(min_value, max_value)}\n'
    else:
        for _ in range(data_num):
            res += f'{random.normalvariate(mean, std)}\n'
    return res


if __name__ == "__main__":
    main()
