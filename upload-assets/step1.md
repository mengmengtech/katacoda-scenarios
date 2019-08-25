
启动后台服务器
## Start HTTP Server
`docker run -p 80:80 -d katacoda/docker-http-server`{{execute}}

## Test
`curl localhost`{{execute}}

## Generated Web Link

https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com

## Markdown 
<pre>https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com</pre>

## Learn More
[Displaying Tabs](https://katacoda.com/scenario-examples/scenarios/dashboard-tabs) and [embedding iFrames](https://katacoda.com/scenario-examples/scenarios/dashboard-tabs-iframe)



显示图片
![panda](/mengmeng/scenarios/upload-assets/assets/panda.png)




The following will copy the text into the clipboard. This is useful if users need to interactive with a web UI.

`docker`{{copy}}

Within the Markdown step, you would write:
<pre>
`docker`{{copy}}
</pre>

Katacoda supports copying code snippets or longer text into the clipboard by adding the attribute `data-target`.

<pre class="file" data-target="clipboard">
Copy Me To The Clipboard!!
</pre>

This is created by embedded HTML into the Markdown.

<pre>
&#x3C;pre class=&#x22;file&#x22; data-target=&#x22;clipboard&#x22;&#x3E;
Copy Me To The Clipboard!!
&#x3C;/pre&#x3E;
</pre>

**Note** Without the class="file" it will not display the clipboard functionality. For example:

<pre data-target="clipboard">
Not a file
</pre>

This was created by the HTML:

<pre>
&#x3C;pre data-target=&#x22;clipboard&#x22;&#x3E;
Not a file
&#x3C;/pre&#x3E;
</pre>


###### 拷贝
<kbd>Ctrl</kbd> + <kbd>C</kbd>

`echo "Copy it"`{{copy}}

###### 运行
For example, commands such as `echo "Run in Terminal"`{{execute}}
 can be executed by clicking the command.

This is done by adding `execute` to the markdown code block, for example:
<pre>`echo "Run in Terminal"`{{execute}}</pre>


`echo "run in terminal" `{{execute}}
`docker run -p 80:80 -d katacoda/docker-http-server`{{execute}}


###### 中断 
`echo "Send Ctrl+C before run" `{{execute interrupt}}

``` 
  # -*- coding: UTF-8 -*-
  import numpy as np
  import operator
  
  """
  函数说明:创建数据集
  Parameters:
      无
  Returns:
      group - 数据集
      labels - 分类标签
  Modify:
      2017-07-13
  """
  def createDataSet():
      #四组二维特征
      group = np.array([[1,101],[5,89],[108,5],[115,8]])
      #四组特征的标签
      labels = ['爱情片','爱情片','动作片','动作片']
      return group, labels
  
  """
  函数说明:kNN算法,分类器
  Parameters:
      inX - 用于分类的数据(测试集)
      dataSet - 用于训练的数据(训练集)
      labes - 分类标签
      k - kNN算法参数,选择距离最小的k个点
  Returns:
      sortedClassCount[0][0] - 分类结果
  Modify:
      2017-07-13
  """
  def classify0(inX, dataSet, labels, k):
      #numpy函数shape[0]返回dataSet的行数
      dataSetSize = dataSet.shape[0]
      #在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
      diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
      #二维特征相减后平方
      sqDiffMat = diffMat**2
      #sum()所有元素相加，sum(0)列相加，sum(1)行相加
      sqDistances = sqDiffMat.sum(axis=1)
      #开方，计算出距离
      distances = sqDistances**0.5
      #返回distances中元素从小到大排序后的索引值
      sortedDistIndices = distances.argsort()
      #定一个记录类别次数的字典
      classCount = {}
      for i in range(k):
          #取出前k个元素的类别
          voteIlabel = labels[sortedDistIndices[i]]
          #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
          #计算类别次数
          classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
      #python3中用items()替换python2中的iteritems()
      #key=operator.itemgetter(1)根据字典的值进行排序
      #key=operator.itemgetter(0)根据字典的键进行排序
      #reverse降序排序字典
      sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
      #返回次数最多的类别,即所要分类的类别
      return sortedClassCount[0][0]
  
  if __name__ == '__main__':
      #创建数据集
      group, labels = createDataSet()
      #测试集
      test = [101,20]
      #kNN分类
      test_class = classify0(test, group, labels, 3)
      #打印分类结果
      print(test_class)

``` {{copy}}