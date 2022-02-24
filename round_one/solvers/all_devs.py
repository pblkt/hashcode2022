#!/usr/bin/env python3.8
from typing import List

from round_one.our_types import Assignment, Input


def solve(input: Input) -> List[Assignment]:
    return [Assignment(name=proj.name, devs=input.devs) for proj in input.projects]
