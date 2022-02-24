#!/usr/bin/env python3.8
from collections import defaultdict
from typing import List

from ..our_types import Assignment, Input


def solve(input: Input) -> List[Assignment]:
    projs = sorted(
        input.projects,
        # add weights to the levels by rarity?
        key=lambda proj: proj.score / sum(y.min_level for y in proj.roles),
    )

    result = []
    while projs:
        proj = projs.pop()
        roles = sorted(
            proj.roles,
            key=lambda req: req.min_level,
        )

        while roles:
            role = roles.pop()



    # add availability?
