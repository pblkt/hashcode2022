from types import *


class LiveDev(NamedTuple):
    name: str
    skills: Dict[str, int]
    used_until: int = -1


def assign_project(project: Project, devs: List[LiveDev], time: int) -> List[LiveDev]:
    roles = project.roles
    assigned = []
    for dev in devs:
        for skill in roles:
            pass



def naive_sol(projects: List[Project], input_devs: List[Dev]):
    sorted_by_score = sorted(projects, key=lambda p: p.score)
    devs = [LiveDev(d.name, d.skills) for d in input_devs]
    output: List[Dict[str, List[str]]] = []
    time = 0
    assigned = None
    project_idx = 0
    while not assigned:
        project = sorted_by_score[project_idx]
        available_devs = [d for d in devs if d.used_until < time]
        assigned = assign_project(project, available_devs, time)
        if not assigned:
            time += 1
        else:
            output.append({
              "name": project.name,
              "devs": [d.name for d in assigned]
            })



