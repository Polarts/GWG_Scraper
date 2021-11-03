class GunInfocard:
    def __init__(self, category, name, price, count, hull_dmg, shield_dmg, range, speed, rate, energy_usage):
        self.category = category
        self.name = name
        self.price = price
        self.count = count
        self.hull_dmg = hull_dmg
        self.shield_dmg = shield_dmg
        self.range = range
        self.speed = speed
        self.rate = rate
        self.energy_usage = energy_usage

    def __str__(self):
        return self.category +','+\
            self.name +','+\
                self.price +','+\
                    self.count +','+\
                        self.hull_dmg +','+\
                            self.shield_dmg +','+\
                                self.range +','+\
                                    self.speed +','+\
                                        self.rate +','+\
                                            self.energy_usage
