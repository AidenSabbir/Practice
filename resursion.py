def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def sum_n(n):
    if n == 0:
        return 0
    return n+sum_n(n-1)


def print_1_to_N(n):
    if n == 1:
        return [1]
    data = print_1_to_N(n-1) + [n]
    return data

def print_N_to_1(n):
    if n == 1:
        return [1]
    data = [n] + print_N_to_1(n-1)
    return data


def fib_of_nth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_of_nth(n-1) + fib_of_nth(n-2)


def reverse(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse(string[:-1])



def sum_digits(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    return int(n[-1]) + sum_digits(int(n[:-1]))

def sub_sets(string):
    if len(string) == 0:
        return ['']
    subset = sub_sets(string[1:])
    return subset + [string[0] + x for x in subset]

def perm(s):
    s = str(s)
    r = []
    if len(s) == 0:
        return ['']
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        for x in perm(rest):
            r.append(ch+x)
    return r
