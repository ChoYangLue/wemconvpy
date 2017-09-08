import glob
import os
import sys
import re 

wem_file = glob.glob('*.wem')

print(wem_file)

for x in range(len(wem_file)):
    f = open("convert.bat", "w", encoding="utf-8")
    lit_1 = "for %%f in ({}) do ww2ogg.exe %%f --pcb packed_codebooks_aoTuV_603.bin\n".format(wem_file[x])
    ogg_file = str(wem_file[x])
    ogg_file1 = ogg_file.replace(".wem",".ogg")
    lit_2 = "for %%f in ({}) do revorb.exe %%f\n".format(ogg_file1)
    f.write(lit_1)
    f.write(lit_2)
    f.close()

    print(lit_1)
    print(lit_2)
    os.system("convert.bat")

    print("convert{}end".format(x))
    #os.remove("convert.bat")
    
