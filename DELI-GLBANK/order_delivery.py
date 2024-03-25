import openpyxl
import os
import shutil
import zipfile
wb = openpyxl.open(r"原始表/待处理单.xlsx")
ws = wb.worksheets[0]
locale_path = "微信图片_20221215155531.jpg"
'''
for i in ws :
    for k in i :
        if os.path.exists("签收单\\{}".format(k.value)) :
            continue
        else:
            os.mkdir("签收单\\{}".format(k.value))
for i in os.listdir("签收单\\"):
    shutil.copy(locale_path,"签收单\\{}".format(i))
    if os.path.exists("待上传签收单"):
        continue
    else:
        path = os.mkdir("待上传签收单")
for i in range(len(os.listdir("签收单\\"))):
    if i > 40 :
        continue
    else:
        zipfile.ZipFile("待上传签收单\\签收单{}.zip".format(i),'w', zipfile.ZIP_DEFLATED)

        zipfile.ZipFile.write(r"")
'''
if os.path.exists("待上传签收单\\"):
    shutil.rmtree("待上传签收单\\")
if os.path.exists("签收单\\"):
    shutil.rmtree("签收单\\")
os.mkdir("待上传签收单")
os.mkdir("签收单")
i=0
new_zip = zipfile.ZipFile("待上传签收单\\签收单0.zip","w",zipfile.ZIP_DEFLATED)
for row in ws:
    folder_name = row[0].value
    if os.path.exists("签收单\\{}".format(folder_name)):
        continue
    else:
        os.mkdir("签收单\\{}".format(folder_name))
        path = "签收单\\{}".format(folder_name)
        shutil.copy(locale_path, "签收单\\{}".format(row[0].value))
        new_zip.write("签收单\\{}".format(row[0].value),arcname=row[0].value)
        new_zip.write("签收单\\{}\\{}".format(row[0].value,locale_path),arcname="\\{}\\{}".format(row[0].value,locale_path))
        if len(new_zip.filelist) >= 80:
            i += 1
            new_zip = zipfile.ZipFile("待上传签收单\\签收单{}.zip".format(i),"w",zipfile.ZIP_DEFLATED)
        else:
            continue