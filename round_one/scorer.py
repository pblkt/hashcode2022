#!/usr/bin/env python3
from typing import Any, Dict, NamedTuple, List, Set, Union

from round_one.our_types import Project, Dev, Assignment


def score_solution(
    input: Dict[str, Union[Project, Dev]], assignments: List[Assignment]
) -> int:
    assert is_valid(input, assignments)

    projects: Dict[str, Project] = {
        project.name: project for project in input["projects"]
    }
    devs: Dict[str, Dev] = {dev.name: dev for dev in input["devs"]}
    free_devs = {key for key in devs.keys()}
    running_projects: Dict[str, List[int, Assignment]] = {}

    score = 0
    day = 0
    first_run = True
    while len(running_projects) > 0 or first_run:
        first_run = False

        running_projects_to_remove = set()
        for project_name, project_state in running_projects.values():
            project_start_day, project_assignment = project_state
            # Is DONE?
            if day == project_start_day + projects[project_name].duration:
                # Score
                delay = max(0, day - projects[project_name].best_before)
                project_score = max(0, projects[project_name].score - delay)
                score += project_score
                # level up
                for role, dev in zip(
                    projects[project_name].roles, project_assignment.devs
                ):
                    if dev.skills.get(role.skill, 0) <= role.min_level:
                        if role.skill in dev.skills:
                            dev.skills[role.skill] += 1
                        else:
                            dev.skills[role.skill] = 1
                # Free dev
                free_devs.add(project_assignment.devs)
                # remove running projects
                running_projects_to_remove.add(project_name)

        for running_project_to_remove in running_projects_to_remove:
            running_projects.pop(running_project_to_remove)

        copy_assignments = list()
        for assignment in assignments:
            if set(assignment.devs) <= free_devs:
                # validate assignment
                current_project = projects[assignment.name]
                current_devs = [devs[dev] for dev in assignment.devs]
                if validate_assignment(current_project, current_devs):
                    free_devs = free_devs - set(assignment.devs)
                    running_projects[assignment.name] = [day, assignment]
                else:
                    copy_assignments.append(assignment)
            else:
                copy_assignments.append(assignment)
        assignments = copy_assignments

        day += 1
    return score


def validate_assignment(project: Project, devs: List[Dev]) -> bool:
    assert len(project.roles) == len(devs)

    max_dev_skills = {}
    for dev in devs:
        for skill in dev.skills.keys():
            if skill not in max_dev_skills:
                max_dev_skills[skill] = dev.skills.get(skill, 0)
            else:
                max_dev_skills[skill] = max(
                    max_dev_skills[skill], dev.skills.get(skill, 0)
                )

    for role, dev in zip(project.roles, devs):
        assert role.min_level <= dev.skills.get(role.skill, 0) or (
            (role.min_level == dev.skills.get(role.skill, 0) + 1)
            and (
                role.skill in max_dev_skills
                and role.min_level <= max_dev_skills[role.skill]
            )
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

    # Verify each dev appear only once
    for assignment in assignments:
        assert len(set(assignment.devs)) == len(assignment.devs)

    return True


if __name__ == "__main__":
    pass  # score_solution(input, output)
