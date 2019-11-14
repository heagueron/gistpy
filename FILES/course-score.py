
# Course Score function
def studentScore(fileHandle):
    
    # Open the file, read mode
    my_file = open(fileHandle)

    # Get the file rows via comprehension list
    rows = [ line.split(' ') for line in my_file.read().splitlines() ]
    my_file.close()

    for student_row in rows:
        score_score = (
            int(student_row[1])*0.1 + 
            int(student_row[2])*0.2 + 
            int(student_row[3])*0.15 + 
            int(student_row[4])*0.15 + 
            int(student_row[5])*0.4 )
        # student_row[0] holds the student's name    
        print(f"{student_row[0]} has a cumulative score of {score_score:.2f}")  

# Main program start
filename = 'studentdata.txt'
studentScore(filename)

