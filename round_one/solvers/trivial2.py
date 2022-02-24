#!/usr/bin/env python3.8
import random
from typing import Dict, Any, List

from round_one.our_types import Input, Assignment
from round_one.scorer import validate_assignment


def solve(input: Input) -> List[Assignment]:
    assignments = list()
    projects = input.projects
    while len(projects) > 0:
        project = random.choice(projects)
        # for each role - find min skill dev to do it
        # [if not found dev, check if we hav a mentor]
        assigned_devs = []
        for role in project.roles:
            for dev in input.devs:
                if dev not in assigned_devs:
                    relevant_mentor = False
                    for a_dev in assigned_devs:
                        if a_dev.skills.get(role.skill, 0) >= role.min_level:
                            relevant_mentor = True
                            break

                    if dev.skills.get(role.skill, 0) >= role.min_level or (
                        relevant_mentor
                        and dev.skills.get(role.skill, 0) + 1 == role.min_level
                    ):
                        assigned_devs.append(dev)
        # assert len(assigned_devs) == len(project.roles)

        if validate_assignment(project, assigned_devs):
            projects.remove(project)
            assignments.append(Assignment(project.name, [dev.name for dev in assigned_devs]))

            # level up
            for role, dev in zip(project.roles, assigned_devs):
                if dev.skills.get(role.skill, 0) <= role.min_level:
                    if role.skill in dev.skills:
                        dev.skills[role.skill] += 1
                    else:
                        dev.skills[role.skill] = 1
    return assignments
