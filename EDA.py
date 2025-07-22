import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class VaccineEDA:
    def __init__(self, df):
        self.df = df

    def value_counts(self, column, normalize=False):
        """
        Display value counts for a single column.
        Set normalize=True for proportions.
        """
        return self.df[column].value_counts(normalize=normalize)

    def plot_bar(self, column, hue=None, title=None):
        """
        Plot a barplot for a categorical column.
        Optionally add hue to show class breakdown.
        """
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x=column, hue=hue)
        plt.title(title or f"Distribution of {column}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_box(self, x, y, title=None):
        """
        Boxplot for comparing a numerical variable across categories.
        """
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=self.df, x=x, y=y)
        plt.title(title or f"{y} by {x}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self, method='pearson'):
        """
        Display a heatmap of correlation matrix for numerical features.
        """
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        corr = numeric_df.corr(method=method)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title(f"{method.capitalize()} Correlation Matrix")
        plt.tight_layout()
        plt.show()

    def crosstab_plot(self, feature, target):
        """
        Plot a stacked bar chart of crosstab (feature vs target).
        """
        ctab = pd.crosstab(self.df[feature], self.df[target], normalize='index')
        print(ctab)
        ctab.plot(kind='bar', stacked=True, colormap='viridis', figsize=(8, 5))
        plt.title(f"{feature} vs {target}")
        plt.ylabel("Proportion")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
