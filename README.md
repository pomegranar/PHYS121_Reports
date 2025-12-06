# Anar's PHYS 121 Lab Report Template

A simple template for writing lab reports _programmatically_ for anyone taking **Integrated Science - Physics** at Duke Kunshan University.

# Setup Guide

## Prerequisites:

- Python3
- Make
- LaTeX distribution ([TeX Live](https://www.tug.org/texlive/) / [MacTeX](https://www.tug.org/mactex/) / [MiKTeX](https://miktex.org/))
- [Quarto](https://quarto.org/docs/get-started/)

## Steps:

1. Make a fork and clone it.
2. Open the directory in your terminal of choice.
3. Run this command:

   ```bash
   bash create-physics-environment.sh
   ```

   > This creates a python environment in `/.physics`. It's not necessary to activate this environment to build the report, but you should set it as your active python environment to use language support in your code editor.

4. Duplicate the `lab-report-template` directory under a new name, such as `lab-report-1`, and open it in your editor of choice.

## Workflow:

1. Run `make preview` inside the `lab-report-1` directory. This will open a preview inside your web browser that **automatically rebuilds upon save**.
2. All your editing (text, code, metadata) is then done inside the `lab-report.qmd` file.
3. You can then permanently save your file from the preview browser tab.
