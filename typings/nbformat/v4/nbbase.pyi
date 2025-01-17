"""
This type stub file was generated by pyright.
"""

"""Python API for composing notebook elements

The Python representation of a notebook is a nested structure of
dictionary subclasses that support attribute access.
The functions in this module are merely helpers to build the structs
in the right form.
"""
from typing import Any

import nbformat

def validate(node, ref=...):  # -> None:
    """validate a v4 node"""
    ...

def new_output(output_type, data=..., **kwargs):  # -> NotebookNode:
    """Create a new output, to go in the ``cell.outputs`` list of a code cell."""
    ...

def output_from_msg(msg):  # -> NotebookNode:
    """Create a NotebookNode for an output from a kernel's IOPub message.

    Returns
    -------
    NotebookNode: the output as a notebook node.

    Raises
    ------
    ValueError: if the message is not an output message.

    """
    ...

def new_code_cell(source=..., **kwargs):  # -> NotebookNode:
    """Create a new code cell"""
    ...

def new_markdown_cell(source: str = ..., **kwargs: Any) -> nbformat.NotebookNode:
    """Create a new markdown cell"""
    ...

def new_raw_cell(source=..., **kwargs):  # -> NotebookNode:
    """Create a new raw cell"""
    ...

def new_notebook(**kwargs):  # -> NotebookNode:
    """Create a new notebook"""
    ...
