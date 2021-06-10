import os
import shutil


def MainPath():
    main_path = input("请手动查阅文件夹的路径：")
    return main_path

def SetPath():
    set_path =  input("请手动输入需要建立文件的主目录:")
    if not os.path.exists(set_path):
        os.makedirs(set_path)
    return set_path

def Select():
    print("请确认载物台上的芯片务必保持一致")
    select = input("请输入芯片孔位数（24或96）:")
    return select

def Slide_Process(main_path,set_path):
    filelist = os.listdir(main_path)
    os.makedirs(set_path + '/Slide1')
    os.makedirs(set_path + '/Slide2')
    os.makedirs(set_path + '/Slide3')
    os.makedirs(set_path + '/Slide4')
    tarpath1 = "{0}".format(set_path + '/Slide1')
    tarpath2 = "{0}".format(set_path + '/Slide2')
    tarpath3 = "{0}".format(set_path + '/Slide3')
    tarpath4 = "{0}".format(set_path + '/Slide4')
    for name in filelist:
        if "{0}".format("Slide1") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath1,name))
        elif "{0}".format("Slide2") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath2, name))
        elif "{0}".format("Slide3") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath3, name))
        elif "{0}".format("Slide4") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath4, name))
        else:
            print("what's wrong?")
def Channel_Process(set_path):
    for s in range(1,5):
        scrpath = "{0}".format(set_path + "/Slide" + str(s))
        filelist = os.listdir(scrpath)
        os.chdir(scrpath)
        os.makedirs(set_path + '/Slide' + str(s) + '/Channel1')
        os.makedirs(set_path + '/Slide' + str(s) + '/Channel2')
        os.makedirs(set_path + '/Slide' + str(s) + '/Channel3')
        os.makedirs(set_path + '/Slide' + str(s) + '/Channel4')
        tarpath1 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel1')
        tarpath2 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel2')
        tarpath3 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel3')
        tarpath4 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel4')
        for name in filelist:
            if "{0}".format("ch1") in name:
                shutil.move(os.path.join(scrpath,name),os.path.join(tarpath1,name))
            elif "{0}".format("ch2") in name:
                shutil.move(os.path.join(scrpath,name),os.path.join(tarpath2,name))
            elif "{0}".format("ch3") in name:
                shutil.move(os.path.join(scrpath,name),os.path.join(tarpath3,name))
            elif "{0}".format("ch4") in name:
                shutil.move(os.path.join(scrpath,name),os.path.join(tarpath4,name))
            else:
                print("存在其它文件！")

def Row_Process(set_path):
    for s in range(1,5):
        for c in range(1,5):
            scrpath = "{0}".format(set_path + "/Slide" + str(s)+ '/Channel' + str(c))
            filelist = os.listdir(scrpath)
            os.chdir(scrpath)
            time_order_filelist = sorted(filelist,key=lambda x: os.path.getmtime(os.path.join(scrpath,x)))
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row1')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row2')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row3')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row4')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row5')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row6')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row7')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row8')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row9')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row10')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row11')
            os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row12')
            tarpath1 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row1')
            tarpath2 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row2')
            tarpath3 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row3')
            tarpath4 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row4')
            tarpath5 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row5')
            tarpath6 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row6')
            tarpath7 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row7')
            tarpath8 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row8')
            tarpath9 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row9')
            tarpath10 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row10')
            tarpath11 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row11')
            tarpath12 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row12')
            for i in range(0,192):
                name = time_order_filelist[i]
                if 0 <= i < 16:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath1,name))
                elif 16 <= i < 32:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath2,name))
                elif 32 <= i < 48:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath3,name))
                elif 48 <= i < 64:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath4,name))
                elif 64 <= i < 80:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath5,name))
                elif 80 <= i < 96:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath6,name))
                elif 96 <= i < 112:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath7,name))
                elif 112 <= i < 128:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath8,name))
                elif 128 <= i < 144:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath9,name))
                elif 144 <= i < 160:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath10,name))
                elif 160 <= i < 176:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath11,name))
                elif 176 <= i < 192:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath12,name))
                else:
                    print("希望它不出现！")

def Human_Band_Process(set_path):
    for s in range(1,5):
        for c in range(1,5):
            for r in range(1,13):
                scrpath = "{0}".format(set_path + "/Slide" + str(s)+ '/Channel' + str(c)+ "/Row" + str(r))
                filelist = os.listdir(scrpath)
                os.chdir(scrpath)
                time_order_filelist = sorted(filelist,key=lambda x: os.path.getmtime(os.path.join(scrpath,x)))
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band1')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band2')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band3')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band4')
                tarpath1 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band1')
                tarpath2 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band2')
                tarpath3 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band3')
                tarpath4 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band4')
                for i in range (0,16):
                    name = time_order_filelist[i]
                    if 0 <= i < 4:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath1, name))
                    elif 4 <= i < 8:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath2, name))
                    elif 8 <= i < 12:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath3, name))
                    elif 12 <= i < 16:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath4, name))
                    else:
                        print("something went wrong!")

def Animal_Band_Process(set_path):
    for s in range(1,5):
        for c in range(1,5):
            for r in range(1,13):
                scrpath = "{0}".format(set_path + "/Slide" + str(s)+ '/Channel' + str(c)+ "/Row" + str(r))
                filelist = os.listdir(scrpath)
                os.chdir(scrpath)
                time_order_filelist = sorted(filelist,key=lambda x: os.path.getmtime(os.path.join(scrpath,x)))
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band1')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band2')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band3')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band4')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band5')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band6')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band7')
                os.makedirs(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band8')
                tarpath1 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band1')
                tarpath2 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band2')
                tarpath3 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band3')
                tarpath4 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band4')
                tarpath5 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band5')
                tarpath6 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band6')
                tarpath7 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band7')
                tarpath8 = "{0}".format(set_path + '/Slide' + str(s) + '/Channel' + str(c) + '/Row' + str(r) + '/Band8')
                for i in range (0,16):
                    name = time_order_filelist[i]
                    if 0 <= i < 2:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath1, name))
                    elif 2 <= i < 4:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath2, name))
                    elif 4 <= i < 6:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath3, name))
                    elif 6 <= i < 8:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath4, name))
                    elif 8 <= i < 10:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath5, name))
                    elif 10 <= i < 12:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath6, name))
                    elif 12 <= i < 14:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath7, name))
                    elif 14 <= i < 16:
                        shutil.move(os.path.join(scrpath, name), os.path.join(tarpath8, name))
                    else:
                        print("something went wrong!")


def file_process(main_path,set_path,select):
    Slide_Process(main_path,set_path)
    Channel_Process(set_path)
    Row_Process(set_path)
    if select == "24": #human
        Human_Band_Process(set_path)
    elif select == "96": #animal
        Animal_Band_Process(set_path)
    else:
        print("please restart this programme")
    print("Done!!")

if __name__ == "__main__":
    file_process(main_path=MainPath(),set_path=SetPath(),select=Select())