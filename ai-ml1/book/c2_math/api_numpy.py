import numpy as np
# 导入 jieba
import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取
import re
from sympy import *

# https://github.com/fengdu78/Data-Science-Notes/tree/master/2.numpy
# https://github.com/fengdu78/Data-Science-Notes/tree/master/3.pandas
class Caculation(object):

    def __init__(self):
        self.level = 0
        self.student = 0

    # 3. 数数一个指定长度的
    def count(self,start,end):
        Z = np.arange(start,end)
        print(Z)
        return Z

    def crt1DArray(self,x):
        Z = np.random.random((x))
        print(Z)

        return Z

    def crt2DArray(self,x,y):
        Z = np.random.random((x,y))
        print(Z)

        return Z

    def crt3DArray(self,x,y,z):
        Z = np.random.random((x,y,z))
        print(Z)

        return Z

    def multiMatrix(self,x,y):
        if np.shape(x) != np.shape(y):
            print("形状不适合")
        else:
            Z = x @ y
        print(Z)
        return Z

    def filter1D(self,z, cond):
        cond = (3 < Z) & (Z <= 8)
        Z = z[cond]
        print(Z)
        return Z

    def 哪天(self,n):
        Z =  np.datetime64('today', 'D') - np.timedelta64(n, 'D')
        print(Z)
        return Z

    def listDays(self,start,end):
        Z = np.arange(start, end, dtype='datetime64[D]')
        print(Z)
        return Z

    def 数天(self,开始,结束):
        Z = np.arange(开始, 结束, dtype='datetime64[D]')
        print(Z)
        return Z

    def 数数(self,start,end):
        Z = np.arange(start,end)
        print(Z)
        return Z

    def 解方程(self):
        x = Symbol('x')
        y = Symbol('y')
        print(solve([y + x - 1, 3 * x + 2 * y - 5], [x, y]))
        # t = Symbol('t')
        # x = Symbol('x')
        # m = integrate(sin(t) / (pi - t), (t, 0, x))
        # n = integrate(m, (x, 0, pi))
        # print(n)

    def 探索规律(self,ar):
        asize = len(ar)
        found = 0
        for i in range(0,asize):
            if(i+2<asize):
                cal = math_fib(3,ar[i],ar[i+1])
                print(str(ar[i+2]),str(cal))
                if cal ==ar[i+2]:
                    # print(math_fib(3,ar[asize-2],ar[asize-1]))
                    found = 1
                else:
                    found =0
        if found :
            res = math_fib(3, ar[asize - 2], ar[asize - 1])
            print(math_fib(3, ar[asize - 2], ar[asize - 1]))
        return math_fib(3,ar[asize-2],ar[asize-1])

    def 平面图形(self):
        x = Symbol('x')
        y = Symbol('y')
        z = Symbol('z')
        print(solve([x*y-0.25*x*(y+z),0.5*x*(y+z)-0.5*x*y-0.5*z*x,x*(y+z)-0.5*x*(y+z)-0.5*x*y-0.5*z*x], [0.25*x*z]))
        # x,y,z =
        res = 0

        return res

    def 推理(self):
        p1 = 1
        p2 = 0
        boyage = 10
        motherage = 40

        p = ((boyage - motherage)>0)
        if False == p:
            res="不可能"
        elif True ==p:
            res="一定"
        else:
            res="有可能"
        print(str(res))

def math_fib(n,a,b):
    for i in range(n-1):
        a, b = b, a+b
    return a

def 比较(问句):
    候选字典 = {
        '数数':'从1数到100',
        '数天':'从2019年1月到2019年9月有哪些天',
        '哪天':'3天后是几号',
        '计算':'3乘以5等于多少'
    }
    最终结果 = 0
    res = 2
    for key,value in 候选字典.items():
        结果 = 比较相似(value,问句)
        print(结果)
        if 结果 > 最终结果:
            最终结果 = 结果
            res = key

    return res

def 理解(sentence):
    # sentence = sentence.trim()
    words = pseg.cut(sentence)
    for word, flag in words:
        print("{0} {1}".format(word, flag))
        if flag == "v":
            print(word)

    本领 = 比较(sentence)
    print(本领)
    num = re.findall('\d+', sentence)
    print(num)

    if 本领 == "数数":
        pattern = ''+本领+'('+str(num[0])+','+ str(num[1])+')'
    elif 本领 == "哪天":
        pattern =  ''+本领+'('+str(num[0])+')'


    return pattern



def get_word_vector(s1,s2):

    cut1 = jieba.cut(s1)
    cut2 = jieba.cut(s2)

    list_word1 = (','.join(cut1)).split(',')
    list_word2 = (','.join(cut2)).split(',')
    print(list_word1)
    print(list_word2)

    key_word = list(set(list_word1 + list_word2))#取并集
    print(key_word)

    word_vector1 = np.zeros(len(key_word))#给定形状和类型的用0填充的矩阵存储向量
    word_vector2 = np.zeros(len(key_word))

    for i in range(len(key_word)):#依次确定向量的每个位置的值
        for j in range(len(list_word1)):#遍历key_word中每个词在句子中的出现次数
            if key_word[i] == list_word1[j]:
                word_vector1[i] += 1
        for k in range(len(list_word2)):
            if key_word[i] == list_word2[k]:
                word_vector2[i] += 1

    print(word_vector1)#输出向量
    print(word_vector2)
    return word_vector1, word_vector2

def 比较相似(s1,s2):
    v1, v2 = get_word_vector(s1,s2)
    return float(np.sum(v1 * v2))/(np.linalg.norm(v1) * np.linalg.norm(v2))



if __name__ == "__main__":

    熊猫= Caculation()
    # 熊猫.解方程()
    # list=[1,1,2,3,5,8,13,21]
    # 熊猫.探索规律(list)
    # 熊猫.平面图形()
    熊猫.推理()

    # input = input("input:")
    # print(input)
    # pattern = 理解(input)
    # print("熊猫."+pattern)
    # # eval(pattern)
    # eval("熊猫."+pattern)




