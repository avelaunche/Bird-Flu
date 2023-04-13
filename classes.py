class bird1:
  def __init__(self, location, infection_type):
    self.loc = location
    self.infection_type = infection_type
    self.immunity_type = ""
    self.length = 0

class virus:
  def __init__(self, r, deadliness):
    self.R = r
    self.deadliness = deadliness
