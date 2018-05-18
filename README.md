# fasttext
fastText 是 Facebook 开发的一个用于高效学习单词呈现以及语句分类的开源库。


## 注意
平台：Linux、Mac

预处理文档：train、test文件：注意格式为 .......  _lable_topic

语言： python


参数调整我注释掉了

## 命令完整文档

```
The following arguments are mandatory:
  -input      training file path
  -output     output file path

The following arguments are optional:
  -lr         learning rate [0.05]
  -dim        size of word vectors [100]
  -ws         size of the context window [5]
  -epoch      number of epochs [5]
  -minCount   minimal number of word occurences [1]
  -neg        number of negatives sampled [5]
  -wordNgrams max length of word ngram [1]
  -loss       loss function {ns, hs, softmax} [ns]
  -bucket     number of buckets [2000000]
  -minn       min length of char ngram [3]
  -maxn       max length of char ngram [6]
  -thread     number of threads [12]
  -verbose    how often to print to stdout [1000]
  -t          sampling threshold [0.0001]
  -label      labels prefix [__label__]

  
## 参考资料
```
  1、Facebook page: https://www.facebook.com/groups/1174547215919768
  2、https://github.com/facebookresearch/fastText 
  3、个人博客：https://huimbleclown.github.io/



