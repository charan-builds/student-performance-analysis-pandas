import pandas as pd
df = pd.read_csv("data/student_performance.csv")
def label_performance(percentage):
  if(percentage >= 85):
    return "Excellent"
  elif(percentage >= 70):
    return "Good"
  elif(percentage >= 50):
    return "Average"
  else:
    return "Weak"
  

print("\nTotal No of Students: {}".format(len(df)))
print("\n----------Info------------")
df.info()
print("\n---------Description-------")
print(df.describe())
# head for people on top  and tail for people on end  in dataFrame
print(df.head())
print(df.tail())
#column_selection
marks_df = df[["Student_Name", "Maths" , "Science"]]
# print(marks_df.head())
 
# df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]
# print(df.head())


#Scoring High Marks in Maths
# print("\nHighest Marks Student In Maths")
MaxMaths = df["Maths"].max()
# print(df[df["Maths"] == MaxMaths])
# collecting top score persons in a class
# print("----Toppers In Class-----")
# Top_Marks = 270
# Toppers = df[df["Total_Marks"] > Top_Marks]
# print(Toppers[["Student_Name","Total_Marks"]])

#Weak Students in subject_wise
# print("WeakStudents")
# weakStudents = df[(df["Maths"] < 60 ) |
#                   (df["English"] < 60 ) |
#                   (df["Science"] < 60 )
#                 ]
# print(weakStudents[["Student_Name","Maths","Science","English"]])


# class Average Subject wise
# print("\nMaths Average : " ,df["Maths"].mean())
# print("\nEnglish Average : ",df["English"].mean())
# print("\nScience Average : ",df["Science"].mean())
# print()
# # Total Average 
# print("TotalAverage : ",df["Total_Marks"].mean())

# Method to calculate column wise marks
# print(df[["English","Maths","Science"]].mean(axis = 0))
df["Total_Marks"] = (df[["English","Maths","Science"]].sum(axis = 1))
# print(df.head())


# subject_totals = df[["Maths", "Science", "English"]].sum(axis=0).reset_index()
# subject_totals.columns = ["Subject", "Total_Marks"]
# print(subject_totals)

# calculate Percentage 
Total_Possible_Marks = 300
df["Percentage"] = (df["Total_Marks"] / 300)* 100
# print(df.head())

df["Label"] = df["Percentage"].apply(label_performance)
# print(df.head())

# Ranking Students
df_sorted_total= df.sort_values(by = "Total_Marks" , ascending = False )


#week_students 
week_students = df[df["Label"] == "Weak"]
# print(week_students[["Student_Name","Maths","English","Science","Total_Marks"]])
final_table = df_sorted_total[["Student_Name","Maths","English","Science","Total_Marks","Percentage"]]

df_sorted_percentage = df.sort_values(by = "Percentage", ascending = False )
# print()
# print(df_sorted_percentage.head())
df_sorted_multi = df.sort_values(by = ["Total_Marks", "Maths"] , ascending= [True,False])
# print("------Sorted_Multiple_Rows-----")
# print(df_sorted_multi.head())

# to display the tables 
print("---------FinalTable--------")
print(final_table)
print("\n ------------Top Performances------------------") 
Toppers_students = df_sorted_total.head(3)
print(Toppers_students)
print("\nAttention Needed Students:")
weekStudents = df[(df["Maths"] < 60 ) |
                  (df["English"] < 60 ) |
                  (df["Science"] < 60 )
                ]
attention_students = weekStudents[["Student_Name","Maths","Science","English"]]
print(attention_students)
# Saved to the files 
final_table.to_csv("outputs/final_student_report.csv",index=False)
Toppers_students.to_csv("outputs/top_students.csv", index = False)
attention_students.to_csv("outputs/attention_students.csv",index = False)
