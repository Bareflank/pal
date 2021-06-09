.section ".text"

.global pal_execute_sysl
pal_execute_sysl:
    // TODO: Implement Me!
    // Is it possible to do the following?
    //  - take the fields that make up the encoding for the A64 SYSL instruction
    //  - calculate the instruction encoding, and write it to memory (here)
    //  - execute the instruction, using the memory value that just got written
    //  - return the value that the instruction outputs
    ret
