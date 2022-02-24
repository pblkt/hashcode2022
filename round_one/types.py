#!/usr/bin/env python3.8
from typing import Dict, List, NamedTuple


class Project(NamedTuple):
    name: string
    duration: int
    best_before: int
    score: int
    roles: List[Role]


class Dev(NamedTuple):
    name: string
    skills: Dict[str, int]


class ProjStart(NamedTuple):
    name: str
    dev_names: List[str]
