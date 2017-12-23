###第3章第2节，TensorFlow实现Softmax Regression识别手写数字

#MNIST简介：简单的机器视觉数据集，由几万张手写数字组成，图片只包含灰度值信息
#在训练集上训练模型，在验证集上检验效果，并决定何时完成训练，最后在测试集测试效果（图像是28像素X28像素大小的灰度图片）
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

######运行之后的结果：训练数据的特征是55000X784的Tensor，第一个维度是图片的编号，第二个维度是像素的编号，训练数据的Label是55000X10的Tensor
#print(mnist.train.images.shape,mnist.train.labels.shape)
#print(mnist.test.images.shape,mnist.test.labels.shape)
#print(mnist.validation.images.shape,mnist.validation.labels.shape)

#(55000, 784) (55000, 10)
#(10000, 784) (10000, 10)
#(5000, 784) (5000, 10)

#准备好数据后，设计算法，这里使用Softmax Regression的算法训练手写数字识别的分类模型
import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32,[None,784]) 
#1.创建新的InteractiveSession，使用这个命令将session注册为默认的session，之后的运算跑在这个session中，不同session之间的数据和运算应相互#独立
#2.创建Placeholder，即输入数据的地方。
#2.1Placeholder的第一个参数是数据模型
#2.2Placeholder的第二个参数[None,784]代表的是tensor的shape，也就是数据的尺寸。[None,784]None代表不限条数的输入，784代表784维的向量

#接下来给Softmax Regression模型中的weights和biases创建Variable对象（第一章提到Variable是用来存储模型参数的Variable在模型训练迭代中是持久化的）

#将Vweights和biases全部初始化为0
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#实现Softmax Regression算法
y = tf.nn.softmax(tf.matmul(x,W)+b)
#Softmax是tf.nn下面的一个函数，tf.nn包含了大量神经网络的组件，tf.matmul是TensorFlow中的矩阵乘法函数

#为了训练模型，需要定义一个loss function来描述模型对问题的分类精度。Loss越小，代表模型的分类结果与真实值的偏差越小，模型越精确。
#训练的目的就是将Loss减小，直到达到全局最优或局部最优解。
y_ = tf.placeholder(tf.float32,[None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))

#1.定义优化算法后开始训练（采用常见的随机梯度下降（SGD））。
#2.定义好优化算法后，TensorFlow根据我们定义的整个计算图自动求导，并根据反向传播算法进行训练。在每一轮迭代时更新参数来减小Loss
#3.在后台TensorFlow会自动添加许多运算操作（Operation）来实现反向传播和梯度下降，提供给我们的是封装好的优化器，只要提供数据就好了。
#4.调用tf.train.GradientDescentOptimizer，并设置学习效率为0.5，优化目标设定为cross-entropy，得到进行训练的操作train_step

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#使用TensorFlow的全局参数初始化器tf.global_variables_initializer，并执行run()
tf.global_variables_initializer().run()

#开始迭代的执行训练操作train_step：每次随机从训练集中抽取100条样本构成一个mini-batch,并feed给placeholder

#然后调用train_step对这些样本进行训练。
for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs,y_: batch_ys})
#此时完成了训练，接下来就是对模型的准确率进行验证

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
#tf.argmax从tensor中寻找最大值的序号。例如：tf.argmax(y,1)求各个预测的数字中概率最大的那一个，tf.argmax(y_,1)求样本真实数字类别

#tf.equal方法则用来判断预测的数字类别是否是正确的类别，最后返回计算分类是否正确的操作correct_prediction

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))

#统计全部样本预测的accuracy，需要先用tf.cast将之前的correct_prediction输出的bool值转换为float32,再求平均  
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

#将测试数据的特征和Label输入评测流程accuracy，计算模型在测试集上的准确率，再打印出来。
print(accuracy.eval({x: mnist.test.images,y_: mnist.test.labels}))


##############注释：
####通过这个例子，使用TensorFlow实现了一个简单的机器学习算法Softmax Regression。
####一个四个流程
###1、定义算法公式
###2、定义Loss，选定优化器，指定优化器优化Loss
###3、迭代地对数据进行训练
###4、在测试集或验证集上对准确率进行预测
####类似于Spark，定义公式只是Compution Graph，等run()方法调用时，并feed数据时，才真正执行。

