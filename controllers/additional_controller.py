def calculate_sum(a, b):
    return {'result': a + b}

def check_even(number):
    return {'is_even': number % 2 == 0}

def generate_sequence(n):
    return {'sequence': list(range(1, n+1))}

def greet(name):
    return {'message': f'Hello, {name}!'}
