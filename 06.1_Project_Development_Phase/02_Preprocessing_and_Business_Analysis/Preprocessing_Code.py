import pandas as pd
import numpy as np

# ==============================
# 1. Load Dataset
# ==============================

file_path = 01_Indian_Union_Budget_Dataset.csv
df = pd.read_csv(file_path)

print(Original Shape, df.shape)

# ==============================
# 2. Standardize Column Names
# ==============================

df.columns = df.columns.str.strip() 
                       .str.lower() 
                       .str.replace( , _)

# ==============================
# 3. Remove Duplicate Rows
# ==============================

df.drop_duplicates(inplace=True)

# ==============================
# 4. Handle Missing Values
# ==============================

# For numeric columns → fill with median
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols
    df[col].fillna(df[col].median(), inplace=True)

# For categorical columns → fill with mode
categorical_cols = df.select_dtypes(include=object).columns

for col in categorical_cols
    df[col].fillna(df[col].mode()[0], inplace=True)

# ==============================
# 5. Convert Data Types (if needed)
# ==============================

for col in numeric_cols
    df[col] = pd.to_numeric(df[col], errors=coerce)

# ==============================
# 6. Remove Outliers (IQR Method)
# ==============================

for col in numeric_cols
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5  IQR
    upper_bound = Q3 + 1.5  IQR
    
    df = df[(df[col] = lower_bound) & (df[col] = upper_bound)]

print(Shape After Outlier Removal, df.shape)

# ==============================
# 7. Final NA Check
# ==============================

df.dropna(inplace=True)

# ==============================
# 8. Save Cleaned Dataset
# ==============================

output_file = Cleaned_Dataset.csv
df.to_csv(output_file, index=False)

print(Cleaned dataset saved as, output_file)
print(Final Shape, df.shape)
