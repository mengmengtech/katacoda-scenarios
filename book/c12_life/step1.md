### 服装搭配
  - 服装搭配 ![title](../../book/section/dress.png)
 【Neo4j图】
 
 如何服装搭配打分？
 找到优秀搭配的特征图。
例如，可以选择一对袜子与鞋子相匹配，但不特别选择鞋子。
兼容的装备应具有关键属性：如，不会有两双鞋子在一个装备）。 

在同一套装中，如果是两个类别有匹配关系,应该是他们之间的互动。我们有两个有向边
他们之间在Fashion Graph中，因为两个方向的互动应该是不同的。 

方法：Graph Neural Networks
优化：Gated Graph Neural Network (GGNN)

 
流程 ![title](../../book/section/dressProcess.png)
  
 #### 1.2.2 推荐系统
 假设你不仅要向Mengmeng推荐服装，还要预测她将给喜欢这个装扮的程度。
 分类就是编组，找出类似的人。
 回归就是预测结果。
 
 方法：
 为此，先找出与她最近的5个人。 对他们的评价求平均数。
 
 【ppt配图】![title](../../book/section/dressSuggest.png)
 
 代码： https://github.com/CRIPAC-DIG/NGNN
 
 
 #### 1.2.3 挑选合适的特征
 我们怎么选合适的特征呢？
 一般情况下，在对某一数据集构建模型之前，
 都需要考虑从数据集中去除这五种类型的特征，
 所以feature-selector帮你省去data-science生活中一部分重复性的代码工作
 feature-selector属于非常基础的特征选择工具，它提供了五种特征的选择函数，
 每个函数负责选择一种类型的特征
 
 - https://github.com/WillKoehrsen/feature-selector   
 -  http://www.mamicode.com/info-detail-2367325.html   
 -  https://ask.hellobi.com/blog/python_shequ/18706   
（后两个是中文版介绍）

