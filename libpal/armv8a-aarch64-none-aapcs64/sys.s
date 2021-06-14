.section ".text"

.global pal_execute_sys
pal_execute_sys:
    // TODO: Implement Me!
    // Is it possible to do the following?
    //  - take the fields that make up the encoding for the A64 SYS instruction
    //  - calculate the instruction encoding, and write it to memory (here)
    //  - execute the instruction, using the memory value that just got written
    ret
