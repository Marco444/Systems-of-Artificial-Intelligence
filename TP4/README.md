
# TP4 SIA - Unsupervised Learning

## Introduction

This is an orientation practical assignment for the course on Artificial Intelligence Systems, with the objective of implementing various unsupervised learning algorithms.

[Assignment](docs/Enunciado.pdf)

### Requirements

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Installation

Standing in the root directory, run

```sh
pipenv install
```

to install the necessary dependencies in the virtual environment.

# Exercise 1 - Kohonen
## Execution
### `src/kohonen/main.py`
The program `src/kohonen/main.py` runs the Kohonen algorithm to solve the country clustering problem.
It is executed with the following command:
```sh
pipenv run python src/kohonen/main.py [config_file]
```

```json
{
  "input": "Input CSV file - String",
  "initial_radius": "Initial radius - Float",
  "initial_eta": "Initial eta - Float",
  "size": "Network size (k) - Int",
  "variable_radius": "Indicates if the radius is variable - Boolean",
  "variable_eta": "Indicates if eta is variable - Boolean",
  "mult_iterations": "Number of epochs - Int",
  "similarity": "Similarity function - [EUCLIDEAN, EXP]",
  "data_initialization": "Indicates if data is initialized with the input - Boolean",
  "heatmap_title": "Title of the Heatmap chart - String",
  "u_matrix_title": "Title of the U Matrix chart - String"
}
```

#### Result
The program displays the Heatmap and U Matrix charts after training the model with the input data.

<img src="images/kohonen_heatmap.png" width="1000" alt="Kohonen Heatmap">
<img src="images/kohonen_umatrix.png" width="1000" alt="Kohonen U-Matrix">


# Exercise 2 - Principal Components
## Execution
### PCA - `src/PCA/main.py`
The program `src/PCA/main.py` runs the PCA algorithm, using the [scikit-learn](https://scikit-learn.org/stable/) library.
It is executed with the following command:
```sh
pipenv run python src/PCA/main.py [config_file]
```

```json
{
  "input": "Input CSV file - String",
  "n_components": "Number of principal components - Int"
}
```

#### Result
The program displays the following charts:
- Boxplot of standardized variables
   <br><img src="images/pca_boxplot.png" width="1000" alt="PCA Boxplot"> 
- Bar chart of PC1 by country
   <br><img src="images/pca_pc1.png" width="1000" alt="PCA PC1">
- Biplot of PC1 and PC2
   <br><img src="images/pca_biplot.png" width="1000" alt="PCA Biplot">

It also prints to STDOUT a list of countries sorted (ascending) by their PC1 value.


### Oja - `src/oja/main.py`
The program `src/oja/main.py` runs the Oja rule algorithm, obtaining the eigenvector associated with PC1.
It is executed with the following command:
```sh
pipenv run python -m src.oja.main [config_file]
```

```json
{
  "input": "Input CSV file - String",
  "eta": "Initial eta - Float",
  "limit": "Number of epochs - Int"
}
```

#### Result
The program prints to STDOUT the eigenvector associated with PC1.


### Sanger - `src/sanger/main.py`
The program `src/sanger/main.py` runs the Sanger rule algorithm, obtaining the eigenvectors associated with the principal components.
It is executed with the following command:
```sh
pipenv run python -m src.sanger.main [config_file]
```

```json
{
  "input": "Input CSV file - String",
  "eta": "Initial eta - Float",
  "limit": "Number of epochs - Int",
  "n_components": "Number of principal components - Int"
}
```

#### Result
The program prints to STDOUT the eigenvectors associated with the principal components.


# Exercise 3 - Patterns - Hopfield Model
<img src="images/hopfield_patterns.png" width="1000" alt="Hopfield Patterns">

## Execution
### `src/hopfield/main.py`
This program takes a set of patterns to store and a pattern to recognize using the Hopfield model.
It is executed with the following command:
```sh
pipenv run python src/hopfield/main.py [config_file]
```

An example of config_file is the following:
```json
{
  "input": "storedPatterns.txt",
  "try": "try.txt",
  "size": 25,
  "max_iterations": 100,
  "noise": false,
  "probability_of_noise": 0.9,
  "plot_states": true,
  "plot_energy": true,
  "plot_stored_patterns": true
}
```

- "input" -> File with the patterns to store
- "try" -> File with the pattern to recognize
- "size" -> Input dimension. It must be the multiplication of width and height.
- "max_iterations" -> Maximum number of iterations if no previously repeated state is found
- "noise" -> Boolean, determines whether noise will be applied to the input or not
- "probability_of_noise" -> If "noise": true, this is the probability that a position in the pattern will be altered
- "plot_states" -> Boolean, indicates whether to graph the evolution of states
- "plot_energy" -> Boolean, indicates whether to graph the evolution of Hopfield's energy
- "plot_stored_patterns" -> Boolean, indicates whether to graph the stored patterns

### `src/hopfield/analysis.py`
This program takes all available patterns and looks for combinations of parametrizable size, analyzing the orthogonality between them.
At the end, it shows two charts: the first 25 with the lowest average orthogonality and the last 5.
```sh
pipenv run python src/hopfield/analysis.py [config_file]
```

```json
{
  "input": "letters.txt",
  "combination_size": 7,
  "try": "try.txt",
  "size": 25,
  "max_iterations": 100
}
```
- "input" -> File where all patterns are stored
- "combination_size" -> Size of the combinations
- "size" -> Input dimension. It must be the multiplication of width and height.
- "max_iterations" -> Maximum number of iterations if no previously repeated state is found

### `src/hopfield/analysis_multiple_combinations.py`
This program repeats the previous analysis but for a range of combination sizes.
```sh
pipenv run python src/hopfield/analysis_multiple_combinations.py [config_file]
```
It takes the same config as the previous one, but a bar chart will be shown, with the minimum average orthogonality for each combination size.
