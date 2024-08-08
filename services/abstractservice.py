from abc import ABC, abstractmethod


# TODO bets way? 
class AbstractService(ABC): 
  def __init__(self) -> None:
        pass

  @abstractmethod
  def get_user(self, user_id: int) -> dict:
        pass
