from .models import Phone, Shipping, Receiving, Employee

MODEL_MAP = {
    "Phone": Phone,
    "Shipping": Shipping,
    "Receiving": Receiving,
    "Employee": Employee,
}

AVAILABLE_FIELDS_MAP = {
    "Phone": ["brand", "model"],
    "Shipping": ["destination", "shipped_date"],
    "Receiving": ["received_date"],
    "Employee": ["name"],
}

RELATIONSHIP_MAP = {
    "Shipping": {"phone": "Phone"},
    "Receiving": {"phone": "Phone"},
    "Employee": {""},
    "Phone": {
        "receiving": "Receiving", 
        "shipping": "Shipping"
        },
}
