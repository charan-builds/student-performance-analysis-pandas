import pandas as pd
df = pd.read_csv("data/student_performance.csv")
print(df)

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
 
df["Total_Marks"] = df["Maths"] + df["Science"] + df["English"]
print(df.head())

#Scoring High Marks in Maths
print("\nHighest Marks Student In Maths")
MaxMaths = df["Maths"].max()
print(df[df["Maths"] == MaxMaths])
# collecting top score persons in a class
print("----Toppers In Class-----")
Top_Marks = 270
Toppers = df[df["Total_Marks"] > Top_Marks]
print(Toppers[["Student_Name","Total_Marks"]])

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
# Total Average 
print("TotalAverage : ",df["Total_Marks"].mean())