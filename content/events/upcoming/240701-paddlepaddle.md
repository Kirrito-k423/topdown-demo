---
title: "昇腾入职"
types: "upcoming"
date: 2024-07-01T19:30:15+08:00
location: "上海青浦"
img_url: https://pic.shaojiemike.top/shaojiemike/2024/02/21452b4c88f549d5b8c5a6295a1f582d.png
onlineLink: # 线上会议
abstract: "积极准备AI相关技能"
KeyWords:
- baidu
- AI
---

为了明年入职华为，顺利跟上AI的进度。

我应该积极培养相关的能力：

1. 数理基础
2. AI模型训练（以docker模型画图入手）
      1. 关注开源模型 [civatai](https://civitai.com/)
      2. https://github.com/bmaltais/kohya_ss
      3. https://github.com/KohakuBlueleaf/LyCORIS/tree/main
1. transformer等模型基础学习
2. AI训练热点分析。
3. AI训练优化尝试


{{% admonition note "AI 相关的拓展阅读" %}}

<!-- []() -->

The Landscape of Compute-near-memory and Compute-in-memory: A Research and Commercial Overview

<https://github.com/chenzomi12/DeepLearningSystem/blob/main/02Hardware/02ChipBase/05.gpu.pdf>

[【一起学AI】0-序](https://mp.weixin.qq.com/s/LYbpLWgNpxufTWYi1eyRrQ)

[一张地图带你尽览计算机科学分支](https://mp.weixin.qq.com/s/i00aBe-G3Uqu1phjoVgQ6Q)

[Prompt 【LLM】玩好ChatGPT的黑科技](https://mp.weixin.qq.com/s/b0KJWDCkuGtKLfvTzv8brg)

### 硬件设计

[软硬协同优化 (4)：指令集设计概述](https://mp.weixin.qq.com/s/aTsfKlih9pv-l-Q-iqKLcw)

[一文掌握ASIC半导体芯片知识](https://mp.weixin.qq.com/s/lYR1lS6Yxzgt__271UbrdQ)

### AI模型

[现在LLM 的大小为什么都设计成6/7B、13B和130B几个档次？解析大模型中的Scaling Law](https://mp.weixin.qq.com/s/-JwiRvYAo61RG6iHHhwmVg)

[【LLM】终于有人将大模型可视化了](https://mp.weixin.qq.com/s/2uY0Kw2ZWpzAPMCRHNPbvw)

### 瓶颈与性能分析（成本）

[Memory Wall in Neural Network Inference](https://blog.csdn.net/qq_49588762/article/details/135528513)

[CPU推理](https://mp.weixin.qq.com/s/vb1U_tQ79rsNjUwuTUoD9Q)

mike:
<https://le.qun.ch/en/blog/2023/05/13/transformer-batching/>

mike:
Dissecting Batching Effects in GPT Inference 一个blog你们可能会感兴趣，有GPT inference的内存墙分析

mike:
<https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices>

### 国内产品的硬件差距

1. [国产GPU新势力摩尔线程](https://mp.weixin.qq.com/s/u-hwp7kBTW7fOgDlNNKkRQ)
2. [国产GPU，可堪大用吗？系列之二：神秘的910B](https://mp.weixin.qq.com/s/olWs3I5kHSNPQhSe-SjKcw)
2. [英伟达 vs. 华为海思：GPU性能一览](https://mp.weixin.qq.com/s/d8rdGy8NNbxyqNVU8y11WQ)
昇腾910B 达芬奇 gpuScratchpad
思元690
深水4号

### 国外先进制程

[拆掉英伟达护城河，细节曝光！世界最快超算用3072块AMD GPU训完超万亿参数LLM](https://mp.weixin.qq.com/s/QPAxuBmrr1O6H0LjwiMMxA)


{{% /admonition %}}


{{% admonition note "HUAWEI 计算产品线" %}}

### 工作内容

1. 算子底层npu异常检测，内存踩踏，越界。
2. 高层模型层级，提高精度，算法强相关。
3. (传统内容的创新)基于性能建模，推理和训练加速。

{{% /admonition %}}

{{% admonition note "Baidu ai for system" %}}

### 团队

- 百度编译器 晓光
- 10几个人，后端上海，前端北京。
- **尖酸小黄鸭：T9 - 半年**
- **T5 -清华的硕士**：AI编译器前端，OP → 机器码→kernel。循环融合。

### 工作内容

- 鲁棒性(容忍输入扰动的稳定性，处理出错情况的可靠性)，正确性，AI原生的思维。
- 后端 code阵列，

#### AI 编译器

- 中间理论：代数结构，形式化下来。多个**op循环融合**，map ADT（Abstract Data Type"，即抽象数据类型？）
- TVM autotune op规则
- torch 负优化 - 形式化定义，算子以及约束。 A B op融合

{{% /admonition %}}
