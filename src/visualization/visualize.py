import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# axisX = "Setor" => df['Setor']


def barra_vertical_media_nps_mean_by(df, axisX):
    axisX_labels = df.groupby([f"{axisX}"]).mean()['NPS interno'].index
    nps_media_mean_by_axisX = df.groupby([f"{axisX}"]).mean()[
        'NPS interno'].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(axisX_labels, nps_media_mean_by_axisX)
    ax.set_ylabel("NPS interno mensal médio")
    ax.set_yticks(np.arange(0, 11, 1))
    ax.set_title(f"Média de NPS interno mensal por {axisX}")
    fig.savefig('graph_last_generate.png')
    return plt.close(fig)


def hist_nps(df):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(df['NPS interno'])
    ax.set_title('Distribuição de NPS interno mensal')
    ax.set_xlabel("NPS interno mensal")
    fig.savefig('hist_graph_last_generate.png')
    return plt.close(fig)
