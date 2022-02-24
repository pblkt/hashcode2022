#!/usr/bin/env python3.8
from typing import Dict, List, NamedTuple


class Assignment(NamedTuple):
    name: str
    devs: List[str]


class Dev(NamedTuple):
    name: str
    skills: Dict[str, int] = {}


class Requirement(NamedTuple):
    skill: str
    min_level: int


class Project(NamedTuple):
    name: str
    duration: int
    best_before: int
    score: int
    roles: List[Requirement] = []


class Input(NamedTuple):
    projects: List[Project]
    devs: List[Dev]
