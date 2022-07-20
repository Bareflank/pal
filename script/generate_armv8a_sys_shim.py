import os, sys
from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper

dirpath = "" # path to directory to run in
mode = 'sys' # SYS ir SYSL

switch_output_file_path = "" # path to directory to file to be generated
switch_output_list = []
asm_output_file_path = "" # path to directory to file to be generated
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

def parse_access_mechanisms(yml, register_name):
        global c
        vector = 0
        if not yml["access_mechanisms"]:
            return

        for am_yml in yml["access_mechanisms"]:

            op0 = am_yml["op0"]
            op1 = am_yml["op1"]
            crn = am_yml["crn"]
            crm = am_yml["crm"]
            op2 = am_yml["op2"]

            #print(op0, op1, crn, crm, op2)
            #The switch vector the sys/sysl instruction encodin, the last 5 bits are not used for our purposes
            vector |= (op0 & 3) << 19;
            vector |= (op1 & 7) << 16;
            vector |= (crn & 15) << 12;
            vector |= (crm & 15) << 8;
            vector |= (op2 & 7) << 5;
            #print('%x' % vector)

            if mode == "sysl":

                if vector not in d:
                    d[vector] = register_name
                else:
                    return
                    '''print("Duplicate!")
                    print("Vector %x" % vector)
                    print(c, d[vector], "and", register_name)
                    print("=" * 50)'''
                    

                case_format_string = "case 0x%x:\n\tvalue = pal_get_%s_inline();\n\tbreak;\n" % (vector, register_name)

                asm_format_string = ("inline uint64_t pal_get_%s_inline(void)\n"
                                    "{\n"
                                    "\tuint64_t value = 0;\n"
                                    "\t__asm__ volatile(\"mrs %%0, s%s_%s_c%s_c%s_%s\"\n"
                                    "\t\t\t: \"=r\"(value));\n"
                                    "\treturn value;\n"
                                    "}\n"
                                    ) % (register_name, op0, op1, crn, crm, op2)
                #print(asm_format_string)

                asm_output_list.append(asm_format_string)
                switch_output_list.append(case_format_string)

                break
        
            elif mode == "sys":
                if vector not in d:
                    d[vector] = register_name
                else:
                    return
                    '''print("Duplicate!")
                    print("Vector %x" % vector)
                    print(c, d[vector], "and", register_name)
                    print("=" * 50)'''
                    

                case_format_string = "case 0x%x:\n\tpal_set_%s_inline(value);\n\tbreak;\n" % (vector, register_name)

                asm_format_string = ("inline void pal_set_%s_inline(uint64_t value)\n"
                                    "{\n"
                                    "\t__asm__ volatile(\"msr s%s_%s_c%s_c%s_%s, %%0\"\n"
                                    "\t\t\t:\n"
                                    "\t\t\t: \"r\"(value));\n"
                                    "}\n"
                                    ) % (register_name, op0, op1, crn, crm, op2)
                #print(asm_format_string)

                asm_output_list.append(asm_format_string)
                switch_output_list.append(case_format_string)

                break

            

if __name__ == "__main__":

    os.chdir(dirpath)
    register_files = os.listdir()
    register_files.sort()
    c = 0
    for i in register_files:
        try:
            path = dirpath + '/' + i.strip()
            with open(path, "r", encoding="utf8") as infile:
                data = load(infile, Loader)
                register_name = data[0]['name'].lower()
                parse_access_mechanisms(data[0], register_name)

        except Exception as e:
            msg = "Failed to parse register file " + str(path)
            msg += ": " + str(e)
            print(msg)
    output_string = ''.join(switch_output_list)
    write_to_file(output_string, switch_output_file_path)
    output_string = ''.join(asm_output_list)
    write_to_file(output_string, asm_output_file_path)
        
