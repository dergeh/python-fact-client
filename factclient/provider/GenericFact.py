import os

import factclient.trace_pb2 as trace
from google.protobuf import duration_pb2 as durationpb
from datetime import datetime

def uptime():  
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds

class GenericFact(object):

    def collect(self, trace: trace.Trace, context):
        elat = (datetime.now()-trace.StartTime.ToDatetime()).total_seconds()
        trace.ExecutionLatency = durationpb.FromSeconds(elat)

        return trace

    def init(self, trace: trace.Trace, context=None):
        if trace is None:
            raise ValueError("trace is None")
        trace.Platform = 'UKN'
        uptime = uptime()
        trace.HostID = "H_%d"%uptime
        trace.Tags["uptime"] = uptime