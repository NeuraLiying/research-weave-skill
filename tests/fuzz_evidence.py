"""Seeded JSON-field mutations. These test crash resistance, not semantic correctness."""
import argparse
import copy
import importlib.util
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fuzz_checker", ROOT / "skills/research-weave/scripts/check_evidence.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
VALUES = [None, 1, True, [], {}, "x", ["x"], {"a": 1}, [None], [[1]], 1.5, "https://[", float("inf")]


def paths(value, prefix=()):
    if prefix:
        yield prefix
    if isinstance(value, dict):
        for key, child in value.items():
            yield from paths(child, prefix + (key,))
    elif isinstance(value, list):
        for key, child in enumerate(value):
            yield from paths(child, prefix + (key,))


def mutate(base, count=20000, seed=0):
    rng = random.Random(seed)
    locations = list(paths(base))
    for _ in range(count):
        data = copy.deepcopy(base)
        path = rng.choice(locations)
        cursor = data
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = copy.deepcopy(rng.choice(VALUES))
        result = CHECKER.check(data)
        assert isinstance(result, tuple) and len(result) == 2
        assert all(isinstance(x, list) for x in result)
    return len(locations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--count", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    locations = mutate(json.loads(args.evidence.read_text(encoding="utf-8")), args.count, args.seed)
    print(f"{args.count} seeded mutations over {locations} paths: no crashes (not a correctness score).")
