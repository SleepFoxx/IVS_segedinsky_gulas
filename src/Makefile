.PHONY: all pack clean test doc run stddev help req 

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

ZIP_FILE = xhulinj00_xrybarr00_xrzeszm00_xvercim00.zip
TESTS_FILE = math_test.py
CALCULATOR = calc.py
STDDEV = stddev.py

all: $(VENV)


$(VENV): req
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


req:
	@if [ ! -f requirements.txt ]; then \
		echo "customtkinter" > requirements.txt; \
		echo "pyinstaller" >> requirements.txt; \
	fi


pack: clean req
	cd .. && zip -r $(ZIP_FILE) . -x "*.git*"


clean:
	rm -rf __pycache__ *.pyc $(VENV) requirements.txt dist build *.spec docs/_build
	rm -f ../$(ZIP_FILE)


test: all
	$(PYTHON) -m unittest $(TESTS_FILE)

run: all
	$(PYTHON) $(CALCULATOR)


stddev: all
	$(PYTHON) $(STDDEV)

doc:
	doxygen Doxyfile


help:
	@echo "How to build and run the project:"
	@echo "  1. Install system requirements: sudo apt install python3 python3-venv python3-tk"
	@echo "  2. Setup environment:          make all"
	@echo "  3. Run application:            make run"
	@echo "  4. Run math tests:             make test"
	@echo "  5. Run profiling (stddev):     make stddev < data_file (data_10.txt, data_1000.txt, data_10000000.txt)"
	@echo "  6. Generate documentation:     make doc"
	@echo "  7. Create submission zip:      make pack"
	@echo "  8. Cleanup:                    make clean"