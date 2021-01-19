import tkinter as tk
import pickle

#%%
window = tk.Tk()
window.title("Depression classification GUI")

#%%
def processText(data):
    rows = []
    row = data.lower()
    row = row.replace("#depressed", "")
    row = row.replace("#happy", "")
    rows.append(row)
    #print(row)
    return rows

#%%
def preprocess(Data, vec):
    # Tokenize data
    dataRows = processText(Data)
    token = vec.transform(dataRows)
    
    #exportVectorize(vec)
    
    return token

#%%
def Detect(vec, svc):
    data = preprocess(text_box.get("1.0", "end"), vec)
    res = svc.predict(data)
    print(res)
    if res[0] == 1:
        text_box.delete("1.0", "end")
        text_box.insert("end", "Depressed")
    else:
        text_box.delete("1.0", "end")
        text_box.insert("end", "Not Depressed")

inVec = open("vec.pickle","rb")
vec = pickle.load(inVec)
inVec.close()
insvc = open("svc.pickle", "rb")
svc = pickle.load(insvc)
insvc.close()

text_box = tk.Text()
text_box.pack()

submit = tk.Button(text = "Classify", command=lambda:Detect(vec, svc))
submit.pack()




window.mainloop()