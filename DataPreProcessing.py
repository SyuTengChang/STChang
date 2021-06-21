#%%
 #import PIL

 #file_path = 'D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/0/1027_宋.jpg'

 #img = PIL.Image.open(file_path)
 #imgSize = img.size  # 大小/尺寸
 #w = img.width  # 圖片的宽

 #h = img.height  # 圖片的高
 #f = img.format  # 圖像格式

# print(imgSize)
 #print(w, h, f)


#------------------------------------------------------------------------------#

#%%
# 重新編輯圖片並儲存
import numpy as np
import cv2,os
import PIL

dir_path = 'D:/Data_Analysis_competition/ESun_AI/ESUN_traindata'
result = next(os.walk(dir_path))[2]
count = len(result)

for i in range(count):

    file_path: str = dir_path + '/' + str(result[i])
    im = PIL.Image.open(file_path)
    imgSize = im.size  # 大小/尺寸
    w = im.width  # 圖片的宽
    #h = img.height  # 圖片的高
    #f = img.format  # 圖像格式
    #print(imgSize)
    #print(w, h, f)

    top, bottom, left, right = (0, 0, 0, 0)
    #BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]
    #image = cv2.imread(file_path)
    image = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1) #讀取檔名有中文名稱的圖片
    #h,w,c = image.shape
    #print(h,w,c)
    if w < 120:
        dw = 120 - w
        left = dw // 2
        right = dw - left
        img = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=WHITE)
    elif w > 120:
        dw = w - 120
        left = dw // 2
        right = w - left
        img = image[0:67, left:right]
    else:
        img = image
        #print('第'+str(i)+'個檔案不用修圖')
    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        #cv2.imwrite(file_path,  img)  # 儲存圖片
    cv2.imencode('.jpg', img)[1].tofile(file_path) #儲存為中文名稱的圖片
    print('第'+str(i)+'個檔案已修圖完畢')


#%%
# 重新編輯801資料夾之size 50*50圖片並儲存
import numpy as np
import cv2,os
import PIL


dir_path = 'D:/Data_Analysis_competition/handwriting data/cleaned_data_50_50'
result = next(os.walk(dir_path))[2]

#for file in enumerate(result):
#    cv2.imdecode(np.fromfile(dir_path,dtype=np.uint8),-1)
#    newName = file.replace('.png','.jpg')
#    cv2.imwrite(os.path.join(jpg_dir,newName),img)

for i in range(250712):

    file_path: str = dir_path + '/' + str(result[i])
    im = PIL.Image.open(file_path)
    imgSize = im.size  # 大小/尺寸
    w = im.width  # 圖片的宽
    h = im.height  # 圖片的高
    #f = img.format  # 圖像格式
    #print(imgSize)
    #print(w, h, f)

    top, bottom, left, right = (0, 0, 0, 0)
    BLACK = [0, 0, 0]
    #image = cv2.imread(file_path)
    image = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1) #讀取檔名有中文名稱的圖片
#%%
    #h,w,c = image.shape
    #print(h,w,c)
    if w > 120 and h > 67:
        dw = w - 120
        left = dw // 2
        right = w - left
        dh = 67 - h
        top = dh // 2
        bottom = dh - top
        img = image[0:67, left:right]


    cv2.imencode('.jpg', img)[1].tofile(file_path) #儲存為中文名稱的圖片
    print('第'+str(i)+'個檔案已修圖完畢')


#%%
# resize 300*300圖片
import numpy as np
import PIL
import cv2,os

for i in range(1,13066):
    dir_path = 'D:/Data_Analysis_competition/handwriting data/cleaned_data_300_300/' + str(i)
    result = next(os.walk(dir_path))[2]
    count = len(result)
    for j in range(count):
        file_path: str = dir_path + '/' + str(result[j])
        #image = PIL.Image.open(file_path)
        image = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1) #讀取檔名有中文名稱的圖片
        img = cv2.resize(image,(120,67), interpolation=cv2.INTER_AREA)
        cv2.imencode('.jpg', img)[1].tofile(file_path) #儲存為中文名稱的圖片
        print('第'+str(i)+'個資料夾之圖片已修圖完畢')

#%%
#尋找檔名關鍵字之資料夾
import os

dir_path ='D:\Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata'
result = next(os.walk(dir_path))[1]
count = len(result)
for i in range(0,800): #13065
    file_path = os.path.join(dir_path, str(i))
    path = next(os.walk(file_path))[2]
    count1 = len(path)
    for j in range(count1): #51

        file_path1 = os.path.join(file_path, str(path[j]))

        keyword = '俊'

        if keyword in file_path1:  # 當有找到關鍵字時，紀錄Word的路徑位置

            print("檔案在第"+str(i)+"個資料夾")
        #else:
            #print("檔案不存在")


#%%

#文件內容字數統計(去除空格)
num_chars = 0
with open("d:/Data_Analysis_competition/ESun_AI/training_data_dic.txt", encoding='utf8') as f:
    for line in f:
     num_chars += len(line.split('\n')[0])
    num_charsx = num_chars - line.count(' ')
print(num_charsx)

#%%
#文件內容字數統計
#strip,rstrip,lstrip 去除指定字元


file_name = 'd:/Data_Analysis_competition/ESun_AI/training_data_dic.txt'

try:
    with open(file_name, encoding='utf8') as file_obj:
    #若檔名不是英文或含有符號，要加上 encoding='utf8'
        contents = file_obj.read()

except FileNotFoundError:
    msg = 'Sorry, the file' + file_name + ' does not exist.'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)  #去除空格
    print('The file ' + file_name + ' has about ' + str(num_words) + ' words.')
    #print(words[1])

#%%
#新增多個資料夾

import os,shutil

def mkdir(path):
    # 判斷目錄是否存在
    # 存在：True
    # 不存在：False
    folder = os.path.exists(path)

    # 判斷結果
    if not folder:
        # 如果不存在，則建立新目錄
        os.makedirs(path)
        print('-----建立成功-----')

    else:
        # 如果目錄已存在，則不建立，提示目錄已存在
        print(path + '  目錄已存在  ')

for j in range(num_words+1) :
    path = 'd:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/' + str(j)
    mkdir(path)

#%%
#彙整 dirty data
import os,shutil

file_path = 'D:/Data_Analysis_competition/ESun_AI/ESUN_traindata'
file_path1 = 'D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata_with black border/800'
file_path2 = 'D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/800'

if __name__ == '__main__':
    file = next(os.walk(file_path))[2]
    file1 = next(os.walk(file_path1))[2]
    # 差集 clean_file = list(set(file)^set(file1))
    clean_file = list((set(file).union(set(file1))) ^ (set(file) ^ set(file1))) #交集
    count = len(clean_file)
for i in range(count):
    shutil.move(file_path+'/'+clean_file[i],file_path2)  #shutil.copy 複製到另一資料夾
print("dirty data 資料夾彙整完成")

#%%

import os
import shutil


src_dir_path = 'D:/Data_Analysis_competition/ESun_AI/ESUN_traindata'        # 源文件夹

for k in range(800):

    key = words[k]
    to_dir_path = 'D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/'+str(k)         # 存放复制文件的文件夹

                         # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
    if not os.path.exists(to_dir_path):
        print("to_dir_path not exist,so create the dir")
        os.mkdir(to_dir_path,1)
    if os.path.exists(src_dir_path):
        print("src_dir_path exist")
    for file in os.listdir(src_dir_path):
        # is file
        if os.path.isfile(src_dir_path+'/'+file):


            if key in file:
                shutil.move(src_dir_path+'/'+file,to_dir_path+'/'+file)  #shutil.copy 複製到另一資料夾
                print("第 "+str(k)+" 號資料夾彙整完成")
            else:
                print(file, '已存在')


#讀取資料夾裡所有非目錄的檔案名稱

#%%
import os

dirPath = 'D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/800'
list_data = next(os.walk(dirPath))[2]
file = open('D:/Data_Analysis_competition/ESun_AI/ESun_AI_Contest_traindata/dirty data.txt','w')
file.write(str(list_data));
file.close()

