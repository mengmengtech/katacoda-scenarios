## 构建环境

第一步是打开包含 3D Balance Ball 环境的 
Unity 场景：

1. 启动 Unity。
2. 在 Projects 对话框上，选择窗口顶部的 **Open** 选项。
3. 使用随后打开的文件对话框，找到 ML-Agents 项目内的 
`unity-environment` 文件夹，然后单击 **Open**。
4. 在 `Project` 窗口中，找到文件夹 
`Assets/ML-Agents/Examples/3DBall/`。
5. 双击 `Scene` 文件以加载包含 Balance Ball 环境的
场景。

![3DBall 场景](images/mlagents-Open3DBall.png)

由于我们要建立此环境来进行训练，因此我们需要
将 agent 使用的 Brain 设置为 **External**。这样 agent 在
进行决策时能够与外部训练过程进行通信。

1. 在 **Scene** 窗口中，单击 Ball3DAcademy 对象旁边的三角形
图标。
2. 选择其子对象 `Ball3DBrain`。
3. 在 Inspector 窗口中，将 **Brain Type** 设置为 `External`。

![将 Brain 设置为 External](images/mlagents-SetExternalBrain.png)

接下来，我们希望设置场景以便在训练过程启动我们的环境可执行文件时
正确播放场景。这意味着：
* 环境应用程序在后台运行
* 没有对话需要互动
* 正确的场景会自动加载
 
1. 打开 Player Settings（菜单：**Edit** > **Project Settings** > **Player**）。
2. 在 **Resolution and Presentation** 下方：
    - 确保选中 **Run in Background**。
    - 确保 **Display Resolution Dialog** 设置为 Disabled。
3. 打开 Build Settings 窗口（菜单：**File** > **Build Settings**）。
4. 选择目标平台。
    -（可选）选择“Development Build”以便
    [记录调试消息](https://docs.unity3d.com/Manual/LogFiles.html)。
5. 如果 **Scenes in Build** 列表中显示了任何场景，请确保
唯一选中的是 3DBall Scene。（如果该列表为空，则表示
仅当前场景包含在编译中）。
6. 单击 *Build*：
    a. 在 File 对话框中，导航至 ML-Agents 目录中的 `python`
    文件夹。
    b. 指定文件名，然后单击 **Save**。

![编译窗口](images/mlagents-BuildWindow.png)