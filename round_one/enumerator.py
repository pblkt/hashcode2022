#!/usr/bin/env python3.8
import json
import pathlib
import random
import signal
import string
import sys
from typing import Any, Dict, Tuple, TypeVar

from deserialize import deserialize
from scorer import score_solution
from serialize import serialize
from datetime import datetime

State = TypeVar("State")


def one_solution(problem: Dict[str, Any], state: State) -> Tuple[Dict[str, Any], State]:
    pass  # FIXME


def random_string(length: int) -> str:
    """:return A random string of the required length"""
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(length)
    )


RESULT_PATH = pathlib.Path("enumerator_output")


def main():
    [_me, input_path] = sys.argv
    with open(input_path, "r") as f:
        input = deserialize(f.read())

    max_score = 0
    best_solution = None
    state = None

    def signal_handler(sig, frame):
        RESULT_PATH.mkdir(exist_ok=True)
        print(f"{datetime.now()} - Got Ctrl+C")

        while (output_path := pathlib.Path(input_path) / random_string(3)).exists():
            print(f"{output_path=} exists, trying a different random suffix")

        print(f"Saving to {output_path=} with {max_score=}")
        if not best_solution:
            print("No best solution found")
            return

        try:
            serialized = serialize(best_solution)
        except Exception as e:
            print(f"Encountered exception when serializing: {e}")
            serialized = json.dumps(best_solution)

        with open(output_path, "w") as f:
            f.write(serialized)

        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    print(f"{datetime.now()} - Started running on {input_path}")
    i = 0
    while True:
        print(f"{datetime.now()} - Run #{i} on {input_path}")
        i += 1
        solution, state = one_solution(input, state)
        if score := score_solution(input, solution) > max_score:
            print(f"{datetime.now()} - Score beaten! New score is {score}, last max was {max_score}")
            best_solution = solution
            max_score = score

    signal.pause()


main()
