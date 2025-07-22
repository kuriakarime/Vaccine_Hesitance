class VaccineDataCleaner:
    def __init__(self, features_df, labels_df):
        self.df = features_df.merge(labels_df, on='respondent_id')
        self.cleaned = None
    
    def fill_missing(self):
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        
        category_cols = self.df.select_dtypes(include='category').columns
        self.df[category_cols] = self.df[category_cols].apply(lambda x: x.fillna(x.mode()[0]))
        
        self.df = self.df.fillna('Unknown')

    # loop through the columns and columns with less than 10 unique values considered categorical
    def convert_types(self, max_unique=10):
    # Loop through object and float columns
        for col in self.df.columns:
            if self.df[col].dtype in ['object', 'float64']:
                unique_vals = self.df[col].nunique(dropna=True)
                if unique_vals <= max_unique:
                    self.df[col] = self.df[col].astype('category')
    
    def get_cleaned_data(self):
        return self.df.copy()
