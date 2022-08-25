class HttpError:
    """ Class to define Http Errors"""
   
    @staticmethod
    def error_422():
        """ HttpError 422 """
        
        return { "status_code": 422, "body": { "error": "Unprocessable Entity" }}
    
    
    @staticmethod
    def error_400():
        """ HttpError 400 """
        
        return { "status_code": 400, "body": { "error":  "Bad Request" }}
    
    
    @staticmethod
    def error_409():
        """ HttpError 409 """
        
        return { "status_code": 409, "body": { "error":  "Conflict"}}
    
    
    @staticmethod
    def error_500():
        """ HttpError 500 """
        
        return { "status_code": 500, "body": { "error":  "Internal Server Error"}}

    
    