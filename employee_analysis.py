import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("employee_analytics_data.xlsx")
print(df.head())


print(df.isnull().sum())
df.columns = df.columns.str.strip()
print(df.describe())


total_employees = df.shape[0]
print("Total Employees:", total_employees)

attrition_rate = df['AttritionFlag'].sum() / total_employees * 100
print("Attrition Rate:", round(attrition_rate,2), "%")


avg_salary_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_dept)


left_employees = df[df['LeftCompany']=='Yes'][['EmployeeID','Name','Department']]
print(left_employees)


high_risk = df[(df['Performance']<=2) & (df['Attendance']<75)]
print(high_risk[['Name','Department','Performance','Attendance']])


sns.countplot(x='Department', hue='AttritionFlag', data=df)
plt.title('Attrition by Department')
plt.show()

df.groupby('Department')['Salary'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Salary by Department')
plt.ylabel('Salary')
plt.show()

sns.scatterplot(x='Experience', y='Salary', hue='Department', data=df)
plt.title('Experience vs Salary')
plt.show()

sns.boxplot(x='Department', y='Performance', data=df)
plt.title('Performance Distribution by Department')
plt.show()


df.to_excel("employee_analysis_ready.xlsx", index=False)
