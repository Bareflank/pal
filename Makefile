#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

TOP_DIR = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
BUILD_DIR = $(TOP_DIR)/build
TEST_DIR = $(TOP_DIR)/test

CROSS_COMPILE = aarch64-linux-gnu-
CXX = $(CROSS_COMPILE)g++
CXX_FLAGS = -c -std=c++14 -O3 -I$(TOP_DIR)/include

PYTHON = python3
PYTHON_COVERAGE_FLAGS = --source=. --omit=*abstract*,*test*

generate:
	# mkdir -p ${BUILD_DIR}
	${PYTHON} -m shoulder

all:

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	rm -rf output


test: python_test

test_all: python_test cxx_test

python_test:
	coverage3 run $(PYTHON_COVERAGE_FLAGS) -m unittest discover -p 'test_*.py'

coverage: python_test
	coverage3 report -m

cxx_test:
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXX_FLAGS) -c $(TEST_DIR)/cpp/test_regs.cpp -o $(BUILD_DIR)/test_regs.o
	$(CXX) $(BUILD_DIR)/test_regs.o -o $(BUILD_DIR)/test

.PHONY: test python_test cxx_test coverage all
