TOP_DIR = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
BUILD_DIR = $(TOP_DIR)/build
TEST_DIR = $(TOP_DIR)/test

CROSS_COMPILE = aarch64-linux-gnu-
CXX = $(CROSS_COMPILE)g++
CXX_FLAGS = -c -std=c++14 -O3 -I$(TOP_DIR)/include

PYTHON = python3

all:

test: python_test

test_all: python_test cxx_test

python_test:
	$(PYTHON) -m unittest discover -p 'test_*.py'

cxx_test:
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXX_FLAGS) -c $(TEST_DIR)/cpp/test_regs.cpp -o $(BUILD_DIR)/test_regs.o
	$(CXX) $(BUILD_DIR)/test_regs.o -o $(BUILD_DIR)/test

.PHONY: test python_test cxx_test all
