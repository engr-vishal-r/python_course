class MethodDemo:

    def instance_method(self):
        print("Called Instance Method")

    @classmethod
    def class_method(cls):
        print("Called Class Method")
    
    @staticmethod
    def static_method(a,b):
        print("Called Static Method")
        return a+b

obj=MethodDemo()
obj.instance_method()

MethodDemo.class_method()
print(f"Static Method output ---> ",MethodDemo.static_method(2,3))
