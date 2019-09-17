# 3D Balance Ball 环境入门

本教程介绍在 Unity 中打开 ML-Agents 示例环境、
构建 Unity 可执行文件、在其中训练 agent 以及
最终将经过训练的模型嵌入到 Unity 环境中的端到端过程。

ML-Agents 包含大量[示例环境](Learning-Environment-Examples.md)，
您可以通过这些环境来了解 ML-Agents 的
不同使用方式。这些环境也可以用作新环境的模板
或用作测试新 ML 算法的方法。阅读本教程后，
您应该能够了解并构建示例环境。

![3D Balance Ball](images/balance.png)

本演练过程将使用 **3D Balance Ball** 环境。3D Balance Ball 包含
大量平台和球（它们都是彼此的副本）。
每个平台都会试图通过水平或垂直旋转的方式
防止球掉落。在这种环境下，平台是一个 **agent**，
可以在对球进行平衡的每一步中获得奖励。agent 也会
因为掉球而得到负奖励（惩罚）。训练过程的
目标是让平台学会绝不掉球。

让我们开始吧！
