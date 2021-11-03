import logging
from project.settings import DEBUG

logger = logging.getLogger(name='project')
logger.setLevel(logging.DEBUG)

format = '%(asctime)s [%(levelname)s] %(filename)s: %(message)s'
formatter = logging.Formatter(format, datefmt='%d.%m.%Y %H:%M:%S')

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.INFO

# создаём консольный handler и задаём уровень
console_handler = logging.StreamHandler()
console_handler.setLevel(level)

# добавляем formatter
console_handler.setFormatter(formatter)

# добавляем к logger
logger.addHandler(console_handler)
