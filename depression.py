from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("depression.html")

@app.route("/depression", methods = ["POST"])
def depression():
    msg = ""
    texttosearch = request.form.get("gamename")
    
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

#Running through a list

    import string
    import matplotlib.pyplot as plt
    from scipy import stats
    import time
    counter = 0
    sadwords = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress", "depressed", "unhealthy", "life", "elephant", "belligerent", "barbed", "cant", "contradictory", "evil", "help", "negativity", "negative", "uhh", "slow", "collapse", "shame", "ashamed", "shamed", "personality", "deprived", "despair", "different", "will", "extrem", "extremist", "terror", "ouch", "foolish", "fear","conquerable", "guilt", "heartbroken", "worthless", "haunt", "give", "unfortunate", "zapped", "zombie", "difidet" "apathetic", "zealot", "wrongful", "wrongly", "wrong", "wripped", "wrinkles", "wrinkly", "zealot", "zapped", "vindictive", "diffident", "vindicitious", "revenge","revengeful", "hacker", "spy", "spying", "nle","died", "loved", "never","apathy","emp","rip","rest","peace","freedom", "mind", "crime", "jail", "parkinsons", "crypto", "bit", "no", "tribe", "freak", "frightened", "dark", "night", "will", "contemplate", "think", "give", "up", "down", "turn", "vindictive", "revenge", "messy", "mean", "pissed", "suicide", "ouch"]

    #def main():
    

    texttosearch = texttosearch.lower()
    



    newlist = texttosearch.split()
    mylist = []

    #if len(sadwords) > len(newlist):
    for i in range(len(newlist)):
        for x in range(len(sadwords)):
            if newlist[i] == sadwords[x]:
                print("Word found", newlist[i])
                counter = counter + 1
                #mylist = mylist.append[newlist[i]]

                

    if counter > 0:
        slope = (((len(texttosearch)/(counter))))
        print(slope)
        if slope < 40 and slope > 0:
            msg ="You are in danger! Lots of depression symptoms have been found. Medical care is needed immediately. Call the hotline now! Make sure to remain positive at all times! It is important to not think too much about your thoughts and too be prompt and curve whatever side thoughts you may be feeling. Make sure to have the hotline number handy in case, and have a friend or family member near you at all times in case you by any chance start to feel extremely depressed and are at the point of committing suicides"
        elif slope <80 and slope >40:
            msg = "A few depression symptoms have been found in word choice and similarity of typing speed. You are in mild danger, and must concentrate on the postitivity of the world and life. Medical Care is recommended but not required. It is important to not think too much about your thoughts and too be prompt and curve whatever side thoughts you may be feeling. Make sure to have the hotline number handy in case, and have a friend or family member near you at all times in case you by any chance start to feel extremely depressed and are at the point of committing suicides"
        elif slope <130 and slope >80:
            msg = "A few depression symptoms have been found for your word choices and your typing speed patterns. You are in mild danger, and must concentrate on the postitivity of the world and life. Medical Care is recommended but not required. It is important to not think too much about your thoughts and too be prompt and curve whatever side thoughts you may be feeling. Make sure to have the hotline number handy in case, and have a friend or family member near you at all times in case you by any chance start to feel extremely depressed and are at the point of committing suicides"
        else:  
            msg = "You don't have depression"


    # Finding frequency
    def count_substring(nStr, pattern, data_dict):
        count = 0
        start = 0
        while True:
            a = nStr.find(pattern,start)  # find() returns -1 if the word is not found,
            if a == -1:
                break
            else:
                count += 1
                start = a + 1
        data_dict[pattern] = count
        return data_dict
    def main():
        _str = texttosearch
        my_list = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress", "depressed", "unhealthy", "life", "elephant", "belligerent", "barbed", "cant", "contradictory", "evil", "help", "negativity", "negative", "uhh", "slow", "collapse", "shame", "ashamed", "shamed", "personality", "deprived", "despair", "different", "will", "extrem", "extremist", "terror", "ouch", "foolish", "fear","conquerable", "guilt", "heartbroken", "worthless", "haunt"]
        counts = {}
        for i in my_list:
            counts = count_substring(_str, i, counts)
        print(counts)
        barx1 = list(counts.keys())
        barx2 = list(counts.values())
        plt.xlabel('Most used negative words')
        plt.ylabel('Frequency of the word in your text')
        plt.title("Bar graph for analyzing frequency of negative words written")

        plt.bar(barx1, barx2)

        plt.xticks(rotation=45)
        #plt.show()
    main()

    ## BAR GRAPH 2  Words to frequency
    ## Bar Graph1
### YOUR CODE GOES BELOW
    from matplotlib import pyplot as plt
    import matplotlib.pyplot as plt
    barx = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress"]
    bary = [99, 34, 4, 34, 23, 46, 67, 78, 45, 34, 23]



    plt.xlabel('Programming Languages')
    plt.ylabel('Toxicity of Word')
    plt.title('Bar graph for analyzing depression.')
    plt.bar(barx, bary)

    plt.xticks(rotation=45)
    #plt.show()


    

    return render_template("depression.reroute.html", name=texttosearch, name1 = msg) 



if __name__ == "__main__":
    app.run(port=5000, debug=True)


## TEST

## Graph2
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

import time
class time_checker():
    def check_speed(self, word, speed):
        average_speed = word/speed
        return average_speed #returns chars per second
#def main():
print("Tell me some text to first analyze your typing ")
time_check_object = time_checker()
int_time = time.time()
word = len(input())
fin_time = time.time()
tot_time = fin_time - int_time
time_taken = time_check_object.check_speed(word,tot_time)
print(time_taken)
    # DRAwING THE MAP
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6,56]
#y = [time_taken,time_taken*2,time_taken*3,time_taken*4,time_taken*5,time_taken*6,time_taken*7,time_taken*8,time_taken*9,time_taken*10,time_taken*11,time_taken*12,time_taken*13, time_taken*14]

#plt.xlabel('Toxicity of each word that was previously typed?')
#plt.ylabel('Typing speed for each word')
#plt.title('Toxicity of Word just typed with typing speed')
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, time_taken, time_taken*0.25)
#t1 = np.random.permutation(t0)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

def count_substring(nStr, pattern, data_dict):
        count = 0
        start = 0
        while True:
            a = nStr.find(pattern,start)  # find() returns -1 if the word is not found,
            if a == -1:
                break
            else:
                count += 1
                start = a + 1
        data_dict[pattern] = count
        return data_dict
def mains():
    _str = "I am mental and sad and angry. I am so negative and just trash. I am on the verge of being unhealthy and am facing extreme stress. Im starting to collapse and die."
    my_list = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress", "depressed", "unhealthy", "life", "elephant", "belligerent", "barbed", "cant", "contradictory", "evil", "help", "negativity", "negative", "uhh", "slow", "collapse", "shame", "ashamed", "shamed", "personality", "deprived", "despair", "different", "will", "extrem", "extremist", "terror", "ouch", "foolish", "fear","conquerable", "guilt", "heartbroken", "worthless", "haunt"]
    counts = {}
    for i in my_list:
        counts = count_substring(_str, i, counts)
    #print(counts)
    barx1 = list(counts.keys())
    barx2 = list(counts.values())
    plt.xlabel('Most used negative words')
    plt.ylabel('Frequency of the word in your text')
    plt.title("Bar graph for analyzing frequency of negative words written")
    plt.bar(barx1, barx2)

    plt.xticks(rotation=45)
    plt.show()
mains()


##GRAPH#

barx = ["depression", "mental", "pain", "trash", "abysmal", "angry", "negative", "sad", "stressed", "die", "stress"]
bary = [99, 34, 4, 34, 23, 46, 67, 78, 45, 34, 23]



plt.xlabel('Programming Languages')
plt.ylabel('Toxicity of Word')
plt.title('Bar graph for analyzing depression.')
plt.bar(barx, bary)

plt.xticks(rotation=45)
plt.show()


