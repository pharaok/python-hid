from __future__ import annotations
from collections.abc import Iterable
from enum import IntEnum, IntFlag, auto
from typing import Any, Optional

from . import BaseFlagItem, BaseItem
from hid.helpers import flatten, ConvertibleToBytes


class DataFlag(IntFlag):
    DATA = 0x00
    ARRAY = 0x00
    ABSOLUTE = 0x00
    NO_WRAP = 0x00
    LINEAR = 0x00
    PREFERRED_STATE = 0x00
    NO_NULL_POSITION = 0x00
    NON_VOLATILE = 0x00
    BIT_FIELD = 0x00
    CONSTANT = auto()
    VARIABLE = auto()
    RELATIVE = auto()
    WRAP = auto()
    NON_LINEAR = auto()
    NO_PREFERRED = auto()
    NULL_STATE = auto()
    VOLATILE = auto()
    BUFFER = auto()


class CollectionType(IntEnum):
    PHYSICAL = 0x00
    APPLICATION = auto()
    LOGICAL = auto()
    REPORT = auto()
    NAMED_ARRAY = auto()
    USAGE_SWITCH = auto()
    USAGE_MODIFIER = auto()


class BaseMainItem(BaseItem):
    pass


class Input(BaseFlagItem, BaseMainItem):
    PREFIX = 0b10000000


class Output(BaseFlagItem, BaseMainItem):
    PREFIX = 0b10010000


class Feature(BaseFlagItem, BaseMainItem):
    PREFIX = 0b10110000


class Collection(BaseMainItem):
    PREFIX = 0b10100000

    def __new__(cls, prefix_data: Optional[ConvertibleToBytes], content: Optional[Iterable[Any]] = None) -> Collection:
        obj = super().__new__(cls, prefix_data)
        b = bytes(obj)
        if content:
            b += bytes(flatten(content))
            b += CollectionEnd()
        return bytes.__new__(cls, b)


class CollectionEnd(BaseMainItem):
    PREFIX = 0b11000000

    def __new__(cls) -> CollectionEnd:
        return super().__new__(cls)


class BaseGlobalItem(BaseItem):
    pass


class UsagePage(BaseGlobalItem):
    PREFIX = 0b00000100


class LogicalMinimum(BaseGlobalItem):
    PREFIX = 0b00010100


class LogicalMaximum(BaseGlobalItem):
    PREFIX = 0b00100100


class PhysicalMinimum(BaseGlobalItem):
    PREFIX = 0b00110100


class PhysicalMaximum(BaseGlobalItem):
    PREFIX = 0b01000100


class UnitExponent(BaseGlobalItem):
    PREFIX = 0b01010100


class Unit(BaseGlobalItem):
    PREFIX = 0b01110100


class ReportSize(BaseGlobalItem):
    PREFIX = 0b01110100


class ReportID(BaseGlobalItem):
    PREFIX = 0b10000100


class ReportCount(BaseGlobalItem):
    PREFIX = 0b10010100


class Push(BaseGlobalItem):
    PREFIX = 0b10100100


class Pop(BaseGlobalItem):
    PREFIX = 0b10110100


class BaseLocalItem(BaseItem):
    pass


class Usage(BaseLocalItem):
    PREFIX = 0b00001000


class UsageMinimum(BaseLocalItem):
    PREFIX = 0b00011000


class UsageMaximum(BaseLocalItem):
    PREFIX = 0b00101000


class DesignatorIndex(BaseLocalItem):
    PREFIX = 0b00111000


class DesignatorMinimum(BaseLocalItem):
    PREFIX = 0b01001000


class DesignatorMaximum(BaseLocalItem):
    PREFIX = 0b01011000


class StringIndex(BaseLocalItem):
    PREFIX = 0b01111000


class StringMinimum(BaseLocalItem):
    PREFIX = 0b10001000


class StringMaximum(BaseLocalItem):
    PREFIX = 0b10011000


class Delimiter(BaseLocalItem):
    PREFIX = 0b10101000
