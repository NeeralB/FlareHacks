from flask import Flask, render_template, request

app = Flask(__name__)


#import pandas
#from sklearn import linear_model
#names =  ['Words', 'Toxicity', 'Frequency']
#df = pandas.read_csv("coviddepression.csv")
#X = df[['Toxicity']]
#y = df[['Frequency']]

#regr = linear_model.LinearRegression()
#regr.fit(X,y)

#mentalcheck = regr.predict([[45,56]])
#print(mentalcheck)








    
#for i in range(len(texttosearch)):
#    print(texttosearch[i])



@app.route("/")
def index():
    return render_template("coronaform.html")

@app.route("/corona", methods = ["POST"])
def corona():
    msg=""
    name = request.form.get("q1")
    if name == "YES":
        score = 1
    else:
        score = 0
    name1 = request.form.get("q2")
    if name1 == "YES":
        score = score + 1
    else:
        score = score
    name2 = request.form.get("q3")
    if name2 == "YES":
        score = score + 1
    else:
        score = score
    name3 = request.form.get("q4")
    if name3 == "YES":
        score = score + 1
    else:
        score = score
    name4 = request.form.get("q5")
    if name4 == "YES":
        score = score + 1
    else:
        score = score
    name5 = request.form.get("q6")
    if name5 == "YES":
        score = score + 1
    else:
        score = score
    name6 = request.form.get("q7")
    if name6 == "YES":
        score = score + 1
    else:
        score = score
    name7 = request.form.get("q8")
    if name7 == "YES":
        score = score + 1
    else:
        score = score
    name8 = request.form.get("q9")
    if name8 == "YES":
        score = score + 1
    else:
        score = score
    print(score)

    if score == 0:
        msg = "It doesn't seem like you have any signs and symptoms of coronavirus. You're answers to the quiz indicate that you are in good health, and that you are taking the necessary precautions needed.  1. Make sure to wash your hands for 20 seconds. 2. Make sure to stay 6 feet apart from everyone. 3. Make sure to always wear a mask if you go outside and handgloves to be extra careful. "
    elif score == 1:
        msg = "It doesn't seem like you have any signs and symptoms of coronavirus. You're answers to the quiz indicate that you are in good health, and that you are taking the necessary precautions needed.  1. Make sure to wash your hands for 20 seconds. 2. Make sure to stay 6 feet apart from everyone. 3. Make sure to always wear a mask if you go outside and handgloves to be extra careful. "
    elif score == 2:
        msg = "It doesn't seem like you have any signs and symptoms of coronavirus. You're answers to the quiz indicate that you are in good health, and that you are taking the necessary precautions needed.  1. Make sure to wash your hands for 20 seconds. 2. Make sure to stay 6 feet apart from everyone. 3. Make sure to always wear a mask if you go outside and handgloves to be extra careful. "
    elif score == 3:
        msg = "You show a few symptoms of coronavirus, such as having a mild fever, or nausea. These smyptoms are very well associated with coronavirus, and therefore it is recommended to take a test right away, as it will be much more helpful in evaluating your current health status. It seems like you can new symptoms in a couple of weeks such as sore throat, headache, muscle aches, etc. You may also develop extreme symptoms such as loss of breathing or pressure in chest, or a bluish color for your lips. If you experience any syptoms like this, call 911 right away, as you are in dire medical condition. If an infant is experiencing these symptoms, don't feed him well known medications as this might hurt his health. Make sure to book and reserve you appointment away as the infant is in much need of medical attention."
    elif score == 4:
       msg = "You show a few symptoms of coronavirus, such as having a mild fever, or nausea. These smyptoms are very well associated with coronavirus, and therefore it is recommended to take a test right away, as it will be much more helpful in evaluating your current health status. It seems like you can new symptoms in a couple of weeks such as sore throat, headache, muscle aches, etc. You may also develop extreme symptoms such as loss of breathing or pressure in chest, or a bluish color for your lips. If you experience any syptoms like this, call 911 right away, as you are in dire medical condition.If an infant is experiencing these symptoms, don't feed him well known medications as this might hurt his health. Make sure to book and reserve you appointment away as the infant is in much need of medical attention."
    elif score == 5:
        msg = "You show a few symptoms of coronavirus, such as having a mild fever, or nausea. These smyptoms are very well associated with coronavirus, and therefore it is recommended to take a test right away, as it will be much more helpful in evaluating your current health status. It seems like you can new symptoms in a couple of weeks such as sore throat, headache, muscle aches, etc. You may also develop extreme symptoms such as loss of breathing or pressure in chest, or a bluish color for your lips. If you experience any syptoms like this, call 911 right away, as you are in dire medical condition.If an infant is experiencing these symptoms, don't feed him well known medications as this might hurt his health. Make sure to book and reserve you appointment away as the infant is in much need of medical attention."
    elif score == 6:
        msg = "You show a few symptoms of coronavirus, such as having a mild fever, or nausea. These smyptoms are very well associated with coronavirus, and therefore it is recommended to take a test right away, as it will be much more helpful in evaluating your current health status. It seems like you can new symptoms in a couple of weeks such as sore throat, headache, muscle aches, etc. You may also develop extreme symptoms such as loss of breathing or pressure in chest, or a bluish color for your lips. If you experience any syptoms like this, call 911 right away, as you are in dire medical condition.If an infant is experiencing these symptoms, don't feed him well known medications as this might hurt his health. Make sure to book and reserve you appointment away as the infant is in much need of medical attention."
    elif score == 7:
        msg = "You show a few symptoms of coronavirus, such as having a mild fever, or nausea. These smyptoms are very well associated with coronavirus, and therefore it is recommended to take a test right away, as it will be much more helpful in evaluating your current health status. It seems like you can new symptoms in a couple of weeks such as sore throat, headache, muscle aches, etc. You may also develop extreme symptoms such as loss of breathing or pressure in chest, or a bluish color for your lips. If you experience any syptoms like this, call 911 right away, as you are in dire medical conditionIf an infant is experiencing these symptoms, don't feed him well known medications as this might hurt his health. Make sure to book and reserve you appointment away as the infant is in much need of medical attention."
    else:
        msg = 'You have an extreme case of coronavirus. You show all the dangerous symptoms, and must immediately go to a hospital. You are above 18 years old and it might be much harder for you to recover. Take action immediately.'
        print('msg =', msg)

    return render_template("coronareroute.html", msg = msg)





if __name__ == "__main__":
    app.run(port=5000, debug=True)


