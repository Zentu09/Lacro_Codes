from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():

    warning = ""
    last = []    

    if request.method == 'POST':

        num = int(request.form['given'])
        try: 
            for multiplication in range(1, 11): # this serves as function for the increasing multiplyer up to 10
                result = num * multiplication  # the main logic for computing
                last.append(f"{num} X {multiplication} = {result}") 

        except ValueError:
            warning = "That is not a number please try again"        

    return render_template('McPb.html', last=last, warning=warning)

if __name__ == "__main__":
    app.run(debug=True)