# https://www.youtube.com/watch?v=pHPmzTQ_e2o&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=6#t=59.448354
import tensorflow as tf
import matplotlib.pyplot as plt

# training data
X = [1., 2., 3.]
Y = [1., 2., 3.]
m = n_samples = len(X)

W = tf.placeholder(tf.float32)

# Construct a linear model
hypothesis = tf.mul(X, W)

# Cost function
cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2)) / (m)  # cost(W, b)

# Initializing the variables
init = tf.initialize_all_variables()

# For graphs
W_val = []
cost_val = []

# Launch the graph
sess = tf.Session()
sess.run(init)
for i in range(-30, 50):
    print i * 0.1, sess.run(cost, feed_dict={W: i * 0.1})
    W_val.append(i * 0.1)
    cost_val.append(sess.run(cost, feed_dict={W: i * 0.1}))

# Graphic display
plt.plot(W_val, cost_val, 'ro')
plt.ylabel('Cost')
plt.xlabel('W')
plt.show()
