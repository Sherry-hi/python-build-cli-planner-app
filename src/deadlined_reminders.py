from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable,metaclass=ABCMeta):

    def __iter__(self):
        return self
    
    @abstractmethod
    def is_due(self):
        pass
    
    def __subclasscheck__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented
    
class DeadlinedReminder(ABC):
    
    def __iter__(self):
        return self
        
    @abstractmethod
    def is_due(self):
        pass
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text
        
    def is_due(self):
        if self.date <= datetime.now():
            return True
        else:
            return False

    def __iter__(self):
        return iter([self.text,self.date.isoformat()])
    