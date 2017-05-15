# py_agency
# agent
# @author - sidmishraw
# @last_modified - 5/15/17 :: 12:18 AM


"""
An agent in the agency platform
"""

# pystdlib imports ~
from collections import deque
from uuid import uuid4


class Agent(object):
  """
  The agent in the Agent Based platform/architecture framework.

  :class: `agency_framework.Agent`
  """

  def __init__(self):
    """
    initialize the Agent object
    """

    # id
    self.__id = uuid4()

    # description
    self.__description = ""

    # message queue
    self.__mailbox = deque()

    # the facilitator of the agent
    self.__facilatator = None

    # the partner of the agent
    self.__partner = None

    # flag that identifies if the agent is dead
    self.__is_dead = False

    # flag that identifies if the agent is ready
    self.__is_ready = True

    # param map
    self.__params = dict()

  @property
  def description(self):
    """
    description(self) -> `str`

    The description of the agent.

    :return: the description of the agent :class: `str`
    """

    return self.__description

  @description.setter
  def description(self, description=""):
    """
    description(self, description="") -> None

    Sets the description of the agent.

    :param description: the description of the agent, is an empty string by
    default. :class: `str`

    :return: None
    """

    self.__description = description

  @property
  def facilitator(self):
    """
    The facilitator of this agent.

    Default value = None

    :return: facilitator :class: `agency_framework.Facilitator`
    """

    return self.__facilatator

  @facilitator.setter
  def facilitator(self, facilitator=None):
    """
    Sets the facilitator of the agent.

    :param facilitator: The facilitator of the agent :class:
    `agency_framework.Facilitator`

    :return: None
    """

    self.__facilatator = facilitator

  @property
  def partner(self):
    """
    The partner agent of this agent.

    Default value = None

    :return: partner :class: `agency_framework.Agent`
    """

    return self.__partner

  @partner.setter
  def partner(self, partner=None):
    """
    Sets the partner of the agent.

    :param partner: The partner of the agent :class: `agency_framework.Agent`

    :return: None
    """

    self.__partner = partner

  @property
  def isdead(self):
    """
    Is the agent dead? True or False

    Default value = False

    :return: isdead :class: `boolean`
    """

    return self.__is_dead

  @isdead.setter
  def isdead(self, is_dead=False):
    """
    isdead(self, is_dead=False) -> None

    Sets if the agent is dead.

    :param is_dead: the flag that indicates of the agent is dead?

    :return: None
    """

    self.__is_dead = is_dead

  @property
  def isready(self):
    """
    Is the agent ready? True or False

    Default value = True

    :return: self.__is_ready :class: `boolean`
    """

    return self.__is_ready

  @isready.setter
  def isready(self, is_ready=True):
    """
    Sets if the agent is ready.

    :param is_ready: flag indicating if the agent is ready, `True` by default

    :return: None
    """

    self.__is_ready = is_ready

  @property
  def mailbox(self):
    """
    The message queue of the agent where all the incoming messages from its
    partners are stored.

    :return: self.__mailbox :class: `collections.deque`
    """

    return self.__mailbox

  @property
  def id(self):
    """
    The ID of the agent, is an uuid.

    :return: self.__id :class: `uuid.uuid4`
    """

    return self.__id

  # agent behaviors
  def add_message(self, message):
    """
    add_message(self, message) -> None

    Adds the message to the agent's mailbox.

    :param message: the message to be added to the agent's mailbox

    :return: None
    """

    if message is not None:
      print("""Adding the message: {message} to agent: {agent}'s
      mailbox""".format(
          message=message, agent=self.__description))
      self.__mailbox.append(message)
    else:
      print("""The message is not a valid message, it was None""")

  def add_param(self, **params):
    """
    add_param(self, **params) -> None

    Adds the parameters to the agent

    :param params: the parameters for the agent, key-value arguments

    :return: None
    """

    for param_name, param_value in params.items():
      self.__params[param_name] = param_value
