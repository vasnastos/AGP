pa='DIT UOI INFORMATICS AND TELECOMMUNICATIONS'

def Fun():
    print('A:{}'.format(pa))
    """
        pa="TraceBack Error"
        #-----------------------------------------------------------------------#
        # Traceback (most recent call last):                                    #
        # File "S:\AGP\PYTHON\scope2.py", line 7, in <module>                   #
        #    Fun()                                                              #
        # File "S:\AGP\PYTHON\scope2.py", line 4, in Fun                        #
        #    print('A:{}'.format(a))                                            #
        # UnboundLocalError: local variable 'a' referenced before assignment    #
        #-----------------------------------------------------------------------#
    """
Fun()
print(pa)