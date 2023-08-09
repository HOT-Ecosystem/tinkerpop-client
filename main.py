"""Tinkerpop client

https://tinkerpop.apache.org/docs/current/reference/#gremlin-python

TODO's
  1. Think of some examples
  2. Think of some example cases
"""
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __, has, out, valueMap

CONNECTION_URL = 'ws://localhost:8182/gremlin'


def connect():
    """Connect to graph"""
    g = traversal().with_remote(DriverRemoteConnection(CONNECTION_URL,'g'))
    return g


def run():
    """Run"""
    g = connect()
    ex1 = g.V().has("id", "4027255").repeat(out('parent')).emit().as_('x').repeat(__.in_('parent')).emit(
        has("id", "43530856")).select('x').by(valueMap("id")).limit(5)
    # ex1_result = [v for v in ex1]
    for v in ex1:
        print(v)
    # {'id': ['321588']}
    # {'id': ['134057']}
    print()


if __name__ == '__main__':
    run()
