
import math
import os
'''
def circle(r):
    return round(math.pi*r*r,2)

def is_primes(number):
    if number in range(1,2):
        return True
    for i in range(2,number):
        if number % i == 0 :
           return False
    return True
def get_primse(beg,end):
    for number in range(beg,end+1):
        if is_primes(number):
            print( f"{number} is a prime")
'''
# 计算前N个数字的平方和
'''
def sum_pingfang(n):
    result = 0
    for inx in range(1,n+1):
        result += inx*inx
    return result
print(sum_pingfang(3))
print(sum_pingfang(5))
print(sum_pingfang(10))
'''
#计算列表数字之和
'''
def sum_list(param_list):
    total = 0
    for i in param_list :
        total += i
    return total
list1 = [1,2,3,4,5]
sum(list1)
'''
#取偶数
'''
def oushu(begin,end):
    oushu_list = []
    for number in range(begin,end):
        if number % 2 == 0 :
            oushu_list.append(number)
    return oushu_list
begin,end = 4,15
print(f"{begin}到{end}范围里的偶数是",oushu(begin,end))
data = [item for item in range(begin,end) if item % 2 == 0] # 列表推导式 
print(f"{begin}到{end}范围里的偶数是",data)
'''
#移除元素
'''
data = [idx for idx in range(3,14) if idx % 2 != 0]
data1 = [7,9]
data2 = [item for item in data if item not in data1] #移除多元素 列表推导式
print(data2)
'''
#列表去重
'''
list1 = [10,20,30,10,20]
print(list(set(list1))) #set 集合 无重复
'''
#列表排序
'''
lista = [20,10,40,70,50]
lista.sort() # 原地排序
listb = sorted(lista,reverse=True) #创建一个新的排序后的列表，reverse= True 降序，False升序
print(f"lista is {lista}")
print(f"listb is {listb}")
'''
#复杂列表排序
'''
lista = [{"name":"周先生","sno":101,"sgrade":88},
         {"name":"李先生","sno":102,"sgrade":78},
         {"name":"王先生","sno":103,"sgrade":99}]

listb = sorted(lista,key=lambda x:x['sgrade'],reverse=True) # x是列表的每一个元素,x['sgrade']指的是元素里的键
'''
# 成绩文件排序
'''
def read_file():
    result =[]
    with open("./student_grade.txt") as fin:
        for line in fin:
            line = line[:-1]
            #line.encode('GBK')
            line.split(",")
            result.append(line.split(","))
    return result
# 读取文件
datas = read_file()
print("reda_file datas:",datas)
# 排序数据
def sort_grades(datas):
    return sorted(datas,key = lambda x:int(x[2]),reverse=True)
datas = sort_grades(datas)
print(datas)
# 写出文件
def write_file(datas):
    with open("./out.txt","w") as fout:
        for data in datas:
            fout.write(",".join(data)+"\n")
write_file(datas)
'''
# 最高分 最低分 平均分
'''
def compute_scroe():
    scores  = []
    with open("./out.txt") as f:
        for line in f:
            line = line[:-1]
            fields = line.split(",")
            score = int(fields[-1])
            scores.append(score)
    print(scores)
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores)/len(scores),2)
    return max_score,min_score,avg_score
max_score,min_score,avg_score = compute_scroe()
print(f"max_s = {max_score}",f"min_s={min_score}",f"avg_s={avg_score}")
'''
# 统计单词的出现次数
'''
word_count = {}
with open('./out.txt') as f:
    for line in f :
        line.replace(","," ")
        line.replace(".", " ")
        words = line.split(" ")
        for word in words :
            if word not in word_count:
                word_count[word]=0
            word_count[word] += 1
print(f"所有单词出现次数={word_count}")
print(
    sorted(
    word_count.items(),
    key=lambda x: x[1], reverse=True
)[:10]
)
'''
# 统计目录下文件的大小
'''
import os
size = 0
print(size)
'''
# 获取文件名
'''
import os
import shutil
os.listdir() #获取目录下的所有文件
os.path.splitext()  #输出元组，第二位是后缀
os.mkdir()#创建目录
shutil.move() #移动文件
'''
# 数据关联
teatch = {}
with open('teacher.txt',encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        c,t = line.split(',')
        teatch[c] = t
print(teatch)