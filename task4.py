import pandas as pd

# Helper function to convert currency strings to numbers
def parse_currency(value):
    if pd.isna(value):
        return 0
    value = str(value).replace('$', '').replace(',', '').replace(' ', '')
    if '(' in value and ')' in value:
        value = '-' + value.replace('(', '').replace(')', '')
    try:
        return float(value)
    except:
        return 0

# Step 1: Load Excel file
file_path = 'Financials_Sample_Data.xlsx'
df = pd.read_excel(file_path)

# Step 2: Clean currency columns (Jan to Dec)
month_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for col in month_cols:
    df[col] = df[col].apply(parse_currency)

# Step 3: Data manipulation examples

# a. Total per month (sum of each column)
monthly_totals = df[month_cols].sum()

# b. Add a column for full year total
df['Annual_Total'] = df[month_cols].sum(axis=1)

# c. Filter only positive annual totals
positive_df = df[df['Annual_Total'] > 0]

# d. Group by Year and calculate total
yearly_total = df.groupby('Year')['Annual_Total'].sum().reset_index()

# Step 4: Save to Excel
with pd.ExcelWriter("Financials_Processed.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
    positive_df.to_excel(writer, sheet_name="Positive_Annuals", index=False)
    monthly_totals.to_frame("Monthly_Total").to_excel(writer, sheet_name="Monthly_Totals")
    yearly_total.to_excel(writer, sheet_name="Yearly_Totals", index=False)

print("Processing complete. Data saved to 'Financials_Processed.xlsx'")
