"""Defines a markdown output handler for STACS.

SPDX-License-Identifier: BSD-3-Clause
"""

from typing import List

from stacs import model
from stacs.exceptions import NotImplementedException


def render(findings: List[model.finding.Entry], pack: model.pack.Format) -> str:
    return NotImplementedException("Markdown output not yet implemented, sorry!")
