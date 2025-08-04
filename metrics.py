import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix
#test case 1
'''y_true = ['Y','Y','Y','Y']
y_pred = ['N','N','N','N']

#test case 2
y_true = ['Y','N','Y','Y']
y_pred = ['N','N','N','N']

#test case 3
y_true = ['Y','N','N','Y']
y_pred = ['N','N','N','N']'''

y_true = ['Y','N','N','N']
y_pred = ['N','N','N','N']


print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))
cm = confusion_matrix(y_true, y_pred)

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['True 0', 'True 1'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

plot_confusion_matrix(y_true,y_pred)