import pandas as pd
def performance_label(P):
   if P > 85:
      label = "Excellent"
   elif P > 70:
      label = "Good"
   elif P > 50:
      label = "Average"
   else:
      label = "Poor"
   return label
 
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
df_left_join["Class"] = df_left_join["Class"].fillna("11.0")
df_left_join["Total_Marks"] = df_left_join[["Maths","English","Science"]].sum(axis = 1)
df_left_join["Percentage"] = (df_left_join["Total_Marks"] / 300) * 100
print("Left Join")
print(df_left_join[["Student_Name","Class","City","Maths","Science","English","Total_Marks","Percentage"]])
df_left_join.to_csv("outputs/MasterFile.csv")
outer_join = pd.merge(df_marks,df_info, on="Student_Name",how="outer")
df_left_join['City'] = df_left_join['City'].fillna("Banglore")
print(df_left_join)

## group by
class_wisee_avg = df_left_join.groupby("Class")[["Science","Maths","English"]].mean()
city_wis_avg = df_left_join.groupby("City")[["Science","Maths","English"]].mean()
summary = df_left_join.groupby("Class").agg(
   Class_wise_students = ("Student_Name","count"),
   Maths_mean = ("Maths", "mean"),
   English_mean = ("English","mean"),
   Science_mean = ("Science","mean"),
   Total_marks_mean = ("Total_Marks","mean"),
   class_wise_topper = ("Total_Marks","max")
)
summary = summary.reset_index()
summary.to_csv("outputs/SummaryFile.csv",index = False)
print("Class Wise Summary")
print(summary)

df = df_left_join
## groupby - advanced
class_city_avg = (
    df
    .groupby(["Class", "City"])[[ "Maths","Science","English"]]
    .mean()
    .reset_index()
)
class_city_count = (
    df.groupby(["Class","City"])["Student_Name"].count().reset_index()
 )
print(class_city_count)
class_city_percentage = (
   df.groupby(["Class","City"])["Percentage"].mean().reset_index(name="Percentage_Mean")
)
print(class_city_percentage)
df["Performance"] = df["Percentage"].apply(performance_label)
performance_dist = (
   df.groupby(["Class","Performance"])["Student_Name"].count().reset_index(name = "Count")
)
print(performance_dist)
print("Class-City-Performance-Wise")
class_city_wise = (df.groupby(["Class","City","Performance"])["Student_Name"].count().reset_index())
print(class_city_wise)
# total_per_class = (
#     performance_dist.groupby("Class")["Count"]
#     .transform("sum")
# )
# performance_dist["Percentage"] = (
#     performance_dist["Count"] / total_per_class * 100
# ).round(2)

# print(performance_dist)
total_per_class = (
   performance_dist.groupby("Class")["Count"].transform("sum")
)
print(total_per_class)
performance_dist["Percentage"] = performance_dist["Count"]/total_per_class * 100
print(performance_dist)
### overall Class
class_overall = (
    df.groupby("Class")[["Maths", "Science", "English"]]
      .mean()
)
print(class_overall)
class_overall["Overall_Mean"] = class_overall.mean(axis=1)
print(class_overall)
class_overall = class_overall.sort_values("Overall_Mean", ascending=False)
print(class_overall)

class_city_count.to_csv("outputs/class_city_count.csv", index=False)
class_city_avg.to_csv("outputs/class_city_avg.csv", index=False)
performance_dist.to_csv("outputs/performance_distribution.csv", index=False)
class_overall.reset_index().to_csv("outputs/class_overall_ranking.csv", index=False)
