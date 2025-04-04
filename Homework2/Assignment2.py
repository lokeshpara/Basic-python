
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

"""# Load the Iris dataset"""

iris = datasets.load_iris()

"""# Convert to a DataFrame"""

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

"""# Display first few rows"""

print(df.head())

"""# Create Scatter plots for feature Pairs
## Generate all possible scatter plots

### 1.Add species to the DataFrame for better visualization
### 2.Species are labeled as 0, 1, or 2
``` ['setosa', 'versicolor', 'virginica']```
### 3.Convert to names
### 4.Use seaborn’s pairplot with hue (color by species)

### 5. Save Image
"""

save_path = 'scatter_plots_all_features.png'

df['species'] = iris.target
species_names = iris.target_names
df['species'] = df['species'].apply(lambda x: species_names[x])

plt.figure(figsize=(10, 8))
sns.pairplot(df, hue="species", palette="Set2", markers=["o", "s", "D"])

# Add title for clarity
plt.savefig(save_path)
plt.suptitle("Scatter Plots of All Feature Pairs (Colored by Species)", y=1.02, fontsize=14)
plt.show()

"""## Compute Correlation

### Compute the correlation matrix (excluding the 'species' column)

### Display the correlation matrix
"""

correlation_matrix = df.drop('species', axis=1).corr()

# Display the correlation matrix
print("Correlation matrix:\n")
print(correlation_matrix)

"""## Find the Strongest Positive Correlation

### Unstack and sort the correlations to find the strongest pair
### Remove self-correlations
### Take absolute value to identify the strongest relationship (optional)
``` correlations = correlations.abs()```

### Sort and get the pair with the highest positive correlation


"""

correlations = correlation_matrix.unstack()

correlations = correlations[correlations < 1]

strongest_pair = correlations.sort_values(ascending=False).idxmax()
highest_corr_value = correlations[strongest_pair]

print(f"\nStrongest positively correlated pair: {strongest_pair}")
print(f"Correlation value: {highest_corr_value:.2f}")

"""## Plot the Strongest Correlated Feature Pair

### Extract the two feature
### Plot with species coloring
### Add labels and title

### Save the image
"""

colab_save_path = 'iris_strongest_correlation_plot.png'
sys_path = 'iris_strongest_correlation_plot.png'

feature_x, feature_y = strongest_pair

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x=feature_x, y=feature_y, hue='species', palette='Set2', s=70, alpha=0.8)

plt.xlabel(feature_x.capitalize())
plt.ylabel(feature_y.capitalize())
plt.title(f"Strongest Positive Correlation: {feature_x} vs {feature_y} (r = {highest_corr_value:.2f})")
plt.grid(True)
plt.legend(title='Species')
plt.tight_layout()
plt.savefig(sys_path)
plt.show()
print(f"Plot saved to: {save_path}")

