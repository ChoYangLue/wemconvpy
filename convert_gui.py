import glob
import os
import sys
import re
from tkinter import *
import tkinter.filedialog
import shutil

tk = Tk()
import_directory = []
save_OGGfile = []
dirs=[]
wem_path_list=[]
iDir = 'D:/game/World_of_Warships/res/audio/Arpeggio/Voice'
oDir = "C:/"
'D:/Music/iona2'
wem_file_list = []
ogg_file_list=[]
dir_num=[0]

def convert():
    wem_file = glob.glob('*.wem')
    flie_sum = len(wem_file)

    if flie_sum != 0:
        for x in range(flie_sum):
            f = open("convert.bat", "w", encoding="utf-8")
            lit_1 = "for %%f in ({}) do ww2ogg.exe %%f --pcb packed_codebooks_aoTuV_603.bin\n".format(wem_file[x])
            ogg_file = str(wem_file[x])
            ogg_file1 = ogg_file.replace(".wem",".ogg")
            lit_2 = "for %%f in ({}) do revorb.exe %%f\n".format(ogg_file1)
            f.write(lit_1)
            f.write(lit_2)
            f.close()

            #print(lit_1)
            #print(lit_2)
            os.system("convert.bat")

            print("convert{}end".format(x))
            #os.remove("convert.bat")

def dummy():
    pass

def getdirs(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path,item)):
            app = path +"/"+ item
            dirs.append(app)
    return dirs

def copy():
    for x in range(len(wem_file_list)):
        t_pass = wem_file_list[x]
        t_path = t_pass.replace('\\','/')
        file_name0 = wem_file_list[x].replace('{}'.format(wem_path_list[x]),"")
        s_pass = cwd 
        s_path = s_pass.replace('\\','/')
        ogg_pass = file_name0 # + cwd
        ogg_pass2 = ogg_pass.replace('\\','/')
        ogg_path = ogg_pass2.replace(".wem",".ogg")
        ogg_file_list.append(ogg_path)
        #print(wem_path_list[x])
        #print("{}から".format(t_pass))
        #print("{}まで".format(s_path))
        #print("{}をコピー".format(file_name0))
        shutil.copy("{}".format(t_path),"{}".format(s_path))

def delete():
    del wem_file_list[:]
    search_wem(cwd)
    for x in range(len(wem_file_list)):
        file_name0 = wem_file_list[x].replace('{}'.format(wem_path_list[x]),"")
        file_name1 = file_name0.replace('{}'.format(cwd),"")
        file_name2 = file_name1.replace('/',"")
        file_name3 = file_name2.replace('\\',"")
        os.remove(file_name3)
    del wem_path_list[:]
    wem_file = glob.glob('*.ogg')
    for x in range(len(wem_file)):
        ogg_pass = wem_file[x].replace('/',"")
        ogg_path = ogg_pass.replace('\\',"")
        os.remove(ogg_path)

def move():
    for x in range(len(ogg_file_list)):
        ogg_pass = ogg_file_list[x].replace('/',"")
        ogg_path = ogg_pass.replace('\\',"")
        shutil.copy("{}".format(ogg_path), "{}".format(save_OGGfile[0]))

def search_wem(path):
    wem_file = glob.glob('{}\*.wem'.format(path))
    for c in range(len(wem_file)):
        wem_file_list.append(wem_file[c])
        wem_path_list.append(path)

def open_wem():
    sv0 =tkinter.filedialog.askdirectory(initialdir=iDir,title="wemファイル")
    if len(import_directory)==1:
        del import_directory[0]
    import_directory.append(sv0)
    buf0.set("{}".format(sv0))
    print(import_directory[0])

def save_ogg():
    sv1 =tkinter.filedialog.askdirectory(initialdir=oDir,title="oggファイル保存先")
    if len(save_OGGfile)==1:
        del save_OGGfile[0]
    save_OGGfile.append(sv1)
    buf1.set("{}".format(sv1))
    print(save_OGGfile[0])

def main00():
    if buf0 != None and buf1 != None:
        main()
    else:
        print("error")

def sec_file(start):
    for y in range(start,len(dirs)):
        global ndir_sum
        ndir_sum = 0
        for dire in getdirs(dirs[y]):
            ndir_sum = ndir_sum + 1
    dir_num.append(ndir_sum)
    print(len(dirs))
    print(dir_num)
    

def main():
    global cwd
    cwd = os.getcwd()

    path = import_directory[0]
    dir_sum = 0
    
    for dire in getdirs(path):
        dir_sum = dir_sum + 1
    dir_num.append(dir_sum)
    print(dir_sum)

    for z in range(100):
        sec_file(dir_num[z])
        if dir_num[z+1]==dir_num[z]:
            del dir_num[z]
            del dir_num[z-1]
            break

    """
    for y in range(0,dir_sum-1):
        ndir_sum = 0
        for dire in getdirs(dirs[y]):
            ndir_sum = ndir_sum + 1
    dir_num.append(ndir_sum)
    print(len(dirs))
            
    for yd in range(dir_sum,len(dirs)):
        nndir_sum = 0
        for dire in getdirs(dirs[yd]):
            nndir_sum = nndir_sum + 1
    dir_num.append(nndir_sum)
    print(len(dirs))

    for ysd in range(ndir_sum,len(dirs)):
        nnndir_sum = 0
        for dire in getdirs(dirs[ysd]):
            nnndir_sum = nnndir_sum + 1
    dir_num.append(nnndir_sum)
    print(len(dirs))
    """

    #print(dir_num)

        
    for jo in range(len(dirs)):
        #print(dirs[jo])
        search_wem(dirs[jo])
        #pass

    print("wemファイルの数：{}".format(len(wem_file_list)))
    
    for jfo in range(len(wem_file_list)):
        print(wem_file_list[jfo])
        #pass
    copy()
    convert()
    move()
    delete()
    print("オワタ")


def gui():
    canvas = Canvas(tk,width=100,height=50)
    tk.title(u"ソフト")

    global buf0
    global buf1
    global opts1
    global opts2
    global opts3

    # メニューの設定

    # variable 用のオブジェクト
    action = IntVar()
    action.set(0)
    level = IntVar()
    level.set(0)

    # メニューバーの生成
    menubar = Menu(tk)
    tk.configure(menu = menubar)

    # メニューの設定
    games = Menu(menubar, tearoff = False)
    levels = Menu(menubar, tearoff = False)
    menubar.add_cascade(label="設定", underline = 0, menu=games)
    menubar.add_cascade(label="保存設定", underline = 0, menu=levels)

    # Games
    games.add_command(label = "referer", under = 0, command = dummy)
    games.add_separator
    games.add_radiobutton(label = "first", variable = dummy, value = 0)
    games.add_radiobutton(label = "second", variable = dummy, value = 1)
    games.add_separator
    games.add_command(label = "exit", under = 0, command = sys.exit)

    # Levels
    levels.add_radiobutton(label = '変換しない', variable = level, value = 0)
    levels.add_radiobutton(label = '上書き', variable = level, value = 1)
    levels.add_radiobutton(label = '名前変更して保存', variable = level, value = 2)


    opts1 = BooleanVar()
    opts1.set(True)
    opts2 = BooleanVar()
    opts2.set(True)
    opts3 = BooleanVar()
    opts3.set(False)


    f0 = LabelFrame(tk, text = 'wemフォルダ')
    f0.pack(padx = 5, pady = 5, side="top")
    btn0 = Button(f0,text="参照...",command = open_wem)
    btn0.pack(side="right")
    buf0 = StringVar()
    buf0.set("")
    e = Entry(f0, textvariable = buf0)
    e.pack(side="left")
    e.focus_set()
    import_directory.append(buf0.get())


    f1 = LabelFrame(tk, text = 'oggファイル保存先')
    f1.pack(padx = 5, pady = 5, )
    btn1 = Button(f1,text="参照...",command = save_ogg)
    btn1.pack(side="right")
    buf1 = StringVar()
    buf1.set("")
    g = Entry(f1, textvariable = buf1)
    g.pack(side="right")
    g.focus_set()
    save_OGGfile.append(buf1.get)


    btn = Button(tk,text="変換開始",command = main00)
    btn.pack(side="top",fill="both")


    canvas.pack()
    tk.mainloop()

gui()
