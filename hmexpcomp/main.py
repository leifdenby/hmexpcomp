import os
import warnings
from pathlib import Path

import pandas as pd

from .parsers import FILE_PARSERS
from .utils import compare_dicts, find_different_files


def can_read(fp):
    return os.access(fp, os.R_OK)


def compare_harmonie_experiments(paths):
    if isinstance(paths, dict):
        named_paths = paths
    else:
        fp_common = os.path.commonpath(paths)
        names = [Path(path).relative_to(fp_common) for path in paths]
        named_paths = dict(zip(names, paths))

    no_read_access = [path for path in paths if not can_read(path)]
    if len(no_read_access) > 0:
        no_read_str = "\n\t".join([str(fp) for fp in no_read_access])
        warnings.warn(
            "Skipping the following paths because you don't have read"
            f" access: {no_read_str}",
        )

        named_paths = {
            name: path
            for (name, path) in named_paths.items()
            if path not in no_read_access
        }

    path_tuples = list(named_paths.items())
    reference_path_tuple = path_tuples[0]
    refp_name, refp = reference_path_tuple
    other_paths = path_tuples[1:]

    diff_fps = []

    for otherp_name, otherp in other_paths:
        different_files = find_different_files(refp, otherp)

        for fname, refp_fp, otherp_fp in different_files:
            rel_fp = refp_fp.relative_to(refp)
            diff_fp = rel_fp / fname
            if diff_fp not in diff_fps:
                diff_fps.append(diff_fp)

    all_diffs = {}

    for diff_fp in diff_fps:
        try:
            file_parser = FILE_PARSERS[str(diff_fp)]
        except KeyError:
            warnings.warn(
                f"Skipping `{diff_fp}` because no parser is defined for this file"
            )

        if file_parser is None:
            continue

        exp_names = list(named_paths.keys())

        exps_params = [
            file_parser(named_paths[exp_name] / diff_fp) for exp_name in exp_names
        ]

        file_diffs = compare_dicts(*exps_params)

        df = pd.DataFrame(file_diffs).transpose()
        df.columns = exp_names
        all_diffs[str(diff_fp)] = df

    return all_diffs
