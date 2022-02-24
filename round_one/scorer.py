#!/usr/bin/env python3
from typing import Any, Dict, NamedTuple, List, Set, Union

from round_one.types import Project, Assignment, Dev


def score_solution(input: Dict[str, Any], output: Dict[str, Any]) -> int:
    if not is_valid(input, output):
        print("Invalid solution")
    return 0

    pass


def validate_assignment(project: Project, devs: Dev) -> bool:
    assert len(project.roles) == len(devs)

    max_dev_skills = {}
    for dev in devs:
        for skill in dev.skills.keys():
            if skill not in max_dev_skills:
                max_dev_skills[skill] = dev.skills[skill]
            else:
                max_dev_skills[skill] = max(max_dev_skills[skill], dev.skills[skill])

    for role, dev in zip(project.roles, devs):
        assert role.min_level <= devs.skills.get(role.skill, 0) or (
            (role.min_level == devs.skills.get(role.skill, 0) + 1)
            and (role.skill in max_dev_skills and role.min_level <= max_dev_skills[role.skill])
        )

    return True


def is_valid(
    input: Dict[str, Union[Project, Dev]], assignments: List[Assignment]
) -> bool:
    projects: Project = input["projects"]
    devs: Dev = input["devs"]

    # Sanity
    output_project_names = [assignment.name for assignment in assignments]
    # Unique project name in output
    assert len(output_project_names) == len(set(output_project_names))
    output_project_names = set(output_project_names)
    output_dev_names = set([assignment.devs for assignment in assignments])

    input_projects_names = set([project.name for project in projects])
    input_dev_names = set([dev.name for dev in devs])
    assert output_dev_names <= input_dev_names
    assert output_project_names <= input_projects_names

    # Unique dev in each project
    for assignment in assignments:
        assert len(set(assignment.devs)) == len(assignment.devs)

    return True


if __name__ == "__main__":
    pass  # score_solution(input, output)
