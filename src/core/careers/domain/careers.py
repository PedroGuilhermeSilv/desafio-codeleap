from dataclasses import dataclass, field
from datetime import datetime

MAX_LENGTH = 50


@dataclass
class Career:
    id: int = 0
    username: str = ""
    title: str = ""
    content: str = ""
    created_datetime: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.username) > MAX_LENGTH:
            raise ValueError("Username is too long")
        if not self.username:
            raise ValueError("Username is required")
        if not self.title:
            raise ValueError("Title is required")
        if not self.content:
            raise ValueError("Content is required")

    def __eq__(self, other):
        """Initially this class only checks if the instances are at
        the same memory address. We need to compare the id."""
        if not isinstance(other, Career):
            raise ValueError("Comparison between different classes")
        return self.id == other.id

    def update(self, content: str, title: str):
        self.content = content
        self.title = title
        self.validate()
