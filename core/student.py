from typing import Optional
from core.client import GradescopeClient


class GradescopeStudent:
    def __init__(
        self,
        client: GradescopeClient,
        user_id: str,
        full_name: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        sid: Optional[str] = None,
        email: Optional[str] = None,
    ) -> None:
        self.client = client
        self.user_id = user_id
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.sid = sid
        self.email = email