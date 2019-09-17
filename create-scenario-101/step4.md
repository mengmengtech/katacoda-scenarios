## 将经过训练的 Brain 嵌入到 Unity 环境中（测试功能）

一旦训练过程完成，并且训练过程保存了模型
（通过 `Saved Model` 消息可看出），您便可以将该模型添加到 Unity 项目中，
然后将其用于 Brain 类型为 **Internal** 的 agent。

### 设置 TensorFlowSharp 支持

由于 TensorFlowSharp 支持仍处于实验阶段，因此默认情况下会
将其禁用。为了启用这项支持，必须遵循以下步骤。请注意，
只有完成这些步骤后才能使用 `Internal` Brain 模式。

1. 确保 TensorFlowSharp 插件位于 `Assets` 文件夹中。
可在
[此处](https://s3.amazonaws.com/unity-ml-agents/0.5/TFSharpPlugin.unitypackage)下载一个包含 TF# 的 Plugins 文件夹。
下载后，双击并将其导入。您可以在 Project 选项卡中
（位于 `Assets` > `ML-Agents` > `Plugins` > `Computer` 下）
检查 TensorFlow 的相关文件来查看是否安装成功
2. 转到 `Edit` > `Project Settings` > `Player`
3. 对于每个目标平台
（**`PC, Mac and Linux Standalone`**、**`iOS`** 或 **`Android`**）：
    1.转到 `Other Settings`。
    2.选择 `Scripting Runtime Version` 为
    `Experimental (.NET 4.6 Equivalent)`
    3.在 `Scripting Defined Symbols` 中，添加标志 `ENABLE_TENSORFLOW`。
    输入后，按 Enter。
4. 转到 `File` > `Save Project`
5. 重新启动 Unity Editor。

### 将经过训练的模型嵌入到 Unity 中

1. 经过训练的模型存储在 `ml-agents` 文件夹中的 `models/<run-identifier>` 内。训练
完成后，该位置会有一个 `<env_name>.bytes` 文件，其中的 `<env_name>` 是训练期间使用的可执行文件的
名称。
2. 将 `<env_name>.bytes` 从 `python/models/ppo/` 移入 
`unity-environment/Assets/ML-Agents/Examples/3DBall/TFModels/`。
3. 打开 Unity Editor，然后选择 `3DBall` 场景（如上所述）。
4. 从 Scene 层级视图中选择 `Ball3DBrain` 对象。
5. 将 `Type of Brain` 更改为 `Internal`。
6. 将 `<env_name>.bytes` 文件从 Editor 的 Project 窗口拖入 
`3DBallBrain` Inspector 窗口中的 `Graph Model` 占位区域。
7. 按 Editor 顶部的 Play 按钮。

如果您正确执行了这些步骤，您现在应该能够
看到 Unity 编辑器中有这个用于控制平衡球行为的
训练模型。从这里开始，您便可以重新构建 Unity 的可执行文件，
并单独运行该可执行文件，在其中内置 agent 新学到的行为。
