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
    
class DeadlinedReminder(ABC):
    
    def __iter__(self):
        return self
        
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text
        
    def is_due(self):
        if self.date <= datetime.now():
            return True
        else:
            return False
