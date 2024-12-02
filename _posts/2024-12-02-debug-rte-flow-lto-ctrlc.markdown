---
layout: post
title:  计划外调试一则
date:   2024-12-02 16:07:54 +0800
categories: [调试]
---

完成了调式以后我终于可以开始原定下午要做的工作了。按照原计划这些工作现在应该已经做完了，我应该可以开始弄报销事宜了才对。

搞科研这份工作对于J人想来是很不友好了。

----

我新建了一个Rust工程用来放新的实验程序代码。

把之前工程里的一个样例程序从`examples`文件夹复制为新工程的`src/main.rs`。

编写对应的辅助脚本，尝试运行，可以正常启动TCP服务器，但是无法接受客户端连接，客户端会卡死。

> 原工程文件夹中的样例，一模一样的代码，就可以运行正常。
{: .prompt-info }

在启动环节的日志中发现了三行

```
Default flow (dropping) created: 0x101
TCP Flow (port: 10000 => queue: 0) created: 0x0
UDP Flow (port: 10000 => queue: 0) created: 0x181
```

感觉其中的`0x0`格外刺眼。查看原来工程中的样例的对应输出

```
Default flow (dropping) created: 0x101
TCP Flow (port: 10000 => queue: 0) created: 0x141
UDP Flow (port: 10000 => queue: 0) created: 0x181
```

确实有所不同。根据日志的内容推测是DPDK的`rte_flow`接口，在创建TCP相关规则的时候失败了（并返回了`0x0`），导致后续所有TCP流量收不到。

----

DPDK里面的事情我没法管，所以我能做的只有尽量对齐两边工程的设定。

经过一段时间的尝试，我发现必须要保留如下内容，TCP流规则才不会是`0x0`。

首先，链接时优化（LTO）必须打开。

> ？
{: .prompt-tip }

其次，必须对Ctrl-C注册一个回调函数。

> ？？
{: .prompt-tip }

我想破了头也想不出来这俩是怎么影响到`rte_flow`创建TCP流规则的。

以上。
