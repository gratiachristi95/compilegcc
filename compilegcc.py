import os

programname = input('C File: ')
programname = programname.removesuffix('.c')          
assembly = 'gcc -S ' + programname + '.c -o ' + programname + '.s'
os.system(assembly)

objectfile = 'gcc -c ' + programname + '.s -o ' + programname + '.o'
os.system(objectfile)

exe = 'gcc ' + programname + '.o -o ' + programname
os.system(exe)

disassemble = 'objdump -S --disassemble ' + programname + ' > ' + programname + '.dump'
os.system(disassemble)
