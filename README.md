# python-fact-client

Python client for the [fact](https://github.com/faas-facts/fact) library.

## Usage
import the factclient module in your FaaS-function code and use the provided methods to generate 
insights for your function execution.

First start the fact client with your config using `Fact.boot`. After the fact client has been started, it can be used to start, update and close traces 
using `Fact.start`, `Fact.update` and `Fact.done`. Each of these functions take a context object to identify the trace.

An example implementation can be found [here](https://github.com/faas-facts/fact/tree/main/examples/python-aws).
## Config

The config object for the client is a python dictionary with the following options:
+ send_on_update --> bool to specifiy if a message should be send on every phase change in the function 
+ inlcudeEnvironment --> bool if the function environment should be logged to the trace
+ lazy_loading --> bool to activate lazy loading
+ io --> IO object the fact client uses to send their logs to(ConsoleLogging or TCPSender are currently supported) 

### TCP config
Port and address for the TCP sender are set through environment variables this needs to be done in the runtime
environment of the function. Set `fact_tcp_address` and `fact_tcp_port` to your match your log server's. 