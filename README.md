# Anar's PHYS 121 Lab Report Template

A simple template for writing lab reports _programmatically_ for anyone taking **Integrated Science - Physics** at Duke Kunshan University.

# Setup Guide

## Prerequisites:

### Required Software:

- **Python 3.8+** - For running analysis code and Jupyter notebooks
- **Make** - For building the reports (usually pre-installed on Linux/macOS)
- **LaTeX Distribution** - For PDF generation and plot text rendering
  - **Linux**: Install TeX Live via your package manager
    ```bash
    # Ubuntu/Debian
    sudo apt-get install texlive-latex-extra texlive-fonts-recommended

    # Fedora/RHEL
    sudo dnf install texlive-scheme-medium
    ```
  - **macOS**: Install MacTeX (TeX Live for Mac)
    ```bash
    brew install --cask mactex
    # Or download from https://www.tug.org/mactex/
    ```
  - **Alternative**: MiKTeX works on all platforms but may require additional package installation

- **Quarto** - For rendering Quarto markdown documents to PDF
  - **Linux/macOS**: Install via package manager or download from [quarto.org](https://quarto.org/docs/get-started/)
    ```bash
    # macOS
    brew install quarto

    # Linux - download and install from https://quarto.org/docs/get-started/
    ```

> **Note**: The setup script installs `quarto-cli` via pip, but you should also install Quarto system-wide for best compatibility.

### Why LaTeX is Required:

LaTeX is essential for this template because:
1. **Quarto PDF Generation**: Quarto uses LaTeX (pdflatex) to compile `.qmd` files to PDF
2. **Matplotlib Plot Rendering**: The template configures matplotlib to use LaTeX for text rendering in plots (see `matplotlibrc` and `plot_helpers.py`), ensuring consistent typography between your plots and document

Without a LaTeX distribution installed, both `make preview` and plot generation will fail.

## Steps:

1. Make a fork and clone it.
2. Open the directory in your terminal of choice.
3. Run this command:

   ```bash
   bash create-physics-environment.sh
   ```

   > This creates a python environment in `/.physics`. It's not necessary to activate this environment to build the report, but you should set it as your active python environment to use language support in your code editor.

4. Duplicate the `lab-report-template` directory under a new name, such as `lab-report-1`, and open it in your editor of choice.

### Verify Your Installation:

To check if all dependencies are properly installed, navigate to your lab report directory and run:

```bash
make check-deps
```

This will verify that Python packages and Quarto are available. To manually check LaTeX:

```bash
# Check if LaTeX is installed
pdflatex --version

# Check if Quarto is installed
quarto --version
```

## Workflow:

1. Run `make preview` inside the `lab-report-1` directory. This will open a preview inside your web browser that **automatically rebuilds upon save**.
2. All your editing (text, code, metadata) is then done inside the `lab-report.qmd` file.
3. You can then permanently save your file from the preview browser tab.
