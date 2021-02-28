import logging
import socket as s
import re

ipclass={'A':'([1-9]?[0-9]|1(0|1)[0-9]|12[0-7])','B':'(1[2-8][0-9]|19(0|1))','C':'(19[2-9]|2(0|1)[0-9]|22[0-3])'}

def main():
    logging.info('This is a logging information message')
    logging.critical('Error logging message from module logging')
    logging.warning('This is a warning logging message')
    logging.error('this is an error logging message from module logging')
    logging.debug('This is a debug logging message')

def ip_show():
    sc=s.socket(s.AF_INET,s.SOCK_DGRAM)
    sc.connect(('8.8.8.8',80))
    adrress=''
    try:
        address=sc.getsockname()[0]
        print(sc.getsockname()[0])
    except:
        address='127.0.0.1'
        print('Loopback:127.0.0.1')
    finally:
        sc.close()
    logging.warning('Drain information from Socket,Ip Adreess is exposed!!!!!!!!!')
    print('Candicate Subnet Mask')
    print('********************************')
    if re.match(ipclass['A']+'\..*',str(address)):
        print('Subnet Mask:255.0.0.0-Ip:'+str(address)+'-->Class A')
        return
    else:
        logging.error('Subnet Masked Failed:255.0.0.0')
    if re.match(ipclass['B']+'\..*',str(address)):
        print('Subnet Mask:255.255.0.0-Ip:'+str(address)+'-->Class B') 
        return
    else:
        logging.error('Subnet Masked Failed:255.255.0.0')
    if re.match(ipclass['C']+'\..*',address):
        print('Subnet Mask:255.255.255.0-Ip:'+str(address)+'-->Class C')    
        return
    else:
        logging.error('Subnet Masked Failed:255.255.255.0')
    logging.warning('Loopback address ip/Proxy Server Connected/Another Network type Ip')

if __name__=="__main__":
    main()
    print('-------------------------------------')
    ip_show()
