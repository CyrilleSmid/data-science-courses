from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected = True)

def plot_val_acc_loss(history, metrics=['loss', 'acc']):
    history_dict = history.history
    fig = make_subplots(rows=len(metrics), cols=1)
    for i, metric in enumerate(metrics):
        loss_values = history_dict[metric]
        val_loss_values = history_dict['val' + metric]
        fig.add_trace(go.Scatter(y=loss_values, 
                                line=dict(color='royalblue', width=6),
                                name = metric),
                    row=i+1, col=1)
        fig.add_trace(go.Scatter(y=val_loss_values, 
                                line=dict(color='crimson', width=3),
                                name = 'Validation ' + metric),
                    row=i+1, col=1)
    fig.show()