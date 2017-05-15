# py_agency
# facilitator
# @author - sidmishraw
# @last_modified - 5/15/17 :: 12:18 AM


"""
The facilitator of the agency framework.
"""

# pystdlib imports ~
from collections import deque

class Facilitator(object):
  """
  Facilitator of agents in the agency platform.

  :class: `agency_framework.Facilitator`
  """

  def __init__(self):
    """
    facilitator initializer
    """

    # flag for multithread, True by default
    self.__multithread = True
    self.__free_agents = deque()
    self.__booked_agents = deque()
    self.__params = dict()


