import abc
import factclient.trace_pb2 as trace


class PlatformFact(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'init') and
                callable(subclass.init) and
                hasattr(subclass, 'collect') and
                callable(subclass.collect) or
                NotImplemented)

    @abc.abstractmethod
    def init(self, trace: trace.Trace, context=None):
        """init trace"""
        raise NotImplementedError

    @abc.abstractmethod
    def collect(self, trace: trace.Trace, context):
        """collect the trace"""
        raise NotImplementedError
