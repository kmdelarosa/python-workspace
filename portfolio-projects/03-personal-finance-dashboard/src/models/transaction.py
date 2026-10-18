"""Transaction model."""
from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, date, category, amount, description, transaction_type="expense"):
        self.id = transaction_id
        self.date = date if isinstance(date, str) else date.strftime("%Y-%m-%d")
        self.category = category
        self.amount = float(amount)
        self.description = description
        self.type = transaction_type  # "expense" or "income"

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "type": self.type,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            transaction_id=data["id"],
            date=data["date"],
            category=data["category"],
            amount=data["amount"],
            description=data["description"],
            transaction_type=data.get("type", "expense"),
        )
