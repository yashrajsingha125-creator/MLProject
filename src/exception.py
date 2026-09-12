import sys
#imports logging object from loggers.py
from src.logger import logging

#generates detailed error message 
def error_message_detail(error,error_detail:sys):
#   return exception type, exception object and also give exception tracebacks
#   exc_tb --> stores info. about where error has occured
    _,_,exc_tb = error_detail.exc_info()
#gets file name of python file in which error has occured 
    file_name = exc_tb.tb_frame.f_code.co_filename

#tells file_name, exc_tb.tb_lineno:line at which error occured, 
# str(error):exct error
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message  


#run this part of code only when I run exception.py
if __name__ =="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)           