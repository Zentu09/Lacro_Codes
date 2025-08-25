from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    final = ""              # these are the placeholders for string values like the sentences
    head = ""
    PrelimGrade = None      # place holder for numbers like the prelim grade
    warning = ""            # also string place holder

    if request.method == 'POST':
        try:
            Attendance =  int(request.form['absence'])   #the request method will gather data from HTML and will be converted to simple variables
            Exam =  float(request.form['prel_exam'])
            Qz =  float(request.form['quiz'])
            Req =  float(request.form['requirments'])
            Reci =  float(request.form['recitation'])

            att_standing = 100 - (Attendance * 10)    # logic for the attendance
            ClassStanding = (Qz * 0.4) + (Req * 0.3) + (Reci * 0.3)
            PrelimGrade = round((Exam * 0.6) + (att_standing * 0.1) + (ClassStanding * 0.3), 2)  # main logic for prelim and it will round up to 2 decimal places

            if Attendance == 4:
                final = "Frequent absences. Subject failed"    #attendance failure chacker but the prelim grade will still be showed
                

            elif not (0 <= Attendance <= 4):  
                warning = "Attendance Exam must be between 0 and 4."   #will check if the values are right if somehthing happened to html
            elif not (0 <= Exam <= 100):
                warning = "Prelim Exam must be between 0 and 100."
            elif not (0 <= Qz <= 100):
                warning = "Quizzez must be between 0 and 100."
            elif not (0 <= Req <= 100):
                warning = "Requirments must be between 0 and 100."
            elif not (0 <= Reci <= 100):
                warning = "Recitation must be between 0 and 100."

            else:        
                if PrelimGrade <= 74:                                   #these will run if the prelim grade is bellow 75
                    lowreq = (75 - (0.2 * PrelimGrade))/0.8  
                    required = (90 - (0.2 * PrelimGrade))/0.8
                    final = f"You need a grade of {lowreq:.2f} in Midterm and Finals to reach 75% passing grade"
                    head = f"You need a grade of {required:.2f} in Midterm and Finals to reach 90% and get Dean listed"
                    

                elif PrelimGrade >= 90:
                    final = "Outstanding! You are qualified for the Dean's List!"   #Only this will show if the grade is above the 90
                   
    
                elif 75 <= PrelimGrade < 90:                             # This will run up if your grade is between 75 to 89.99
                    required = (90 - (0.2 * PrelimGrade))/0.8            
                    final = f"Good job! You need a grade of {required:.2f} in Midterm and Finals to reach 90% and get Dean listed!"
                    
        except ValueError:
            warning = "There is a letter in your input. Please use mumbers"
        
    return render_template('prel.html', final=final, Prelim=PrelimGrade, head=head, warning=warning)

if __name__ == "__main__":
    app.run(debug=True)

