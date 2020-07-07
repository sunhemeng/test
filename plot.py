import matplotlib.pyplot as plt
import numpy as np



plt.figure()
plt.plot(e, QN.critic_loss_a)
plt.xlabel('episodes')
plt.ylabel('loss')
plt.show()