from typing import Tuple, Optional

from round_one.our_types import *


class LiveDev(NamedTuple):
    name: str
    skills: Dict[str, int]
    used_until: int = -1


def is_dev_helpful_without_mentor(project_reqs: List[Requirement], dev: LiveDev):
    project_reqs_copy = project_reqs.copy()

    for proj_req in project_reqs_copy:
        # If is helpful
        if dev.skills.get(proj_req.skill, 0) >= proj_req.min_level:
            # Remove the skills
            project_reqs.remove(
                [
                    req for req in project_reqs
                    if req.skill == proj_req.skill
                ][0]
            )
            return True

    return False


def is_dev_helpful_with_mentor(project: Project, dev: LiveDev):
    return any(
        dev.skills.get(role.skill, 0) + 1 >= role.min_level
        for role in project.roles
    )


def find_devs_for_project(project: Project, avail_devs: List[LiveDev]) -> Optional[List[LiveDev]]:
    assigned_devs = []
    left_requirements_to_fill = project.roles.copy()

    for dev in avail_devs:
        if is_dev_helpful_without_mentor(left_requirements_to_fill, dev):
            assigned_devs.append(dev)

        if not left_requirements_to_fill:
            return assigned_devs

        # TODO Mentorship
    else:
        return None


def solve(input: Input):
    projects = input.projects
    input_devs = input.devs

    sorted_by_score = sorted(projects, key=lambda p: p.score)
    devs = [LiveDev(d.name, d.skills) for d in input_devs]
    output: List[Dict[str, List[str]]] = []
    cur_time = 0
    assignees = None

    project_idx = 0
    while not assignees:
        project = sorted_by_score[project_idx]

        print("Checking proj", project.name)
        available_devs = [d for d in devs if d.used_until < cur_time]
        assignees = find_devs_for_project(project, available_devs)

        # TODO Other rpojects, concurrent and next time
        if not assignees:
            print("Didn't find devs :////")
            cur_time += 1
        else:
            print("Found devs!", assignees)
            for assignee in assignees:
                assignee.used_until = cur_time + project.duration

            project_idx += 1

            output.append({
                "name": project.name,
                "devs": [d.name for d in assignees]
            })

    return output