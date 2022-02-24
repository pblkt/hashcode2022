#!/usr/bin/env python3.8
from typing import List

from round_one.our_types import Assignment, Input


def solve(input: Input) -> List[Assignment]:
    projs = sorted(
        input.projects,
        # add weights to the levels by rarity?
        key=lambda proj: proj.score / sum(y.min_level for y in proj.roles),
    )

    result = []

    devs = sorted(input.devs, key=lambda dev: sum(dev.skills.values()))

    while projs:
        proj = projs.pop()
        roles = sorted(
            proj.roles,
            key=lambda req: req.min_level,
        )

        assignment = set()

        while roles:
            role = roles.pop()
            # add availability?
            for dev in devs:
                if (
                    dev.name not in assignment
                    and dev.skills.get(role.skill, 0) >= role.min_level
                ):
                    assignment.add(dev.name)
                    break

        result.append(Assignment(name=proj.name, devs=list(assignment)))

    return result
