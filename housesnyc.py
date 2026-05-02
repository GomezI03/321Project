# ============================================
# Exploratory Data Analysis (EDA) - Save Outputs
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --------------------------------------------
# 1. Load Dataset (same folder)
# --------------------------------------------

df = pd.read_csv('AB_NYC_2019.csv')

# Create output folder
output_folder = 'eda_output'
os.makedirs(output_folder, exist_ok=True)

# --------------------------------------------
# 2. Save Text Outputs to File
# --------------------------------------------

with open(os.path.join(output_folder, 'summary.txt'), 'w') as f:
    f.write("=== FIRST 5 ROWS ===\n")
    f.write(df.head().to_string())
    
    f.write("\n\n=== INFO ===\n")
    df.info(buf=f)
    
    f.write("\n\n=== SUMMARY STATISTICS ===\n")
    f.write(df.describe().to_string())
    
    f.write("\n\n=== MISSING VALUES ===\n")
    f.write(df.isnull().sum().to_string())
    
    f.write("\n\n=== DUPLICATES ===\n")
    f.write(str(df.duplicated().sum()))

# --------------------------------------------
# 3. Correlation Matrix Save
# --------------------------------------------

corr = df.corr(numeric_only=True)
corr.to_csv(os.path.join(output_folder, 'correlation.csv'))

# --------------------------------------------
# 4. Visualizations (Saved as Images)
# --------------------------------------------

# Histogram
plt.figure()
df['price'].hist()
plt.title('Distribution of Airbnb Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_folder, 'histogram_price.png'))
plt.close()
# Interpretation: Prices are right-skewed with many low values and few high outliers.

# Box Plot
plt.figure()
df['price'].plot(kind='box')
plt.title('Box Plot of Prices')
plt.ylabel('Price')
plt.savefig(os.path.join(output_folder, 'boxplot_price.png'))
plt.close()
# Interpretation: Many extreme outliers exist in price.

# Scatter Plot
plt.figure()
plt.scatter(df['number_of_reviews'], df['price'])
plt.title('Price vs Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.savefig(os.path.join(output_folder, 'scatter_reviews_price.png'))
plt.close()
# Interpretation: Weak or no strong relationship between reviews and price.

# Bar Chart
plt.figure()
df['room_type'].value_counts().plot(kind='bar')
plt.title('Room Type Counts')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.savefig(os.path.join(output_folder, 'bar_room_type.png'))
plt.close()
# Interpretation: Entire homes are the most common listing type.

# --------------------------------------------
# Done
# --------------------------------------------

print(f"EDA outputs saved in folder: {output_folder}")