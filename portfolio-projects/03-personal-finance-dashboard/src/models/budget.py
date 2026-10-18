"""Budget model."""


class Budget:
    def __init__(self, category, monthly_limit):
        self.category = category
        self.monthly_limit = float(monthly_limit)

    def to_dict(self):
        return {"category": self.category, "monthly_limit": self.monthly_limit}

    @classmethod
    def from_dict(cls, data):
        return cls(category=data["category"], monthly_limit=data["monthly_limit"])
