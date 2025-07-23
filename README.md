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

---
## Key Insights and Reommendations

This analysis of the 2009 H1N1 Flu Survey provided key insights into factors that influence vaccine uptake for both H1N1 and seasonal flu. The findings are valuable for guiding future public health strategies and improving vaccine campaign outcomes.

### Key Insights

- **Doctor Recommendations Matter**  
  Respondents who received a recommendation from a healthcare provider were **significantly more likely** to get vaccinated. This highlights the crucial role of **trusted messengers** in influencing public behavior.

- **Perceptions of Risk and Effectiveness Drive Behavior**  
  Higher **perceived risk** of flu and greater **confidence in vaccine effectiveness** were positively correlated with vaccine uptake. Conversely, fears of **side effects** were associated with hesitancy.

- **Behavioral Factors Provide Predictive Signals**  
  Preventive actions such as **mask-wearing, handwashing, and avoiding crowds** were often aligned with vaccine acceptance. These behavioral cues can be early indicators of openness to vaccination.

- **Sociodemographic Patterns are Uneven**  
  Vaccine uptake varied by **age group, education level, and employment sector**. Tailoring campaigns to different demographics can improve reach and effectiveness.

- **Model Performance is Promising**  
  Both Logistic Regression and Decision Tree classifiers achieved over **82% accuracy**. While Logistic Regression performed slightly better in terms of recall and precision for H1N1 predictions, Decision Trees were easier to interpret and showed comparable F1 scores.

---

###  Recommendations for Stakeholders

- **Public Health Officials**  
  Target individuals with low vaccine uptake using behavioral and demographic signals. Strengthen community-based strategies and deploy trained communicators.

- **Healthcare Providers**  
  Actively discuss vaccine benefits and risks with patients. Provider recommendation is a key driver of acceptance.

- **Policy Makers**  
  Invest in educational campaigns that correct misconceptions. Prioritize **health literacy** initiatives and fund **data-driven outreach programs**.

- **Data Scientists & NGOs**  
  Build predictive tools into health information systems to **flag high-risk groups** before campaigns launch. Use interpretable models to guide real-time decisions.

---
 By leveraging these insights, vaccination programs can become more strategic, equitable, and impactful.
