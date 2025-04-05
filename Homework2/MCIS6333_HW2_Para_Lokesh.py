# Import required libraries for data manipulation and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

def load_iris_data():
    """Load and prepare the Iris dataset."""
    iris = datasets.load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    return df

def create_pair_plots(df, save_path='scatter_plots_all_features.png'):
    """Create scatter plots for all feature pairs."""
    plt.figure(figsize=(10, 8))
    sns.pairplot(df, hue="species", palette="Set2", markers=["o", "s", "D"])
    plt.suptitle("Scatter Plots of All Feature Pairs (Colored by Species)", y=1.02, fontsize=14)
    plt.savefig(save_path)
    plt.show()

def find_strongest_correlation(df):
    """Find and return the strongest correlated feature pair."""
    correlation_matrix = df.drop('species', axis=1).corr()
    correlations = correlation_matrix.unstack()
    correlations = correlations[correlations < 1]
    strongest_pair = correlations.sort_values(ascending=False).idxmax()
    highest_corr_value = correlations[strongest_pair]
    return strongest_pair, highest_corr_value, correlation_matrix

def plot_strongest_correlation(df, strongest_pair, highest_corr_value, save_path='iris_strongest_correlation_plot.png'):
    """Create a scatter plot for the strongest correlated feature pair."""
    feature_x, feature_y = strongest_pair
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=feature_x, y=feature_y, hue='species', 
                    palette='Set2', s=70, alpha=0.8)
    plt.xlabel(feature_x.capitalize())
    plt.ylabel(feature_y.capitalize())
    plt.title(f"Strongest Positive Correlation: {feature_x} vs {feature_y} (r = {highest_corr_value:.2f})")
    plt.grid(True)
    plt.legend(title='Species')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def analyze_iris_dataset():
    """Analyze the Iris dataset by creating visualizations and finding correlations."""
    # Load data
    df = load_iris_data()
    print("\n=== Iris Dataset Overview ===")
    print("First 5 rows of the dataset showing measurements and species:")
    print(df.head())
    print("\nDataset shape (rows, columns):", df.shape)
    print("Features available:", list(df.columns[:-1]))
    print("Species in dataset:", df['species'].unique())

    # Create pair plots
    print("\n=== Creating Scatter Plot Matrix ===")
    print("Generating scatter plots for all feature pairs...")
    create_pair_plots(df)
    print("Scatter plot matrix saved as 'scatter_plots_all_features.png'")

    # Find strongest correlation
    print("\n=== Correlation Analysis ===")
    print("Calculating correlation matrix between features:")
    strongest_pair, highest_corr_value, correlation_matrix = find_strongest_correlation(df)
    print("\nCorrelation matrix showing relationships between all features:")
    print(correlation_matrix)
    print(f"\nStrongest positively correlated feature pair: {strongest_pair}")
    print(f"Correlation coefficient: {highest_corr_value:.2f}")

    # Plot strongest correlation
    print("\n=== Creating Strongest Correlation Plot ===")
    print(f"Generating scatter plot for {strongest_pair[0]} vs {strongest_pair[1]}...")
    plot_strongest_correlation(df, strongest_pair, highest_corr_value)
    print("Strongest correlation plot saved as 'iris_strongest_correlation_plot.png'")

# Execute the analysis
analyze_iris_dataset()

