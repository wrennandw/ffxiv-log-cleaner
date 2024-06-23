import os

class EventLog:
    def __init__(self, filename, log_data): 
        self.filename = filename
        self.log_data = log_data


def loader():
    _logs = []
    _log_objects = []
    _dir = os.listdir('./logs/raw')
    for e in _dir:
        if e != 'directions.txt':
            with open(f'./logs/raw/{e}', encoding='utf-8') as _text:
                _logs_data = _text.read()
                _logs.append([e, _logs_data])
    
    for e in _logs:
        _log_objects.append(EventLog(e[0], e[1]))

    return _log_objects


def cleaner(data):
        data.log_data = data.log_data.splitlines()
        data.log_data = [e for e in data.log_data if e != '']
        data.log_data = [e.split(' ', 1)[-1] for e in data.log_data]

logs = loader()

for e in logs:
    cleaner(e)
    print(e.filename)
    print(e.log_data)
