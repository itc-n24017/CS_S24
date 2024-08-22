import logging

def devide(x1, x2):
    return x1 / x2

logging.basicConfig(filename='testlog.log', level=logging.WARNING, format='%(levelname)s:%(message)s')

try:
    ret = devide(10, 0)
except:
    logging.exception('test exception massage')
logging.shutdown()
