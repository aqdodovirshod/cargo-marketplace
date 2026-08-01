class DomainError(Exception):
    code: str = "domain_error"


class DomainValidationError(DomainError):
    code = "domain_validation_error"


class BusinessRuleViolation(DomainError):
    code = "business_rule_violation"


class EntityNotFoundError(DomainError):

    def __init__(self, entity_name: str, entity_id: object):
        self.entity_name = entity_name
        self.entity_id = entity_id
        super().__init__(f"{entity_name} с id={entity_id} не найден(а)")


class ConcurrencyConflictError(DomainError):
    code = "concurrency_conflict"