import os

# Basic log data structure
class EventLog:
    def __init__(self, filename, log_data): 
        self.filename = filename
        self.log_data = log_data


def loader():
    _logs = []
    _log_objects = []
    _dir = os.listdir('./logs/raw')
    
    # Load each log and instantiate it as an object
    for e in _dir:
        if e != 'directions.txt':
            with open(f'./logs/raw/{e}', encoding='utf-8') as _text:
                _logs_data = _text.read()
                _log_objects.append(EventLog(e, _logs_data))
                
    return _log_objects


def cleaner(data):
        # Remove newline characters
        data.log_data = data.log_data.splitlines()

        # Remove empty strings
        data.log_data = [e for e in data.log_data if e != '']

        # Remove class markers at start of each string
        data.log_data = [e.split(' ', 1)[-1] for e in data.log_data]


# Load all logs in raw directory
logs = loader()

# Clean all logs
for e in logs:
    cleaner(e)
    print(e.filename)
    print(e.log_data)
