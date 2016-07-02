# https://www.youtube.com/watch?v=FiPpqSqR_1c#t=181s

import numpy as np
import tensorflow as tf

xy = np.loadtxt('train.txt', unpack=True, dtype='float32')
x_data = np.transpose(xy[0:3])
y_data = np.transpose(xy[3:])

# tf Graph Input
X = tf.placeholder("float", [None, 3])  # x1, x2 and 1 (for bias)
Y = tf.placeholder("float", [None, 3])  # A, B, C => 3 classes

# Set model weights
W = tf.Variable(tf.zeros([3, 3]))

# Construct model
hypothesis = tf.nn.softmax(tf.matmul(X, W))  # Softmax

# Minimize error using cross entropy
learning_rate = 0.001

# Cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), reduction_indices=1))

# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    for step in range(2000 + 1):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if 0 == step % 200:
            print step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W)
