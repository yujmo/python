TensorBoard、多GPU并行及分布式并行
---
	1.TensorBoard是TensorFlow官方推出的可视化工具，将模型训练过程中的各种汇总数据展示出来。
	包括标量、图片、音频、计算图、数据分布、直方图和嵌入向量。
	2.如果要通过TensorBoard展示数据，需要在执行TensorFlow计算图的过程中，将各种类型的数据
	汇总并记录到日志文件中，然后使用TensorBoard读取这些日志文件，解析数据生成数据可视化的
	界面。
分布式并行
###
	1.TensorFlow的分布式并行基于gRPC通信框架，其中一个master创建Session。多个Worker负责执行计算图的任务。
	2.首先创建TensorFlow Cluster对象，包含一组task（通常每个task是一台单独的机器），用来分布式执行TensorFlow的计算图
	3.一个Cluster可以切分为多个Job，一个Job指一类特定的任务，一个Job包含多个task。为每个task创建server，然后连接到Cluster。

个人理解：
###
	task：我理解为是计算节点
	Cluster：我理解为是要计算的任务。将一个大的任务分为多个小任务（Job）。每一个小任务可以在多台task执行。
	第一步：我们需要为每一台机器（task）创建Server端（端口2222），然后连接到整个的集群环境中。
	可以一台机器多个task（即可看做多台机器）

创建TensorFlow并行计算
###
	1.Cluster对象通过tf.train.ClusterSpec来初始化。初始化信息是一个Python的字典。
	2.例如，tf.train.ClusterSpec({"ps":["192.168.1.1:2222"],"worker":["192.168.1.2:2222"],"worker":["192.168.1.3:2222"]})	
	ps:paramter server

分布式的方式：
###
	1.In-graph replication模型并行，将模型的计算图的不同部分放在不同的机器上执行。
	2.Between-graph replication数据并行，每台机器使用完全相同的计算图，但是计算不同的batch数据
	3.异步并行：每台机器独立计算梯度，一旦计算完更新到parameter server中，不等其他机器
	4.同步并行：等所有机器都完成对梯度的计算后，将多个梯度合并并统一更新模型参数。
