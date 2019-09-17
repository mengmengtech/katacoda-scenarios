## 使用 Reinforcement Learning（强化学习）来训练 Brain

有了一个包含模拟环境的 Unity 可执行文件后，现在我们
可以执行训练。为了首先确保您的环境和 Python 
API 能正常工作，您可以使用 `python/Basics` 
[Jupyter 笔记本](/book/en-US/Background-Jupyter.md)。
此笔记本包含了 API 功能的简单演练。
在 `Basics` 中，务必将 `env_name` 设置为您先前构建的
环境文件的名称。

### 使用 PPO 进行训练

为了训练 agent 对球进行正确平衡，我们将使用一种称为 Proximal Policy Optimization (PPO) 的 
Reinforcement Learning（强化学习）算法。
与其他许多 RL 算法相比，这种算法经证明是一种安全、
有效且更通用的方法，因此我们选择它作为与 ML-Agents 
一起使用的示例算法。有关 PPO 的更多信息，
请参阅 OpenAI 近期发布的[博客文章](https://blog.openai.com/openai-baselines-ppo/)，
其中对 PPO 进行了说明。


为了训练 Balance Ball 环境中的 agent，我们将使用 Python 
包。我们提供了一个名为 `learn.py` 的方便的 Python 包装脚本，此脚本会接受用于配置训练和预测阶段的参数。


我们将向这个脚本传递我们刚才构建的环境可执行文件的路径。（可选）我们可以
使用 `run_id` 来识别实验并创建用于存储模型和摘要统计信息的文件夹。当使用 
TensorBoard 来观测训练统计信息时，将每次训练的此项设置为顺序值
将会很有用。也就是说，第一次训练时为“BalanceBall1”，
第二次训练时为“BalanceBall2”，依此类推。如果不这样做，每次训练的
摘要信息都会保存在同一个目录中，并且全部将包含在
同一个图中。

总之，转到命令行，进入 `ml-agents` 目录并输入：

```
python3 python/learn.py <env_name> --run-id=<run-identifier> --train 
```

`--train` 标志告诉 ML-Agents 以训练模式运行。`env_name` 应该是刚才创建的 Unity 可执行文件的名字。


### 观测训练进度

开始使用 `learn.py` 按照前面部分所述的方式进行训练后，`ml-agents` 文件夹将
包含一个 `summaries` 目录。为了更详细地观测训练过程，
您可以使用 TensorBoard。从命令行中运行：

`tensorboard --logdir=summaries`

然后导航至 `localhost:6006`。

从 TensorBoard 中，您将看到摘要统计信息：

* Lesson - 只有在进行
[课程训练](/book/en-US/Training-Curriculum-Learning.md)时才有意义。
3D Balance Ball 环境中不使用此项。
* Cumulative Reward - 所有 agent 的平均累积场景奖励。
在成功训练期间应该增大。
* Entropy - 模型决策的随机程度。在成功训练过程中
应该缓慢减小。如果减小得太快，应增大 `beta` 
超参数。
* Episode Length - 所有 agent 在环境中每个场景的
平均长度。
* Learning Rate - 训练算法搜索最优 policy 时需要多大的
步骤。随着时间推移应该减小。
* Policy Loss - policy 功能更新的平均损失。与 policy
（决定动作的过程）的变化程度相关。此项的幅度
在成功训练期间应该减小。
* Value Estimate - agent 访问的所有状态的平均价值估算。
在成功训练期间应该增大。
* Value Loss - 价值功能更新的平均损失。与模型
对每个状态的价值进行预测的能力相关。此项
在成功训练期间应该减小。

![TensorBoard 运行示例](images/mlagents-TensorBoard.png)