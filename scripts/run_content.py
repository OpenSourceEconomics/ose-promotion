#!/usr/bin/env python
"""This script compiles the content of the repository."""
import subprocess as sp
import argparse
import shutil
import os


def compile_material(task):

    os.chdir(os.environ["PROJECT_DIR"] + f"/{task}")

    [
        sp.check_call([cmd, "main"])
        for cmd in ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
    ]

    os.chdir(os.environ["PROJECT_DIR"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Create material for OSE promotion")

    parser.add_argument("-s", "--slides", action="store_true", help="create slides")

    parser.add_argument("-p", "--paper", action="store_true", help="create paper")

    args = parser.parse_args()

    if args.paper:

        compile_material("paper")

        shutil.copy("paper/main.pdf", "ose-paper.pdf")

    if args.slides:

        compile_material("slides")

        shutil.copy("slides/main.pdf", "ose-slides.pdf")
