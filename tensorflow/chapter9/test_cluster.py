import math
import tempfile
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#使用tf.app.flags定义标记，在命令行执行TensorFlow程序时设置参数。在命令行指定的参数会被TensorFlow读取，并直接转换为flags。
flags = tf.app.flags

#设定数据存储目录data_dir，默认为/tmp/mnist-data，隐藏节点数默认为100，训练最大步数train_steps默认为100000，batch size默认为100，学习速率为默认0.1
flags.DEFINE_string("data_dir","/tmp/mnist-data","Directory for storing mnist data")
flags.DEFINE_integer("hidden_units",100,"Number of units in the hidden layer of the NN")
flags.DEFINE_integer("train_steps",1000000,"Number of (global) training steps to perform")
flags.DEFINE_integer("batch_size",100,"Training batch size")
flags.DEFINE_float("learning_rate",0.01,"Learning rate")

#设定是否使用同步并行的标记sync_replicas默认为False，在命令行执行时可以设为True开启同步并行。同时设置累计多少个梯度来更新模型的值，默认None。
#这个参数代表进行同步并行时，一共积攒多少个batch的梯度才进行一次参数更新，设为None则使用worker的数量，即所有worker都完成一个batch的训练后再更新模型参数
flags.DEFINE_boolean("sync_replicas",False,"Use the sync_replicas (synchronized replicas) mode,wherein the parameter updates from workers are aggregated before applied to avoid stale gradients")
flags.DEFINE_integer("replicas_to_aggregate",None,"Number of replicas to aggregate before parameter update is applied (For sync_replicas mode only;default: num_workers)")

#定义ps的地址

flags.DEFINE_string("ps_hosts","172.26.10.87:2222","Comma-separated list of hostname:port pairs")
flags.DEFINE_string("worker_hosts","172.26.10.83:2222,172.26.10.123:2222","Comma-separated list of hostname:port pairs")
flags.DEFINE_string("job_name",None,"job name:worker or ps")
flags.DEFINE_integer("task_index",None,"Worker task index,should be >= 0. task_index=0 is the master worker task the performs the variable initialization")

FLAGS = flags.FLAGS
IMAGE_PIXELS = 28

#############################编写主函数master
def main(unused_argv):
    mnist = input_data.read_data_sets(FLAGS.data_dir,one_hot=True)
    if FLAGS.job_name is None or FLAGS.job_name == "":
        raise ValueError("Must specify an explicit `job_name`")
    if FLAGS.task_index is None or FLAGS.task_index == "":
        raise ValueError("Must specify an explicit `task_index`")
    print("job_name = %s" % FLAGS.job_name)
    print("task_index = %d" % FLAGS.task_index)

    ps_spec = FLAGS.ps_hosts.split(",")
    worker_spec = FLAGS.worker_hosts.split(",")

    #先计算一共的worker数量，使用tf.train.ClusterSpec生成一个TensorFlow Cluster的对象,传入的参数是ps和worker的地址信息

    num_workers = len(worker_spec)
    cluster = tf.train.ClusterSpec({"ps":ps_spec,"worker":worker_spec})
    server = tf.train.Server(cluster,job_name = FLAGES.job_name,task_index = FLAGS.task_index)
    if FLAGS.job_name == "ps":
        server.join()

    is_chief = (FLAGS.task_index == 0)
    worker_device = "/job:worker/task:%d/gpu:0" % FLAGS.task_index
    with tf.device(tf.train.replica_device_setter(worker_device=worker_device,ps_device="/job:ps/cpu:0",cluster=cluster)):
        global_step = tf.Variable(0,name="global_step",trainable = False)
    
###未完成，待续
