import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Basic log data structure
class EventLog:
    def __init__(self, filename, log_data): 
        self.filename = filename
        self.log_data = log_data


def loader():
    _log_objects = []
    _dir = os.listdir('./logs/raw')
    
    # Load each log and instantiate it as an object
    for filename in _dir:
        if filename != 'directions.txt':
            with open(f'./logs/raw/{filename}', encoding='utf-8') as _text:
                _logs_data = _text.read()
                _log_objects.append(EventLog(filename, _logs_data))
                
    return _log_objects


def cleaner(data):
    # Remove newline characters
    data.log_data = data.log_data.splitlines()

    # Remove empty strings
    data.log_data = [e for e in data.log_data if e != '']

    # Remove class markers and hearts at start of each string
    # LS/CWLS tags are left intact for clarity
    _clean =[]
    for e in data.log_data:
        if e[0] == '[' or e[0].isalpha():
            _clean.append(e)
        else:
            _clean.append(e.split(' ', 1)[-1])
    
    data.log_data = [e.replace('♥', '') for e in _clean]

    # Remove server names
    _lines = enumerate(data.log_data)
    for e in _lines:
        _bounds = []
        
        # Find the start and end of the surname, excluding the first letter
        _bounds.append(e[1].find(' '))
        _bounds.append(e[1].find(' ', _bounds[0]+1))
        
        # Check if there's a server in the surname and remove it
        for i in range(_bounds[0]+2, _bounds[1]-1):
            if e[1][i].isupper():
                data.log_data[e[0]] = data.log_data[e[0]].replace(
                    e[1][i:_bounds[1]-1],'')
                break
    
    # Add newlines to each line
    data.log_data = [f'{e}\n\n' for e in data.log_data]


# Load all logs in raw directory
logs = loader()

# Clean all logs
for e in logs:
    cleaner(e)
    
    # Save clean logs
    _rawfile = str(e.filename)
    with open(f'./logs/clean/[Clean]{_rawfile}', 'w', encoding='utf-8') as _cleanfile:
        for line in e.log_data:
           _cleanfile.write(line)
