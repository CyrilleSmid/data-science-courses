from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected = True)

def graph_val_acc_loss(history):
    history_dict = history.history
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    acc = history.history['acc']
    val_acc = history.history['val_acc']

    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(y=loss_values, 
                            line=dict(width=6),
                            name = 'Loss'),
                row=1, col=1)
    fig.add_trace(go.Scatter(y=val_loss_values, 
                            line=dict(width=3),
                            name = 'Validation Loss'),
                row=1, col=1)
    fig.add_trace(go.Scatter(y=acc, 
                            line=dict(width=6),
                            name = 'Accuracy'),
                row=2, col=1)
    fig.add_trace(go.Scatter(y=val_acc, 
                            line=dict(width=3),
                            name = 'Validation Accuracy'),
                row=2, col=1)
    fig.show()