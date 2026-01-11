import pandas as pd
def check_required_columns(df,required_columns):
  missing = []
  for i in required_columns:
    if i not in df.columns:
      missing.append(i)
  if(len(missing)>0):
    raise ValueError(f"Required Columns Missing : {missing}")
    
def validate_marks(df):
   for subject in ["Maths","Science","English"]:
     if not df[subject].between(0,100).all():
       raise ValueError("Invalid Range of Marks")
def check_missing_values(df):
  return df.isnull().sum()
def load_data(path):
  df = pd.read_csv(path)
  required_columns = ["Student_Name","Maths","Science","English"]
  check_required_columns(df,required_columns)
  return df
 

def add_features(df):
  df = df.copy()
  df["Total_Marks"] = df["Maths"] + df["English"] + df["Science"]
  total_possible_marks = 300
  df["Percentage"] = (df["Total_Marks"] / total_possible_marks )* 100
  return df 

def performance_label(p):
  if(p >= 85):
    return "Excellent"
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
  topper_students = sorted_data.head(3)
  return topper_students
def weak_students(df):
  attention_students = df[((df["Maths"] < 60 ) | (df["English"] < 60) | (df["Science"] < 60))]
  return attention_students

def final_report(topper_students,full_data,attention_students):
  topper_students.to_csv("outputs/top_students.csv",index = False)
  full_data.to_csv("outputs/final_students_report.csv",index = False)
  attention_students.to_csv("outputs/attention_Students.csv",index = False)
  
if __name__ =="__main__":
  try: 
    df = load_data("data/student_performance.csv")
    validate_marks(df)
    check_missing_values(df)
    df = add_features(df)
    df["Performance"] = df["Percentage"].apply(performance_label)
    sorted_data = sorted_data_total(df)
    topper_student = topper_students(sorted_data)
    attention_students = weak_students(sorted_data)
    final_report(topper_student,sorted_data,attention_students) 
  except Exception as e :
    raise ValueError("Pipe Line is Disturbed",e)