#!/usr/bin/env python3
from typing import Any, Dict, NamedTuple, List, Set, Union


class Assingment(NamedTuple):
    name: str
    devs: Set[str]

class Devs(NamedTuple):
    name: str
    skills: Dict[str, int]


class Requirement(NamedTuple):
    skill: str
    min_level: int


class Projects(NamedTuple):
    name: str
    duration: int
    best_before: int
    score: int
    roles: List[Requirement]



def score_solution(input: Dict[str, Any], output: Dict[str, Any]) -> int:
    if not is_valid(input, output):
        print("Invalid solution")
    return 0

    pass


def is_valid(input: Dict[str, Union[Projects, Devs]], output: Dict[str, List[Assingment]]) -> bool:
    return True

if __name__ == "__main__":
    pass # score_solution(input, output)