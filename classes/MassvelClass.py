class massobj:
    def __init__(self, mass, vel):
        self.mass = mass
        self.vel = vel
        self.mv = mass * vel
        self.ke = mass * vel * vel / 2
