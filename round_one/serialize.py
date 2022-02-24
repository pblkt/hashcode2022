#!/usr/bin/env python3.8
from typing import List

from our_types import Assignment


def serialize(solution: List[Assignment]) -> str:
    result = [str(len(solution))]
    for assignment in solution:
        result.append(assignment.name)
        result.append(" ".join(assignment.devs))

    return "\n".join(result)


TESTCASE = [
    Assignment(name="WebServer", devs=["Bob", "Anna"]),
    Assignment(name="Logging", devs=["Anna"]),
    Assignment(name="WebChat", devs=["Maria", "Bob"]),
]

if "__main__" == __name__:
    print(serialize(TESTCASE))
