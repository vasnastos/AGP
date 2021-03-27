import logging as log

log.getLogger().setLevel(log.DEBUG)
x=input('Give First Number:')
log.info('Number input:'+str(x))
y=input('Give second Number:')
log.info('Number Input:'+str(y))
log.info('Summary:'+str(int(x)+int(y)))
