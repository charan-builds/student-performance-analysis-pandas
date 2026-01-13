import pandas as pd
df_marks = pd.read_csv("data/student_performance.csv")
df_info = pd.read_csv("data/students_info.csv")
print(df_marks.head())
print(df_info.head())
#Inner Join 
df_inner_join = pd.merge(df_marks,
                   df_info,
                   on= "Student_Name",
                   how= "inner"
                )
#Print Inner Join
print("\nInner Join")
print(df_inner_join)
df_left_join = pd.merge(df_marks,df_info,on="Student_Name",how = "left")
print(df_left_join.isnull().sum())
df_left_join["City"] = df_left_join["City"].fillna("Unknown")
df_left_join["Class"] = df_left_join["Class"].fillna("Unknown")
df_left_join["Total_Marks"] = df_left_join[["Maths","English","Science"]].sum(axis = 1)
df_left_join["Percentage"] = (df_left_join["Total_Marks"] / 300) * 100
print("Left Join")
print(df_left_join[["Student_Name","Class","City","Maths","Science","English","Total_Marks","Percentage"]])
df_left_join.to_csv("outputs/MasterFile.csv")
outer_join = pd.merge(df_marks,df_info, on="Student_Name",how="outer")

outer_join["City"] = outer_join["City"].fillna("Banglore")
print(outer_join)
