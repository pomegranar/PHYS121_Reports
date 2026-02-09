# Makefile for Quarto physics lab reports

# Variables
REPORT = lab-report.qmd
OUTPUT = lab-report.pdf
VENV = ../.physics
export PATH := $(VENV)/bin:$(PATH)
PYTHON = $(VENV)/bin/python

# Default target
.PHONY: all
all: $(OUTPUT)

# Render the Quarto document to PDF
$(OUTPUT): $(REPORT)
	quarto render $(REPORT)

# Render and open the PDF
.PHONY: view
view: $(OUTPUT)
	open $(OUTPUT)

# Clean generated files
.PHONY: clean
clean:
	rm -f $(OUTPUT)
	rm -rf lab-report_files/
	rm -f .quarto/

# Deep clean (including Python cache)
.PHONY: distclean
distclean: clean
	rm -rf __pycache__/
	rm -rf .ipynb_checkpoints/
	rm -f *.aux *.log *.out *.toc

# Preview mode (auto-reload on changes)
.PHONY: preview
preview:
	quarto preview $(REPORT)

# Check Python dependencies
.PHONY: check-deps
check-deps:
	@echo "Checking Python dependencies..."
	@$(PYTHON) -c "import matplotlib; print('✓ matplotlib')" || echo "✗ matplotlib - run: pip install matplotlib"
	@$(PYTHON) -c "import numpy; print('✓ numpy')" || echo "✗ numpy - run: pip install numpy"
	@$(PYTHON) -c "import pandas; print('✓ pandas')" || echo "✗ pandas - run: pip install pandas"
	@$(PYTHON) -c "import scipy; print('✓ scipy')" || echo "✗ scipy - run: pip install scipy"
	@echo "Checking Quarto..."
	@which quarto > /dev/null && echo "✓ quarto" || echo "✗ quarto - run: brew install quarto"

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make         - Build the PDF report"
	@echo "  make view    - Build and open the PDF"
	@echo "  make preview - Start live preview mode"
	@echo "  make clean   - Remove generated files"
	@echo "  make check-deps - Check for required dependencies"
	@echo "  make help    - Show this help message"
