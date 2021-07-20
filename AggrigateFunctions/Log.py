import logging

class Log:
    logging.basicConfig(filename="OutputInfo.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    