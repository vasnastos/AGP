from functools import reduce
import statistics as s
import logging as log

#create a logger
arraylog=log.getLogger('Test Logger')
fh=log.FileHandler('Datasets/loggingmsg.log','w')
sh=log.StreamHandler()
arraylog.setLevel(log.INFO)
formatter=log.Formatter('*%(asctime)s\n*%(levelname)s\n*%(message)s\n\n')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
arraylog.addHandler(sh)
arraylog.addHandler(fh)


array=[1,2,3,4,5,67,8,9,0,45,12]
arraylog.info('Table Created')

print(filter(lambda x:x>7,array))
arraylog.debug('Filtering data and keep the Data with value above 7')

print(map(lambda x:x+6,array))
arraylog.warning('Mapping over data--Data will change')

arraylog.info(f'Data Summary:{reduce(lambda y,item:y+item,array,0)}')

arraylog.info(sum(array))
arraylog.info(len(array))
arraylog.info(max(array))
arraylog.info(s.mean(array))
arraylog.info(s.median(array))
arraylog.warning(type(array))