# Iris Dataset Feature Analysis

This Python script analyzes and visualizes relationships between different features of the famous Iris dataset using scatter plots and correlation analysis.

## Assignment Description

This code is part of a data visualization assignment that focuses on:
1. Creating scatter plots for all pairs of features in the Iris dataset
2. Identifying and visualizing the feature pair with the strongest positive correlation

## Dataset Information

The Iris dataset contains measurements of three different Iris flower species:
- Setosa
- Versicolor
- Virginica

### Features
1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

## Code Functionality

The script performs the following operations:
1. Loads the Iris dataset from scikit-learn
2. Creates a comprehensive visualization of all feature pairs using scatter plots
3. Calculates correlations between all features
4. Identifies the strongest positively correlated feature pair
5. Creates a detailed scatter plot for the most strongly correlated features

## Output Files

The script generates two visualization files:

### 1. Scatter Plots Matrix (All Features)
This visualization shows the relationships between all pairs of features in the Iris dataset:

![Scatter Plots Matrix](scatter_plots_all_features.png)

### 2. Strongest Correlation Plot
This plot shows the scatter plot of the most strongly correlated feature pair:

![Strongest Correlation](iris_strongest_correlation_plot.png)

## Requirements

The following Python libraries are required:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

## How to Run

1. Ensure all required libraries are installed
2. Run the script using Python:
   ```
   python assignment2.py
   ```
3. The script will display the visualizations and save them as PNG files

## Author

[Lokesh Para]

## Assignment Context

This code is part of the Data Visualization course assignment, focusing on creating simple scatter plots using Matplotlib and analyzing feature relationships in the Iris dataset. 