import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def thk_witherr(data, *args, **kwargs):
    sns.lineplot(data=data, **kwargs)
    plt.fill_between(x=data['x'], y1=data['y']-2*data['std'], y2=data['y']+2*data['std'], alpha=0.2)

    print(args[0])

    plt.show()


data = {'x': np.linspace(1, 100, num=50),
        'y': np.linspace(-100, 50, num=50),
        'std': np.random.randint(5,10,size=50)}


df = pd.DataFrame(data)
print(df)


thk_witherr(data, 1, x='x', y='y')


