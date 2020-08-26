# TASK 1

# let's use the itertools.product to generate all possible combinations
from itertools import product


def correct_expression(n: int):
    """
    1. Generating all combinations (with product)
    2. Eliminate combinations with unpaired '(' and ')'
    3. Last check for the correct placement
    """
    result = []
    tmp = ['()'] * n * 2
    for item in product(*tmp):                         # 1
        if item.count('(') == item.count(')'):         # 2
            tmp, k = 0, 1
            for el in item:                            # 3
                tmp += 1 if el == '(' else -1
                if tmp <= -1:                          # exclude combinations similar to "())...."
                    k = 0
                    break
            if k:
                result.append(''.join(item))
    return result


# check task number 1
number = int(input('Enter a positive integer: '))
print(correct_expression(number))

# TASK 2

# set the initial data
initial_data = {'s': 1,
                'n': 4,
                'name': ('gdansk', 'bydgoszcz', 'torun', 'warszawa'),
                'p': (2, 3, 3, 2),
                'nr_cost': {1: {2: 1, 3: 3}, 2: {1: 1, 3: 1, 4: 4},
                            3: {1: 3, 2: 1, 4: 1}, 4: {2: 4, 3: 1}},
                'r': 2,
                'answer': ['gdansk warszawa', 'bydgoszcz warszawa', 'bydgoszcz torun']
                }


def all_paths(graph: dict, start: int, finish: int):
    """
    Search for all possible routes from one city to another.
    Visit option the same city more than once, not considered.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in set(graph[vertex].keys()) - set(path):
                if next_ == finish:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def min_cost(data: dict):
    """
    Calculate the minimum transportation cost from city NAME1 to city NAME2
    (one line per request)
    """
    for ans in data['answer']:
        result = {}
        ans = ans.split()
        start, finish = data['name'].index(ans[0]) + 1, data['name'].index(ans[1]) + 1
        all_routes = list(all_paths(data['nr_cost'], start, finish))
        for route in all_routes:
            route = tuple(route)
            result[route] = 0
            for i in range(len(route) - 1):
                result[route] += data['nr_cost'].get(route[i]).get(route[i + 1])
        print(min(result.values()))


# check task number 2
min_cost(initial_data)

# TASK 3
""" 3. Find the sum of the digits in the number 100! (i.e. 100 factorial) 
{Correct answer: 648} """


def factorial(n: int):
    """ calculating factorial """
    return 1 if n == 1 else n * factorial(n - 1)


def sum_digit_factorial(n: int):
    """ Find the sum of the digits in the number n!"""
    return sum([int(i) for i in str(factorial(n))])


# check task number 3
print(sum_digit_factorial(100))
