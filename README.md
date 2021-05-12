# LabTool
Common tools in laboratory

### stewart_tool.py
主程序，Stewart平台控制上位机，主要为页面控件运行逻辑。
启动方式： ``` python stewart_tool.py ```

### StewartCtrlPanelUI.ui
UI页面文件，结构化文本，使用QtDesigner绘制并生成。

### MainWindow.py
主窗口类，由UI文件生成，主程序对其进行调用。
生成方式： ``` pyuic5 StewartCtrlPanelUI.ui -o MainWindow.py ```

### stewart_model.py
Stewart机构模型计算类，包含机构尺寸参数化生成及运动学反解。

### protocol_convert.py
协议转换类，用于业务层面的协议转换，这里是将数据按照定制can协议打包，并调用驱动接口发送。

### can_driver.py
CAN通讯驱动类，调用dll接口，下发数据。

# lib
Necessary library files

# test
Demos for testing

### udp_cli.py, udp_srv.py
udp通讯测试程序

### 注：每个类文件都可以通过命令行运行```python ***.py```进行测试