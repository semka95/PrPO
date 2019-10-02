import argparse
import string
import random
import sys
import timeit
import time

parser = argparse.ArgumentParser(description='Generate some random strings or integers.', prog='GEN', usage='%(prog)s [options]')
group = parser.add_mutually_exclusive_group()
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
group1 = parser.add_argument_group('numbers', 'parameters only for numbers')
group1.add_argument('-d', '--distribution',
                    choices=['uniform', 'normal'],
                    help='distribution type (default: normal)')
group1.add_argument('--mean', type=float,
                    help='normal distribution mean (any value)')
group1.add_argument('--std', type=float,
                    help='normal distribution standard deviation (greater than zero)')
group1.add_argument('--min_value', type=float,
                    help='uniform distribution min value (should be less than or equal to max value)')
group1.add_argument('--max_value', type=float,
                    help='uniform distribution max value (should be greater than or equal to min value)')
group2 = parser.add_argument_group('strings', 'parameters only for strings')
group2.add_argument('-l', '--length', type=int,
                    default=100,
                    help='length of the strings (default: 100)')
group2.add_argument('-c', '--charset',
                    default=string.ascii_letters + string.digits + string.punctuation,
                    help='acceptable character set (default: all letters, digits and punctuation marks)')
parser.add_argument('-f', '--filename', type=str,
                    default='', 
                    help='output file name (default: output to console)')
start = time.clock()
args = parser.parse_args()
end = time.clock()
read = end - start

random.seed(a=args.seed)

if args.filename != '':
    sys.stdout = open(args.filename, 'w')

# value checks

def main():
    if args.type == 'str':
        calc = timeit.timeit(gen_str, number=1)
    elif args.type == 'int':
        calc = timeit.timeit(gen_str, number=1)
    elif args.type == 'float':
        calc = timeit.timeit(gen_float, number=1)
    
    if args.timeit:
        sys.stdout = sys.__stdout__
        print(f'Data parse time: ${read}')
        print(f'Algorithm execution time: ${calc}')
    
    sys.stdout.close()
    return
        


def gen_str():
    for _ in range(args.data_num):
        print(''.join(random.choice(args.charset) for i in range(args.length)))
    return

def gen_int():
    for _ in range(args.data_num):
        print(random.randint(-sys.maxsize - 1,sys.maxsize))
    return

def gen_float():
    if args.distribution == 'uniform':
        for _ in range(args.data_num):
            print(random.uniform(args.min_value,args.max_value))
    else:
        for _ in range(args.data_num):
            print(random.normalvariate(args.mean, args.std))
    return

main()