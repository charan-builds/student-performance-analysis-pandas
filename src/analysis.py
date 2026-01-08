import pandas as pd
def load_data(path):
  return  pd.read_csv(path)

def add_features(df):
  df = df.copy()
  df["Total_Marks"] = df[["Maths","Science","English"]].sum(axis = 1)
  total_possible_marks = 300
  df["Percentage"] = (df["Total_Marks"] / total_possible_marks )* 100
  return df 

def performance_label(p):
  if(p >= 85):
    return "Excellence"
  elif(p >= 70):
    return "Good"
  elif(p >= 50):
    return "Average"
  else:
    return "Weak"
  
def sorted_data_total(df):
  sorted_data = df.sort_values(by = "Total_Marks",ascending = False)
  return sorted_data

def topper_students(sorted_data): 
  Topper_students = sorted_data.head(3)
  return Topper_students
def weak_students(sorted_data):
  subject_wise_attention_students = df[((df["Maths"] < 60 ) | (df["English"] < 60) | (df["Science"] < 60))]
  return subject_wise_attention_students

def final_report(Topper_students,sorted_data,subject_wise_attention_students):
  Topper_students.to_csv("outputs/Topper_students.csv",index = False)
  sorted_data.to_csv("outputs/Analysis_data.csv",index = False)
  subject_wise_attention_students.to_csv("outputs/Attention_Students.csv",index = False)
  
  
  

df = load_data("data/student_performance.csv")
df = add_features(df)
df["Performance"] = df["Percentage"].apply(performance_label)
sorted_data = sorted_data_total(df)
Topper_students = topper_students(sorted_data)
Attention_students = weak_students(sorted_data)
final_report(Topper_students,sorted_data,Attention_students) 
