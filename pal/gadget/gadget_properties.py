import abc

class GadgetProperties(abc.ABC):
    """ Base class that represents properties for a gadget """
    @property
    @abc.abstractmethod
    def gadget_name(self):
        """ The name of the gadget these properties apply to """
        pass
