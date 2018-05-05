#! /usr/bin/env python3

from typing import *

def __flatten(d: Any, force: bool = False, json: bool = True) -> Any:
    def flatten_safe(d: Any) -> bool:
        if isinstance(d, dict):
            for v in d.values():
                flatten_safe(v)

            return False

        if isinstance(d, list):
            if all(flatten_safe(v) for v in d):
                safeids.add(id(d))
                return True

            return False

        return True


    def issafe(d: Any) -> bool:
        return id(d) in safeids or not isinstance(d, dict) and not isinstance(d, list)


    def jsonpath(path: Tuple) -> str:
        return '.'.join(
            "{}[{}]".format(
                k[0] or '',
                "][".join(map(str, k[1:]))
            ) if isinstance(k, tuple) else k
            for k in path
        )


    def flatten_act(d: Any, path: Tuple) -> Iterable[Tuple[Any, Any]]:
        if isinstance(d, dict):
            for k, v in d.items():
                yield from flatten_act(v, path + (k,))
        elif isinstance(d, list) and not issafe(d):
            k = path[-1] if len(path) else (None,)
            for i, v in enumerate(d):
                yield from flatten_act(v, path[:-1] + (
                    (k + (i,) if isinstance(k, tuple) else (k, i)),
                ))
        else:
            yield (
                (
                    path[0] if len(path) == 1 and not isinstance(path[0], tuple)
                    else (jsonpath(path) if json else path)
                ),
                d
            )


    if not json and not isinstance(d, dict):
        raise ValueError

    safeids: Set[int] = set()

    if not force:
        flatten_safe(d)

    if json and issafe(d):
        return d

    return dict(flatten_act(d, tuple()))


def flatten(data: Any, force: bool = False) -> Any:
    return __flatten(data, force=force, json=True)
