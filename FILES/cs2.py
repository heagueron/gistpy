# Course Score function
def studentScore(fileHandle):

    # Get the file rows via comprehension list
    rows = [ line.split(' ') for line in fileHandle.read().splitlines() ]

    for student_row in rows:
        score_score = (
            int(student_row[1])*0.1 + 
            int(student_row[2])*0.2 + 
            int(student_row[3])*0.15 + 
            int(student_row[4])*0.15 + 
            int(student_row[5])*0.4 )
    
        print(f"{student_row[0]} has a cumulative score of {score_score:.2f}")  

# Main program start
with open('studentdata.txt', newline='') as scores:
    studentScore(scores)
    