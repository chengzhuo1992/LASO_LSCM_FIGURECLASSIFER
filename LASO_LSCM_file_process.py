import os
import shutil
import os.path as op

def MainPath():
    main_path = input("请手动查阅文件夹的路径：")
    return main_path

def SetPath():
    set_path =  input("请手动输入需要建立文件的主目录:")
    if not os.path.exists(set_path):
        os.makedirs(set_path)
    return set_path

def Slide_Process(main_path,set_path):
    filelist = os.listdir(main_path)
    os.makedirs(set_path + '/Slide1')
    os.makedirs(set_path + '/Slide2')
    os.makedirs(set_path + '/Slide3')
    os.makedirs(set_path + '/Slide4')
    tarpath1 = "{0}".format(set_path + "/Slide1")
    tarpath2 = "{0}".format(set_path + "/Slide2")
    tarpath3 = "{0}".format(set_path + "/Slide3")
    tarpath4 = "{0}".format(set_path + "/Slide4")
    for name in filelist:
        if "{0}".format("slide1") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath1, name))
        if "{0}".format("slide2") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath2, name))
        if "{0}".format("slide3") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath3, name))
        if "{0}".format("slide4") in name:
            shutil.move(os.path.join(main_path, name), os.path.join(tarpath4, name))

def Channel_Process(set_path):
    for s in range(1,5):
        scrpath = "{0}".format(set_path + "/Slide" + str(s))
        filelist = os.listdir(scrpath)
        os.chdir(scrpath)
        os.makedirs(set_path + '/Slide'+ str(s)+"/Channel1")
        os.makedirs(set_path + '/Slide'+ str(s)+"/Channel2")
        os.makedirs(set_path + '/Slide'+ str(s)+"/Channel3")
        os.makedirs(set_path + '/Slide'+ str(s)+"/Channel4")
        tarpath1 = "{0}".format(set_path + '/Slide'+ str(s)+"/Channel1")
        tarpath2 = "{0}".format(set_path + '/Slide'+ str(s)+"/Channel2")
        tarpath3 = "{0}".format(set_path + '/Slide'+ str(s)+"/Channel3")
        tarpath4 = "{0}".format(set_path + '/Slide'+ str(s)+"/Channel4")
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
            filelist.sort(key=lambda x: os.stat(x).st_ctime_ns)  # nano-second
            # filelist.sort(key=lambda x:os.path.getctime(x)) #micro-second
            os.chdir(scrpath)
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row1')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row2')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row3')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row4')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row5')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row6')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row7')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row8')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row9')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row10')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row11')
            os.makedirs(set_path + '/Slide' + str(s) + "/Channel" + str(c) + '/Row12')
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
                name = filelist[i]

                if 0 <= i < 15:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath1,name))
                elif 16 <= i < 31:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath2,name))
                elif 32 <= i < 47:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath3,name))
                elif 48 <= i < 63:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath4,name))
                elif 63 <= i < 80:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath5,name))
                elif 81 <= i < 96:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath6,name))
                elif 97 <= i < 112:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath7,name))
                elif 113 <= i < 128:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath8,name))
                elif 129 <= i < 144:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath9,name))
                elif 145 <= i < 160:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath10,name))
                elif 161 <= i < 176:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath11,name))
                elif 177 <= i < 192:
                    shutil.move(os.path.join(scrpath,name),os.path.join(tarpath12,name))
                else:
                    print("希望它不出现！")

def file_process(main_path,set_path):
    Slide_Process(main_path,set_path)
    Channel_Process(set_path)
    Row_Process(set_path)
    print("Done!!")

if __name__ == "__main__":
    file_process(main_path=MainPath(),set_path=SetPath())