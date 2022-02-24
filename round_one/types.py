#!/usr/bin/env python3.8
from typing import Dict, List, NamedTuple, Set


class Assignment(NamedTuple):
    name: str
    devs: Set[str]


class Devs(NamedTuple):
    name: str
    skills: Dict[str, int]
    used_until: int = 0


class Requirement(NamedTuple):
    skill: str
    min_level: int


class Project(NamedTuple):
    name: str
    duration: int
    best_before: int
    score: int
    roles: List[Requirement]
