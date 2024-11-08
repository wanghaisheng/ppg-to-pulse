# ppg-to-pulse

https://github.com/paulvangentcom/heartrate_analysis_python/blob/master/examples/1_regular_PPG/Analysing_a_PPG_signal.ipynb


https://github.com/Giorgia01carboni/ppg-analyzer

https://github.com/aunal16/video_to_ppg

https://github.com/23875658/cuffless-bp-monitoring

https://github.com/DataboyUsen/Pulse-lead-Peak-Detection

https://github.com/davidokel/PPGExtract/tree/master

https://github.com/WeiweiJin/PulseWaveSignalProcessor/tree/main

https://github.com/stw32/PulseWaveform

https://github.com/vgees/AI-in-Wearable-Device-Data/tree/master/Pulse%20Rate%20Algorithm

https://github.com/TigerKAP/pulse_ox

https://github.com/shiown026/pulseRateEstimate


https://github.com/tonyfu97/Pulse-Ox-BLE


https://github.com/DataboyUsen/Pulse-lead-Peak-Detection


https://github.com/scientisst/BioSPPy


https://github.com/CN-DXTZ/PulseWave/tree/master/Python

https://peterhcharlton.github.io/pwdb/pwdb.html

https://github.com/fwolling/PPGraw/issues/2

https://github.com/peterhcharlton/ppg-beats

https://github.com/dwil2444/PW_Processing/tree/main
https://github.com/fwolling/PulSync

https://github.com/birdflu/pulse/tree/master

## preprocess

### 去工频

工频信号干扰的去除、肌电干扰去除等

## 运动伪差

基于散度值分析的运动伪差滤除算法 
人体的运动，例如喘气、说话、咳嗽、呐喊等动作致使PPG信号采集时光电传感器与皮
肤接触面之间发生微小的偏移，检测光路发生变化进而产生运动伪差干扰噪声，这一类由于
光路变化导致的运动伪差噪声无法通过简单的滤波器进行去除，而运动伪差的存在会降低
PPG信号的信号质量，影响信号特征提取的准确度，进而影响中医脉象分类实验结果的准确
率。因此，对运动伪差的滤除操作，存在很大的必要性，本文将基于散度值的计算分析，对
存在运动伪差的PPG信号周期进行判断和剔除

![image](https://github.com/wanghaisheng/ppg-to-pulse/assets/2363295/8beac941-c574-49f7-8ee5-25e6d5dc5000)

cite:基于PPG信号的脉象分类算法研究与系统设计

### 滤波


矫正基线偏移的方法有很多，常见的有形态滤波[37]、FIR滤波[38]、中值滤波[39]、自适应滤波和基于全部数据的最小二乘拟合法[39]和基于基线上关键点的函数拟合法等

由于基线漂移的特点为非周期直
流分量，利用小波变换的带通滤波特性和尺度函数的低通滤波特性，可以将显现于小
波分解大尺度上的基线漂移直接去除，并由重构算法恢复去除基线漂移后的信号。我
们在软件设计过程中，经过多次实验发现对采集的脉搏信号进行8层分解时，已将基
线漂移从原信号中分解出来。但此时还残留有脉搏波信号中频率较低的成分，对脉搏
信号进行9层分解，到尺度9时，可认为基本是基线漂移成分。

通过与原始信号的比较，证实了尺度9下的逼近信号就是脉搏信号中的基线漂移
成分。既然尺度9下的逼近信号就是原始信号的基线漂移成分。在小波重构的过程中，
将该尺度下的分量置零，就可以得到去除了基线漂移分量的合成信号。在信号的采样
频率不变的情况下，由于对应某一个确定的小波变换，在不同尺度下的频窗中心和窗
宽是确定的，由此可以确定相应去除基线漂移的最大分解尺度。脉搏信号采集系统的
采集频率设为200Hz，采用了8阶Symlets(Sym8)小波基对采集的脉搏信号进行9次小波
分解，尺度9下逼近信号的频率是0～0.45Hz



首先采用带通滤波器将原脉搏波中除0.032~30 Hz以外的噪声去除，其次经过中值滤波消除孤立噪声点，然后使用小波变换进一步去除脉象数据的低频噪声，得到能显现脉搏波特征的脉象图，如图5所示。

散度值分析可以应用在信号相似程度的相关计算之上，分别计算不同信号的散度值大小，
通过对比分析干净稳定的模板信号与存在运动伪差干扰噪声[
38]的实验信号，可以有效判断实
验信号中的伪差干扰信号周期，进而得到平滑稳定的PPG优质波信号。散度值分析可以有效
剔除普通滤波算法，如带通滤波算法所无法滤除的干扰噪声，为实验获取更加干净稳定的优
质波信号奠定坚实的基础


利用希尔伯特黄变换（HHT）法滤除PPG信号中的低频噪声。希尔伯特黄变换主要包括经验模态分解（EMD）和希尔伯特变换两个步骤号。EMD分解将PPG信号分解得到若干个具备独立频率的信号(本征模态函数,IMF)和一个剩余量res,将非线性稳定的信号转化为线性稳定的信号。因为只有线性稳定信号才符合希尔伯特变换的使用要求,因此EMD分解一般作为希尔伯特变换的前序步骤。将EMD分解得到的IMF分量进行希尔伯特变换,得到各个IMF分量的瞬I时频率。
首先,对PPG信号进行EMD分解,将原始PPG信号分解为若干个IMF分量和一个剩余量res。
接着,对EMD分解得到的各个IMF分量进行希尔伯特变换:
最后，因为基线漂移干扰噪声的频率一般低于0.7Hz，所以在求得的若干个IMF中，将
瞬时频率低于0.7Hz的IMF分量弃用，同时也弃用剩余量res，将其余未弃用的IMF分量重
构整合获得滤除低频基线漂移干扰噪声的PPG信号



### 基线漂移 

最后，通过相应的单周期频率窗口，利用三次样条插值方法和频率窗口找到脉象波形的最小值，并通过脉象数据减去最小值拟合曲线来彻底去除基线漂移得到最终的脉象波形，如图6所示。

### 单周期切割


对滤波后的脉象信号进行 单周期分割，获得脉象的单周期波形。

由于脉象数据集中的数据过少，本文采用少数类样本过采样技术（Synthetic Minority OversamplingTechnique，SMOTE）对脉象数据集进行过采样以扩增脉象数据集的样本，防止MECA⁃ResNet欠拟合


https://github.com/scientisst/BioSPPy


### 异质性评估

https://bbs.pinggu.org/thread-429415-1-1.html

>让我来解释一下吧。
如何准确识别自变量X对因变量Y的作用？考虑到影响Y的因素有很多，不仅包括X，也包括其他因素（也即非观测因素）。为逻辑清晰起见，我们简单把非观测因素的作用归结为Z。如果X的值变化了，Z的值也随之变动，此时你观测到的Y的变动，到底是X引起的，还是Z引起的？说不清楚。
所以，逻辑上来讲，只有在Z不变的情况下，X变了，Y也变了，你才可以说，Y的变动确实是X引起的，因为此时其他因素Z是保持不变的，也就是我们通常说的“其他因素不变”。
那么，其他因素Z不变，如果其作用被吸收进误差项（因为既然Z是非观测因素，缺乏有效测量数据，那么你在计量经济模型中是只考虑X的），其在统计上的表现之一就是误差项的方差应该保持不变（当然还有其他统计上的表现，方差不变只是“其他条件不变”这一前提的统计表现之一）。因为误差项是随机因素成分，其方差不应随X的变化而表现出系统性的差别。当把Z的效应纳入误差项后，如果Z是随X变化的（就是不同的X，其他因素Z也不同），那么这样的误差项当然就表现出“异方差”了。
从另一个角度来说，同方差假设给统计推断带来便利，因为你要估计的方差数大大减少了。不管X取何值，误差项的条件方差都是一样的，否则X每取一个值，你都要去估计一个条件方差，重复测量数据还勉强可以做到，一般的横截面数据是不可能估计出这么多的误差方差的。
