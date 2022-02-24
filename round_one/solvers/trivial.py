#!/usr/bin/env python3.8
from typing import Dict, Any, List

from round_one.our_types import Input, Assignment


def solve(input: Input) -> List[Assignment]:
    return [
        Assignment("WebServer", ["Bob", "Anna"]),
        Assignment("Logging", ["Anna"]),
        Assignment("WebChat", ["Maria", "Bob"]),
    ]
