# Vaccine_Hesitance
Trying to figure our why some individuals will fail to get vaccinated.

---
 ## 1.Business Understanding 
 ---
 ###  Context
In 2009, the U.S. conducted the National H1N1 Flu Survey to understand vaccination behaviors during the H1N1 pandemic. This effort mirrors the challenges faced in the COVID-19 era. Understanding the factors that influence vaccine uptake can help public health officials design better vaccine access strategies, communication campaigns, and policy decisions.

###  Project Goal
**Predict whether a person received the H1N1 flu vaccine** based on their background, health behavior, beliefs, and socio-demographics.

This project aims to:
- Help public health departments **identify hesitant populations**
- Guide **targeted awareness campaigns**
- Support **data-driven resource allocation** (e.g., mobile clinics, outreach)
- Inform the design of **future vaccination strategies**

---
### Key Stakeholders
- **Public health officials** managing vaccination programs
- **Healthcare providers** engaging with patients and communities
- **Policy makers** determining communication and funding priorities
- **Data scientists** supporting health systems and NGOs

---

### Business Questions
1. Who is most likely to get vaccinated?
2. What demographic or behavioral features are associated with vaccine acceptance or hesitancy?
3. Can we predict unvaccinated individuals **before** a campaign begins?
4. How can public health campaigns be improved based on these insights?

---
## 2.Data Understanding

### Step 1. Loading the datasets provided

### Step 2: Data Cleaning and Preprocessing

Before proceeding to analysis, the raw data was thoroughly reviewed and cleaned to ensure consistency, reliability, and readiness for modeling.

### Objectives
- Prepare the dataset for bivariate and multivariate analysis.
- Standardize formats and handle missing or inconsistent entries.
- Implement reusable, object-oriented code for cleaning workflows.

### Cleaning Workflow

The following steps were taken:

1. **Initial Exploration**
   - Loaded and previewed the dataset structure.
   - Checked shape, column names, and data types.

2. **Handling Missing Values and Inconsistencies**
   - Identified and quantified missing values across columns.
   - Filled missing values:
     - Numeric columns → median
     - Categorical columns → mode
     - Text/object columns → `"Unknown"`

3. **Type Conversion**
   - Converted appropriate `float` and `object` columns with limited unique values to `category` dtype to optimize memory and modeling.

4. **Code Reusability**
   - Implemented a custom class `VaccineDataCleaner` using Object-Oriented Programming (OOP) principles to:
     - Merge features and labels
     - Clean and prepare the dataset
     - Return a clean, analysis-ready DataFrame
---

The cleaned dataset (`df_clean`) is now ready for:
- Exploratory Data Analysis (EDA)
- Bivariate and multivariate visualizations
- Feature selection and model training

---
## Step 3: Exploratory Data Analysis (EDA)

This section begins the EDA process using a custom `VaccineEDA` class to explore variable distributions, relationships, and patterns relevant to vaccine uptake.

From the two plots above we can see that almost half of the sampled population recieved the seasoal flu vaccine but less than 30% received the H1N1 vaccine. The seasonal vaccine has class balance while the H1N1 is quite imbalanced. 
- _Next we can assess whether the two target variables are independent_

#### Ordinal Encoding and Correlation Analysis

To prepare the data for correlation analysis and modeling:
- **Applied Ordinal Encoding**  
   All remaining categorical columns were converted to numeric format using `OrdinalEncoder`, which assigns integer values to each category. This is important because correlation requires numeric input.
- **Dropped object columns**  
   These columns are non-numeric and not suitable for correlation analysis.

- **Next Step – Crosstab Analysis**  
   For each of the top correlated features:
   - A crosstab will be created showing the relationship between feature values and vaccine uptake (`0` = not vaccinated, `1` = vaccinated).
   - These visualizations will help identify which features may be strong predictors for modeling.

---
---
## Step 4: Modeling – Predicting Vaccine Uptake

With the data cleaned, encoded, and explored, we now move into the **modeling phase**.

In this section, we aim to:
- Define our features (`X`) and target (`y`)
- Split the dataset into training and test sets
- Train baseline classification models (e.g., Logistic Regression, Decision Tree)
- Evaluate model performance using metrics such as **accuracy, precision, recall, and F1-score**
- Use confusion matrices and classification reports for deeper insight

We will begin with simple baseline models and progressively improve using:
- Hyperparameter tuning
- Cross-validation
- Feature engineering

Our goal: Build an effective model to predict whether a person received the **H1N1 vaccine** or the **Seasonal flu vaccine**, based on their characteristics, behaviors, and opinions.
