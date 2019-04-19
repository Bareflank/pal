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

from .read_coprocessor_register import ReadCoprocessorRegister
from .read_coprocessor_register2 import ReadCoprocessorRegister2
from .read_memory_mapped import ReadMemoryMapped
from .read_system_register import ReadSystemRegister
from .read_system_register_banked import ReadSystemRegisterBanked
from .read_system_vector_register import ReadSystemVectorRegister
from .write_coprocessor_register import WriteCoprocessorRegister
from .write_coprocessor_register2 import WriteCoprocessorRegister2
from .write_memory_mapped import WriteMemoryMapped
from .write_system_register import WriteSystemRegister
from .write_system_register_banked import WriteSystemRegisterBanked
from .write_system_register_immediate import WriteSystemRegisterImmediate
from .write_system_vector_register import WriteSystemVectorRegister
