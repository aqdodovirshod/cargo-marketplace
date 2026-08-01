from __future__ import annotations

import abc
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, ClassVar
from uuid import UUID


class Entity(abc.ABC):

    id: int | None 

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        if self.id is None or other.id is None:
            return self is other
        return self.id == other.id

    def __hash__(self) -> int:
        return hash((self.__class__, self.id))


@dataclass(frozen=True)
class ValueObject(abc.ABC):
    pass


@dataclass
class DomainEvent(abc.ABC):
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    event_name: ClassVar[str] = "domain_event"


class AggregateRoot(Entity):

    def __init__(self) -> None:
        self._domain_events: list[DomainEvent] = []

    def add_domain_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        events = self._domain_events[:]
        self._domain_events.clear()
        return events