import os, sys
from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper


switch_output_file_path = "/home/ubuntu/PAL/pal/devpal/linux/armv8a/aarch64/all_perm_switch.c"
switch_output_list = []
asm_output_file_path = "/home/ubuntu/PAL/pal/devpal/linux/armv8a/aarch64/all_perm_asm.c"
asm_output_list = []

d = {}
c = 1

def write_to_file(s, output_file_path):
    try:
        infile = open(output_file_path, "w")
        infile.write(s)  
        infile.close()
    except Exception as e:
        msg = "Failed to write"
        msg += ": " + str(e)
        print(msg)

            
if __name__ == "__main__":

    for vector in range(65536):
        op0 = vector >> 14
        op1 = (vector >> 11) & 7
        crn = (vector >> 7) & 15
        crm = (vector >> 3) & 15
        op2 = vector & 7            

        #print("%x" % vector)
        #print(op0, op1, crn, crm, op2)

        # To follow sys instruction convention
        vector = vector << 5

        case_format_string = "case 0x%x:\n\tvalue = pal_get_s%s_%s_c%s_c%s_%s_inline();\n\tbreak;\n" % (vector, op0, op1, crn, crm, op2)

        asm_format_string = ("inline uint64_t pal_get_s%s_%s_c%s_c%s_%s_inline(void)\n"
                            "{\n"
                            "\tuint64_t value = 0;\n"
                            "\t__asm__ volatile(\"mrs %%0, s%s_%s_c%s_c%s_%s\"\n"
                            "\t\t\t: \"=r\"(value));\n"
                            "\treturn value;\n"
                            "}\n"
                            ) % (op0, op1, crn, crm, op2, op0, op1, crn, crm, op2)
        #print(asm_format_string)

        asm_output_list.append(asm_format_string)
        switch_output_list.append(case_format_string)       


    output_string = ''.join(switch_output_list)
    write_to_file(output_string, switch_output_file_path)
    output_string = ''.join(asm_output_list)
    write_to_file(output_string, asm_output_file_path)
        
