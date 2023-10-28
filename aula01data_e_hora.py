# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
data_atual = datetime.now()
print(data_atual)
print('--')
print('Trabalhando com Unix Timestamp')
print(data.timestamp()) # Isso está na base de dados
print(datetime.fromtimestamp(1698066284))
print('--')
print('Trabalhando com Timezone')
data_timezone_tokyo = datetime(2023, 10, 23, 10, 8, 50, tzinfo=timezone('Asia/Tokyo'))
print(datetime.now(timezone('Asia/Tokyo')))
print(data_timezone_tokyo)
print('--')
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
print('Trabalhando com TimeDelta e RelativeDelta')
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:00', fmt)
data_fim = datetime.strptime('12/12/2022 08:30:00', fmt)
delta = timedelta(days=10, hours=2)
print(data_fim - delta)
print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
delta2 = data_fim - data_inicio
print(delta2.days, delta2.seconds, delta2.microseconds)
print(delta2.total_seconds())
deltarelative = relativedelta(data_fim, data_inicio)
print(deltarelative)
print(data_fim + relativedelta(seconds=60, minutes=10))
# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
print('--')
print('Trabalhando com formatação de datas')
dataformatada = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(dataformatada.strftime('%d/%m/%Y'))
print(dataformatada.strftime('%d/%m/%Y %H:%M'))
print(dataformatada.strftime('%d/%m/%Y %H:%M:%S'))
print(dataformatada.strftime('%Y'), dataformatada.year)
print(dataformatada.strftime('%d'), dataformatada.day)
print(dataformatada.strftime('%m'), dataformatada.month)
print(dataformatada.strftime('%H'), dataformatada.hour)
print(dataformatada.strftime('%M'), dataformatada.minute)
print(dataformatada.strftime('%S'), dataformatada.second)
