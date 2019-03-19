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

cmake_minimum_required(VERSION 3.12)
project(shoulder NONE)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

set(PYTHONPATH ${CMAKE_CURRENT_LIST_DIR})

set(SHOULDER_BUILD_DIR ${CMAKE_CURRENT_BINARY_DIR}/shoulder)
set(SHOULDER_STAMP_DIR ${SHOULDER_BUILD_DIR}/stamp)
file(MAKE_DIRECTORY ${SHOULDER_STAMP_DIR})

# ------------------------------------------------------------------------------
# Generate C/C++ Headers
# ------------------------------------------------------------------------------

file(GLOB_RECURSE SHOULDER_SRC_FILES "shoulder/*.py" "include/*.h" "setup.py")

set(SHOULDER_OUTPUT_STAMP ${SHOULDER_STAMP_DIR}/shoulder_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m shoulder
    COMMAND cmake -E touch ${SHOULDER_OUTPUT_STAMP}
    OUTPUT ${SHOULDER_OUTPUT_STAMP}
    DEPENDS ${SHOULDER_SRC_FILES}
    COMMENT "Generating shoulder outputs"
)

add_custom_target(generate ALL DEPENDS ${SHOULDER_OUTPUT_STAMP})

# ------------------------------------------------------------------------------
# Shoulder distribution package
# ------------------------------------------------------------------------------

set(SHOULDER_PKG_STAMP ${SHOULDER_STAMP_DIR}/shoulder_pkg.stamp)

add_custom_command(
    COMMAND ${Python3_EXECUTABLE}
        ${CMAKE_CURRENT_LIST_DIR}/setup.py sdist bdist_wheel
        --dist-dir=${SHOULDER_BUILD_DIR}/dist
    COMMAND cmake -E touch ${SHOULDER_PKG_STAMP}
    OUTPUT ${SHOULDER_PKG_STAMP}
    DEPENDS ${SHOULDER_OUTPUT_STAMP}
    COMMENT "Packaging shoulder"
)

add_custom_target(package ALL DEPENDS ${SHOULDER_PKG_STAMP})

# ------------------------------------------------------------------------------
# Install
# ------------------------------------------------------------------------------

install(DIRECTORY shoulder DESTINATION lib/python3/dist-packages)
install(DIRECTORY scripts DESTINATION lib/python3/dist-packages)
install(DIRECTORY include DESTINATION lib/python3/dist-packages)
install(DIRECTORY output/ DESTINATION include/shoulder)

#TODO: Remove this, we shoulden't rely on installing the xml specification
install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/../ARMv85A-SysReg-00bet9 DESTINATION lib/python3)

