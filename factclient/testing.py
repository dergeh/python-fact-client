from fact import Fact
from datetime import datetime
import trace_pb2

from factclient.io.ConsoleLogging import ConsoleLogging

io = ConsoleLogging()
Fact.boot({"inlcudeEnvironment": False, "io": io})
Fact.start(None,None)
print(Fact._trace)
print(Fact._provider)
