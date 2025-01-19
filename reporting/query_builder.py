from django.db.models import Q, F
from .reporting_query_configurations import MODEL_MAP, AVAILABLE_FIELDS_MAP, RELATIONSHIP_MAP

def build_dynamic_query(config):

    # Validate the table
    table = config.get("table")
    if table not in MODEL_MAP:
        raise ValueError(f"Invalid table: {table}")

    Model = MODEL_MAP[table]
    queryset = Model.objects.all()

    # Apply filters
    filters = config.get("filters", [])
    for filter_item in filters:
        field = filter_item.get("field")
        operator = filter_item.get("operator")
        value = filter_item.get("value")

        if operator == "equals":
            queryset = queryset.filter(**{field: value})
        elif operator == "gt":
            queryset = queryset.filter(**{f"{field}__gt": value})
        elif operator == "lt":
            queryset = queryset.filter(**{f"{field}__lt": value})
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    # Select related fields (cross-table)
    fields = config.get("fields", [])
    valid_fields = AVAILABLE_FIELDS_MAP[table] + [
        f"{related_field}__{field}"
        for related_field, related_model in RELATIONSHIP_MAP.get(table, {}).items()
        for field in AVAILABLE_FIELDS_MAP[related_model]
    ]

    print(f"The valid fields: {valid_fields}")

    for field in fields:
        if field not in valid_fields:
            print(f"Field received: {field}")
            raise ValueError(f"Invalid field: {field}")

    queryset = queryset.values(*fields)

    return queryset
