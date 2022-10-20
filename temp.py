class Temp:
  
  def __init__(self) -> None:
    pass
  
  @staticmethod
  def sum(x:int, y:int) -> int:
    return x+y
  
  @classmethod
  def mul(cls, x:int, y:int) -> int:
    return x*y
  
  @property
  def div(self, x:int, y:int) -> int:
    return x//y
