# https://www.youtube.com/watch?v=iEaVR1N8EEk&index=9&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm#t=610s
import tensorflow as tf

# training data
x_data = [[1.0] * 5,
          [0., 2., 0., 4., 0.],
          [1., 0., 3., 0., 5.]]
y_data = range(1, 5 + 1)

# Variables : so that W, b can be updated
# initialize with a random number
# actual initialization happens @ tf.initialize_all_variables()
W = tf.Variable(tf.random_uniform([1, 3], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

hypothesis = tf.matmul(W, x_data)  # H(x) = Wx + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))  # cost(W, b)

# Minimize
a = tf.Variable(0.1)  # learning rate alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    # intermediate report
    if 0 == step % 20:
        print step, sess.run(cost), sess.run(W), sess.run(b)
