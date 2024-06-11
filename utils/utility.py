import random
import requests
import traceback

from loggers.logger import logger
# Sample data for generating logs
users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
actions = ['accessed', 'created', 'deleted', 'updated', 'viewed']
items = ['file', 'record', 'document', 'profile', 'item']

log_templates = {
    'debug': [
        '{} user debugged the {}',
        '{} user debugged the {} successfully',
    ],
    'info': [
        '{} user accessed the {}',
        '{} user created new {}',
        '{} user deleted the {}',
        '{} user updated the {}',
        '{} user viewed the {}'
    ],
    'warning': [
        '{} user attempted to access restricted {}',
        '{} user encountered a slow response while accessing {}',
    ],
    'error': [
        '{} user failed to access the {}',
        '{} user encountered an error while creating {}',
        '{} user failed to delete the {}',
    ],
    'critical': [
        'Critical failure as {} user tried to update the {}',
        '{} user caused system outage while accessing {}',
    ],
    'exception': [
        'Exception occurred when {} user processed the {}',
        'Unhandled exception by {} user during {} operation',
    ]
}

def random_exception_generator():
    exception_type = random.choice([
        'FileNotFoundError',
        'ConnectionError',
        'KeyError',
        'IndexError',
        'ValueError'
    ])
    
    try:
        if exception_type == 'FileNotFoundError':
            # Attempt to open a non-existent file
            with open('non_existent_file.txt', 'r') as file:
                pass
        
        elif exception_type == 'ConnectionError':
            # Attempt to connect to a non-existent URL
            response = requests.get('http://thisurldoesnotexist.tld')
            response.raise_for_status()
        
        elif exception_type == 'KeyError':
            # Attempt to access a non-existent key in a dictionary
            d = {'key1': 'value1'}
            value = d['non_existent_key']
        
        elif exception_type == 'IndexError':
            # Attempt to access an out-of-range index in a list
            lst = [1, 2, 3]
            value = lst[10]
        
        elif exception_type == 'ValueError':
            # Attempt to convert an invalid string to an integer
            num = int('invalid_int')
        
    except Exception as e:
        logger.error(f"{exception_type} occurred: {e}")
        logger.error(traceback.format_exc())
