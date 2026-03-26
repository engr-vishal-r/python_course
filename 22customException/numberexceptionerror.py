class NumberFormatExceptionError(Exception): 
    def __init__(self, message="NumberFormatException Occurred"):
        self.message = message
        super().__init__(self.message)
"""
try:
    number = int("abc")
except Exception as e:
    raise NumberFormatExceptionError()
finally:
    print("code exceuted...")
"""