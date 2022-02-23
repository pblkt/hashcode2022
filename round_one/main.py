#!/usr/bin/env python3
import sys
from importlib import import_module

from deserialize import deserialize
from serialize import serialize


def main():
    solver_module_name, input_path = sys.argv[1:]
    solver_module = import_module(f"solvers.{solver_module_name}")
    with open(input_path, "r") as f:
        input = deserialize(f.read())

    solved = solver_module.solve(input)
    serialized = serialize(solved)

    with open(input_path.replace("input", "output"), "w") as f:
        f.write(serialized)


main()
