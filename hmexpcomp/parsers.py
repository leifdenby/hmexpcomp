#!/usr/bin/env python
# coding: utf-8
import re

re_bash_variables = re.compile(r"(?P<key>\w+)=(?P<value>[\w\$\{\}\-\/\":]+).*")


def find_bash_variables(filepath):
    """
    Find all variables defined in a bash script and return as a dictionary
    """
    file_content = open(filepath).read()
    variables = dict(re_bash_variables.findall(file_content))
    variables = {
        k: v[1:-2] if v.startswith('"') and v.endswith('"') else v
        for (k, v) in variables.items()
    }
    return variables


FILE_PARSERS = {
    "ecf/config_exp.h": find_bash_variables,
    "progress.log": None,
    "progressPP.log": None,
}
