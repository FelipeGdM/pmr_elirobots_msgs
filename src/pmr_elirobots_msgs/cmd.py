from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from typing import Optional

from pmr_elirobots_msgs.header import Header


@dataclass_json
@dataclass
class JointCommand:
    """Position command to robot joints"""

    joint1: Optional[float] = None
    joint2: Optional[float] = None
    joint3: Optional[float] = None
    joint4: Optional[float] = None
    joint5: Optional[float] = None
    joint6: Optional[float] = None

    def to_json(self):
        pass

    def from_json(self):
        pass


@dataclass_json
@dataclass
class JointCommandMsg:
    """Joint command with message header"""

    cmd: JointCommand
    header: Header = Header()

    def to_json(self):
        pass

    def from_json(self):
        pass
