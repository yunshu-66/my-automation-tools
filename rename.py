import os
folder ="D:/我的窝计划/测试改名"
count=1
for filename in os.listdir(folder):
    old_path=folder+"/"+filename
    new_path=folder+"/"+"新_"+filename
    os.rename(old_path,new_path)
    print(filename,"->","新_"+filename)