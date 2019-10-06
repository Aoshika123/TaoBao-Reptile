from snownlp import SnowNLP
file="TmallContent2.txt"
file1="new.txt"
x=0
#好评计数
k=0
#中评计数
y=0
#差评计数
z=0
#总数
with open(file,"r",encoding="utf-8") as text:
    #打开目标文件
    with open(file1, "w", encoding="utf-8") as text1:
        #打开保存差评的文件
        for comment in text:
            z+=1
            s=SnowNLP(comment)
            #文本分析
            s=s.sentiments
            #情感系数
            if s>0.5:
                x+=1
            elif s==0.5:
                k+=1
            else:
                text1.write(comment)
                #写入差评数
                y+=1
print("好评数："+str(x))
print("差评数："+str(y))
print("中评数："+str(k))
print("总评论数："+str(z))
print("差评率："+str( round(y/z,2)*100)+"%")
