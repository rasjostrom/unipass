
class Descriptor(object):
    """
    Simple descriptor class.
    """
    def __init__(self, label):
        self.label = label
        
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.label)
    
    def __set__(self, instance, value):
        instance.__dict__[self.label] = value


class GetDescriptor(object):
    """
    Simple get descriptor class.
    """
    def __init__(self, label):
        self.label = label
        
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.label)
        
