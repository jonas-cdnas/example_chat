import re
from datetime import datetime

# Archivo de entrada y salida
input_file = 'flask_logs.log'
output_file = 'converted_logs.log'

# Patrón para extraer la información de los logs de Flask
pattern = r'INFO:werkzeug:(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>.*?)\] "(?P<method>\w+) (?P<path>.*?) HTTP/(?P<version>\d+\.\d+)" (?P<status>\d+) -'

def convert_to_clf(log_line):
    match = re.match(pattern, log_line)
    if match:
        ip = match.group('ip')
        date_str = match.group('datetime')
        method = match.group('method')
        path = match.group('path')
        version = match.group('version')
        status = match.group('status')

        # Convertir la fecha al formato CLF
        date_obj = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S %z")
        clf_date_str = date_obj.strftime("%d/%b/%Y:%H:%M:%S %z")

        # Crear el formato CLF
        clf_log = f'{ip} - - [{clf_date_str}] "{method} {path} HTTP/{version}" {status} -'
        return clf_log
    return None

# Leer y convertir los logs
with open(input_file, 'r') as log_file, open(output_file, 'w') as clf_file:
    for line in log_file:
        clf_log = convert_to_clf(line)
        if clf_log:
            clf_file.write(clf_log + '\n')

print(f'Logs convertidos a CLF en {output_file}')