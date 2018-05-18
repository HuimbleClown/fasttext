import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext

classifier = fasttext.supervised("news_fasttext_train.txt", "news_fasttext.model", label_prefix="__label__", lr = 0.1 , epoch = 100 , dim = 200 , bucket = 5000000)
#classifier = fasttext.supervised("news_fasttext_train.txt", "news_fasttext.model", label_prefix="__label__")
#load训练好的模型
classifier = fasttext.load_model('news_fasttext.model.bin', label_prefix='__label__')
result = classifier.test("news_fasttext_test.txt")
print(result.precision)#全部的准确率
print(result.recall)#全部的召回率
print(result.nexamples)#实例数
labels_right = []
texts = []
with open("news_fasttext_test.txt") as fr:
    lines = fr.readlines()
for line in lines:
    labels_right.append(line.split("\t")[1].rstrip().replace("__label__", ""))
    texts.append(line.split("\t")[0])
#print （labels）
#print （texts）
#break
labels_predict = [e[0] for e in classifier.predict(texts)] #预测输出结果为二维形式
#print(labels_predict)
text_labels = list(set(labels_right))
text_predict_labels = list(set(labels_predict))
print(text_predict_labels)
print(text_labels)
A = dict.fromkeys(text_labels, 0)  #预测正确的各个类的数目
B = dict.fromkeys(text_labels, 0)   #测试数据集中各个类的数目
C = dict.fromkeys(text_predict_labels, 0) #预测结果中各个类的数目
for i in range(0, len(labels_right)):
    B[labels_right[i]] += 1
    C[labels_predict[i]] += 1
    if labels_right[i] == labels_predict[i]:
        A[labels_right[i]] += 1
print(A )
print(B)
print( C)
#计算准确率，召回率，F值
for key in B:
    p = float(A[key]) / float(B[key])
    r = float(A[key]) / float(C[key])
    f = p * r * 2 / (p + r)
    print("%s:\t p:%f\t r:%f\t f:%f" % (key, p, r, f))
