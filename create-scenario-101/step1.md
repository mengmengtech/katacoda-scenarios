## 安装

为了安装和设置 ML-Agents、Python 所依赖的库和 Unity 软件，
请参阅[安装说明](Installation.md)。

## 了解 Unity 环境 (3D Balance Ball)

agent 是一种观测并与_环境_交互的
自主参与者 (actor)。在 ML-Agent的语境下，环境是一个包含一个 Academy， 一个或多个 Brain， 一个或多个Agent， Agent 与其他实体交互的场景。

![Unity Editor](images/mlagents-3DBallHierarchy.png)

**注意：**在 Unity 中，场景内所有元素的基础对象均为
_游戏对象_(GameObject)。游戏对象本质上是其他任何元素
（包括行为、图形、物理等）的容器。要查看组成游戏对象的组件，
请在 Scene 窗口中选择 GameObject，然后打开 
Inspector 窗口。Inspector 会显示游戏对象上的每个组件。
 
在打开 3D Balance Ball 场景后，您可能会首先注意到它包含的
不是一个平台，而是多个平台。场景中的每个平台都是
独立的 agent，但它们全部共享同一个 Brain。3D Balance Ball 通过
这种方式可以加快训练速度，因为所有 12 个 agent 可以并行参与训练任务。

### Academy

在这个示例场景中的 Academy 对象是 Ball3DAcademy 游戏对象。
当您在 Inspector 中查看该 Academy 组件时，可以看到若干
用于控制环境工作方式的属性。例如，Inspector中可以看到
**Training** 和 **Inference Configuration** 属性， 在其中我们可以设置之后生成的 Unity 可执行文件的
图形和 Time Scale 属性。Academy 在训练期间使用 
**Training Configuration**，而在不训练时使用 
**Inference Configuration**。（*Inference* 等同于**不**进行训练的任何时候，此时 agent 可以使用经过训练的模型控制，或用写定的代码控制，或让玩家直接控制。）
通常情况下，您需要为 **Training configuration** 设置低图形质量
和高Time Scale，而为 **Inference Configuration** 设置高图形质量和 
`1.0` 的Time Scale。

**注意：**如果您想在训练期间观测环境，则可以调整 
**Inference Configuration** 设置来使用更大的窗口和更接近 
1:1 的时间刻度。当你要正式训练时一定要重新设置这些参数；
否则，训练可能需要很长时间。

对于环境，另一个需要关注的方面是 Academy 的实现。
由于 Academy 基类是抽象的，您必须始终定义一个子类。
您可以实现以下三个函数，但这些函数都是可选的：

* Academy.InitializeAcademy() — 启动环境时调用一次。
* Academy.AcademyStep() — 在 
Agent.AgentAction() 之前（以及 agent 收集其观测结果之后）的每个模拟步骤调用。
* Academy.AcademyReset() — 在 Academy 开始或重新开始模拟
（包括第一次）时调用。

3D Balance Ball 环境不使用这些函数（每个 agent 在需要时
会自行重置），但许多环境都会使用这些函数来
控制 agent 周围的环境。

### Brain

场景中的 Ball3DBrain 游戏对象包含 Brain 组件，
是 Academy 对象的子级。（场景中的所有 Brain 对象都必须是 
Academy 的子级。）3D Balance Ball 环境中的所有 agent 使用
同一个 Brain 实例。
Brain 不存储关于 agent 的任何信息，
只是将 agent 收集的观测结果发送到决策过程，
然后将所选的动作返回给 agent。因此，所有 agent 可共享
同一个 Brain，但会独立行动。Brain 设置可以提供很多
关于 agent 工作方式的信息。

**Brain Type** 决定了 agent 如何决策。
**External** 和 **Internal** 类型需要协同使用：训练 agent 时使用 **External**，
而在采用经过训练的模型时使用 **Internal**。
**Heuristic** Brain 允许您通过扩展 Decision 类来对 agent 的逻辑进行
手动编码。最后，**Player** Brain 可让您将键盘命令
映射到动作，这样在测试 agent 和环境时
会非常有用。如果这些类型的 Brain 都不能满足您的需求，您可以
实现自己的 CoreBrain 来创建自有的类型。

在本教程中，进行训练时，需要将 **Brain Type** 设置为 **External**；
当您将经过训练的模型嵌入到 Unity 应用程序中时，需要将 
**Brain Type** 更改为 **Internal**。

**向量观测空间**

在决策之前，agent 会收集有关自己在环境中所处的状态的
观测结果。ML-Agents 将观测分为两类：
**Continuous** 和 **Discrete**。**Continuous** 向量观测空间
会收集浮点数向量中的观测结果。**Discrete** 
向量观测空间是一个状态表的索引。大多数示例环境
都使用连续的向量观测空间。

3D Balance Ball 示例中所用的 Brain 实例使用 **State Size** 为 8 的 
**Continuous** 向量观测空间。这意味着
包含 agent 观测结果的特征向量包含八个元素：
平台旋转的 `x` 和 `z` 分量以及球相对位置和
速度的 `x`、`y` 和 `z` 分量。（观测结果值
在 agent 的 `CollectObservations()` 函数中进行定义。）

**向量运动空间**

Brain 以*动作*的形式向 agent 提供指令。与状态
一样，ML-Agents 将动作分为两种类型：**Continuous** 
向量运动空间是一个可以连续变化的数字向量。向量
每个元素的含义都是由 agent 逻辑定义的（PPO 训练过程是一个了解agent的哪种状态更好的过程，这个过程是通过学习不同agent的不同状态会对应多少奖励来实现的）。
例如，一个元素可能表示施加到 agent 某个 
`Rigidbody` 上的力或扭矩。**Discrete** 向量运动空间将其动作
定义为一个表。提供给 agent 的具体动作是这个表的
索引。

根据设计，3D Balance Ball 示例会使用这两种类型的向量运动
空间。
您可以尝试使用两种设置进行训练，观测是否有
差异。（使用离散运动空间时将 `Vector Action Space Size` 设置为 4，
而使用连续运动空间时将其设置为 2。）
 
### Agent

Agent 是在环境中进行观测并采取动作的参与者。
在 3D Balance Ball 环境中，Agent 组件被放置在 12 个
平台游戏对象上。基础 Agent 对象有一些影响其行为的
属性：

* **Brain** — 每个 Agent 必须有一个 Brain。Brain 决定了 agent 如何
决策。3D Balance Ball 场景中的所有 agent 共享同一个 
Brain。
* **Visual Observations** — 定义 agent 用来观测其环境的
任何 Camera 对象。3D Balance Ball 不使用摄像机观测。
* **Max Step** — 定义在 agent 决定自己完成之前可以发生多少个
模拟步骤。在 3D Balance Ball 中，agent 在 5000 步之后重新开始。
* **Reset On Done** — 定义 agent 是否在完成时重新开始。
3D Balance Ball 将此项设置为 true，因此 agent 在达到 
**Max Step** 计数后或在掉球后重新开始。

也许 agent 更有趣的方面在于 Agent 子类的
实现。在创建 agent 时，您必须扩展 Agent 基类。
Ball3DAgent 子类定义了以下方法：

* Agent.AgentReset() — Agent 重置时（包括会话开始时）
调用。Ball3DAgent 类使用重置函数来重置
平台和球。该函数会将重置值随机化，从而使
训练不局限于特定的开始位置和平台
姿态。
* Agent.CollectObservations() — 在每个模拟步骤调用。负责
收集 agent 对环境的观测结果。由于分配给 
agent 的 Brain 实例设置为状态大小为 8 的连续向量观测空间，
因此 `CollectObservations()` 必须调用 8 次 
`AddVectorObs`。
* Agent.AgentAction() — 在每个模拟步骤调用。接收 Brain 选择的
动作。Ball3DAgent 示例可以处理连续和离散
运动空间类型。在此环境中，两种状态类型之间实际上
没有太大的差别：这两种向量运动空间在每一步都会
导致平台旋转发生小变化。`AgentAction()` 函数
为 agent 分配奖励；在此示例中，agent 在每一步
将球保持在平台上时收到较小的正奖励，
而在掉球时收到更大的负奖励。agent 在掉球时还会被标记为
完成状态，因此会重置一个用于下一模拟步骤的
新球。