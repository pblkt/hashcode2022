#!/usr/bin/env python3.8
import sys
from importlib import import_module

from deserialize import deserialize
from scorer import score_solution
from serialize import serialize

import sys
sys.path.append("..")


def main():
    input_path, solver_module_name = sys.argv[1:]
    solver_module = import_module(f"solvers.{solver_module_name}")
    with open(input_path, "r") as f:
        input = deserialize(f.read())
    with open(input_path, "r") as f:
        copy_input = deserialize(f.read())

    solved = solver_module.solve(input)
    score = score_solution(copy_input, solved)
    print(f"score: {score}")
    serialized = serialize(solved)

    with open(input_path.replace("input", "output"), "w") as f:
        f.write(serialized)


main()
