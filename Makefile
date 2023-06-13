# Makefile for generating slides.pdf from .org files

# Define a list of .dot files to be converted
DOT_FILES := $(wildcard *.dot)

# Define the corresponding .png files
PNG_FILES := $(DOT_FILES:.dot=.png)

.PHONY: all
all: $(patsubst %.org,%.pdf,$(wildcard week-*/slides.org)) $(PNG_FILES)

%.pdf: %.org
	@echo "Generating slides: $<"
	@emacs $< --batch -f org-beamer-export-to-pdf --kill

.PHONY: clean
clean: # Target to clean up generated PDFs
	@echo "Cleaning up generated PDFs"
	@rm -f week-*/slides.pdf
	@rm -f $(PNG_FILES)


# Define a pattern rule for converting .dot to .png
%.png: %.dot
	dot -Tpng $< -o $@

deps: # Target to install required dependencies
	# Check if Emacs is installed
	@command -v emacs >/dev/null 2>&1 || { echo >&2 "Emacs is not installed. Aborting."; exit 1; }
	# Install pdf-tools using Emacs package manager
	@echo "Installing pdf-tools..."
	@emacs --batch --eval '(progn (require (quote package)) (add-to-list (quote package-archives) (quote ("melpa" . "https://melpa.org/packages/"))) (package-initialize) (package-refresh-contents) (package-install (quote pdf-tools)))'
	@echo "Dependencies installed successfully."


