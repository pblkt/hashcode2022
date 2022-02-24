#!/usr/bin/env python3.8
import sys
from pprint import pprint

from our_types import Dev, Input, Project, Requirement


def deserialize(input: str) -> Input:
    lines = input.split("\n")
    line = 0

    head, *tail = lines
    line += 1

    devs_to_parse, projs_to_parse = map(int, head.split(" "))

    result = Input()

    while devs_to_parse:
        devs_to_parse -= 1

        head, *tail = tail
        line += 1

        name, skills_to_parse_str = head.split(" ")
        skills_to_parse = int(skills_to_parse_str)
        dev = Dev(name=name)

        while skills_to_parse:
            skills_to_parse -= 1

            head, *tail = tail
            line += 1

            skill, level_str = head.split(" ")
            dev.skills[skill] = int(level_str)

        result.devs.append(dev)

    while projs_to_parse:
        projs_to_parse -= 1

        head, *tail = tail
        line += 1

        name, *nums = head.split(" ")
        duration, score, best_before, num_roles_to_parse = map(int, nums)
        project = Project(
            name=name, duration=duration, best_before=best_before, score=score
        )

        while num_roles_to_parse:
            num_roles_to_parse -= 1

            head, *tail = tail
            line += 1

            skill, level_str = head.split(" ")
            project.roles.append(Requirement(skill, int(level_str)))

        result.projects.append(project)

    return result


if "__main__" == __name__:
    with open(sys.argv[1], "r") as f:
        pprint(deserialize(f.read())._asdict())
