import filecmp
import functools
import os.path
from pathlib import Path

import numpy as np


def find_different_files(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and
        there were no errors while accessing the directories or files,
        False otherwise.
    """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    (_, mismatch, errors) = filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False
    )
    for fp in mismatch:
        yield fp, Path(dir1), Path(dir2)

    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        yield from find_different_files(new_dir1, new_dir2)


def compare_dicts(*dicts):
    all_keys = functools.reduce(lambda d, keys: set(d).union(keys), dicts, set())
    # all_keys = set(d1.keys()).union(d2.keys())

    all_values = {}

    for k in all_keys:
        vals = []
        for d in dicts:
            value = d.get(k, np.nan)
            vals.append(value)
        all_values[k] = vals
    return all_values
