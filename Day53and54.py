#task1
import module
print('1 + 8 =', module.add(1, 8))
print('4 - 2 =', module.subtract(4, 2))
print('6 * 6 =', module.multiply(6, 6))
print('1 / 8 =', module.divide(8, 2))

#task2
import _datetime
x = _datetime.datetime.now()
print(x.strftime("%c"))

#task3
import _datetime
today = _datetime.date.today()
yesterday = today - _datetime.timedelta(days=1)
tomorrow = today + _datetime.timedelta(days=1)
print("Yesterday : ", yesterday)
print("Tomorrow : ", tomorrow)