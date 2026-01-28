import sys

from app.logging.logger import logging

def error_message_detail(error:str,error_detail:sys):
    '''

    '''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message:str, error_details:sys):
        super().__init__()
        self.error_message = error_message_detail(error=error_message,error_detail=error_details)
        
    def __str__(self):
        return self.error_message

#testing
if __name__ == "__main__":
    try:
        a= 1/0
        logging.info("trying diving by zero it will gonna throw an error")
    except Exception as e:
        raise CustomException(e,sys)