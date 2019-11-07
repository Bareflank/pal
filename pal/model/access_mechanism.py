import abc


class AbstractAccessMechanism(abc.ABC):
    """ Abstract base class for modeling a particular mechanism in which a """
    """ register can be accessed """

    @abc.abstractmethod
    def is_read(self):
        """ Returns true if the access mechanism performs a read """
        return

    @abc.abstractmethod
    def is_write(self):
        """ Returns true if the access mechanism performs a write """
        return

    @abc.abstractmethod
    def is_memory_mapped(self):
        """ Returns true if the access mechanism is accessed using memory """
        """ memory mapped I/O """
        return False

    @abc.abstractmethod
    def is_valid(self):
        """ Returns true if the access mechanism is valid """
        return
