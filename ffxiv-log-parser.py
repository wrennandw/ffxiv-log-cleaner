import os

def loader():
    _logs = []
    _dir = os.listdir('./logs/raw')
    for e in _dir:
        with open(f'./logs/raw/{e}', encoding='utf-8') as _text:
            _logs_data = _text.read()
            _logs.append([e, _logs_data])
    return(_logs)

logs = loader()
