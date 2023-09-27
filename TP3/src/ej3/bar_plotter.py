import pandas as pd
import plotly.graph_objects as go
import sys

def bar_plot(csv_filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_filename)

    # Create a column 'perceptrons_for_layers' that combines 'entrada', 'capas_ocultas', and 'salida'
    df['perceptrons_for_layers'] =  df['capas_ocultas'].astype(str)
    
    # Find the minimum 'error_training' and 'error_test' for each iteration within each 'config_id'
    min_errors_df = df.groupby(['config_id', 'iteration', 'perceptrons_for_layers']).agg({'error_training': 'min', 'error_test': 'min'}).reset_index()

    # Compute the mean and standard deviation of those minimum errors across all iterations for each 'config_id'
    statistics_df = min_errors_df.groupby(['config_id', 'perceptrons_for_layers']).agg({'error_training': ['mean', 'std'], 'error_test': ['mean', 'std']}).reset_index()

    # Sort by the length of 'capas_ocultas'
    statistics_df['sort_key'] = statistics_df['perceptrons_for_layers'].apply(len)
    statistics_df = statistics_df.sort_values('sort_key').reset_index(drop=True)

    # Create the bar plot
    fig = go.Figure()

    for error_type, label in [('error_training', 'Error de Entrenamiento'), ('error_test', 'Error de Prueba')]:
        fig.add_trace(go.Bar(
            x=statistics_df['perceptrons_for_layers'],
            y=statistics_df[(error_type, 'mean')],
            name=label,
            error_y=dict(type='data', array=statistics_df[(error_type, 'std')]),
        ))

    # Add Spanish labels
    fig.update_layout(
        title='Mejor Error de Entrenamiento y Prueba para Cada Configuración',
        xaxis_title='Numero de Capas',
        yaxis_title='Mejor Error Promedio',
        barmode='group'
    )

    # Show the plot
    fig.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporcione la ruta al archivo CSV como un argumento.")
        sys.exit(1)

    bar_plot(sys.argv[1])

