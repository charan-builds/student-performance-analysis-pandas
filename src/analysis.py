import pandas as pd
df = pd.read_csv("data/student_performance.csv")
print(df)

def label_performance(percentage):
  if(percentage > 85):
    return "Excellent"
  elif(percentage > 70):
    return "Good"
  elif(percentage > 50):
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
print(marks_df.head())
 
# df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]
# print(df.head())


#Scoring High Marks in Maths
print("\nHighest Marks Student In Maths")
MaxMaths = df["Maths"].max()
print(df[df["Maths"] == MaxMaths])
# collecting top score persons in a class
# print("----Toppers In Class-----")
# Top_Marks = 270
# Toppers = df[df["Total_Marks"] > Top_Marks]
# print(Toppers[["Student_Name","Total_Marks"]])

#Weak Students in subject_wise
print("WeakStudents")
weakStudents = df[(df["Maths"] < 60 ) |
                  (df["English"] < 60 ) |
                  (df["Science"] < 60 )
                ]
print(weakStudents[["Student_Name","Maths","Science","English"]])


# class Average Subject wise
print("\nMaths Average : " ,df["Maths"].mean())
print("\nEnglish Average : ",df["English"].mean())
print("\nScience Average : ",df["Science"].mean())
print()
# # Total Average 
# print("TotalAverage : ",df["Total_Marks"].mean())

# Method to calculate column wise marks
print(df[["English","Maths","Science"]].mean(axis = 0))
df["Total_Marks"] = (df[["English","Maths","Science"]].sum(axis = 1))
print(df.head())


# subject_totals = df[["Maths", "Science", "English"]].sum(axis=0).reset_index()
# subject_totals.columns = ["Subject", "Total_Marks"]
# print(subject_totals)

# calculate Percentage 
Total_Possible_Marks = 300
df["Percentage"] = (df["Total_Marks"] / 300)* 100
print(df.head())

df["Label"] = df["Percentage"].apply(label_performance)
print(df.head())

# Ranking Students
df_sorted = df.sort_values(by = "Total_Marks" , ascending = False )
print(df_sorted.head(3))

#week_students 
week_students = df[df["Label"] == "Weak"]
print(week_students[["Student_Name","Maths","English","Science","Total_Marks"]])
final_table = df_sorted[["Student_Name","Maths","English","Science","Total_Marks","Percentage","Label"]]
print(final_table)
