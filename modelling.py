from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

class VaccineModel:
    def __init__(self, df, target, model=None, scale=False):
        """
        - df: dataframe with encoded features and labels
        - target: target column name (str)
        - model: an sklearn model or pipeline
        - scale: whether to apply StandardScaler (recommended for LR)
        """
        self.df = df.copy()
        self.target = target
        self.scale = scale

        # Separate features and label
        self.X = self.df.drop(columns=['h1n1_vaccine', 'seasonal_vaccine'])
        self.y = self.df[target]

        # Handle model and optional scaling
        if model:
            self.model = model
        elif self.scale:
            self.model = Pipeline([
                ('scaler', StandardScaler()),
                ('classifier', LogisticRegression(max_iter=2000, solver='liblinear'))
            ])
        else:
            self.model = LogisticRegression(max_iter=2000, solver='liblinear')

        # Placeholder for splits and predictions
        self.X_train = self.X_test = self.y_train = self.y_test = self.y_pred = None


    # def __init__(self, df, target, model=None):
    #     """
    #     Initialize with:
    #     - df: df_encoded
    #     - target: string, the column name of the target variable
    #     - model: any sklearn classifier (default is LogisticRegression)
    #     """
    #     self.df = df.copy()
    #     self.target = target
    #     self.model = model if model else LogisticRegression(max_iter=2000)
        
    #     self.X = self.df.drop(columns=['h1n1_vaccine', 'seasonal_vaccine'])
    #     self.y = self.df[target]
    #     self.X_train, self.X_test, self.y_train, self.y_test = (None, None, None, None)
    #     self.y_pred = None

    def split_data(self, test_size=0.2, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, stratify=self.y)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        self.y_pred = self.model.predict(self.X_test)
        
        print(f"\n Evaluation for `{self.target}` using {self.model.__class__.__name__}:")
        print()
        print("Accuracy:", accuracy_score(self.y_test, self.y_pred))
        print("Precision:", precision_score(self.y_test, self.y_pred))
        print("Recall:", recall_score(self.y_test, self.y_pred))
        print("F1 Score:", f1_score(self.y_test, self.y_pred))
        print("\nConfusion Matrix:")
        print(confusion_matrix(self.y_test, self.y_pred))
        print("\nClassification Report:")
        print(classification_report(self.y_test, self.y_pred))
