#!/usr/bin/env python3
from typing import Any, Dict


def score_solution(input: Dict[str, Any], output: Dict[str, Any]) -> int:
    if not is_valid(input, output):
        print("Invalid solution")
    return 0

    pass


def is_valid(input: Dict[str, Any], output: Dict[str, Any]) -> bool:
    return True
