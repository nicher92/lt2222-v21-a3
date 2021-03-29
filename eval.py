
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import random
import sys
import argparse
import numpy as np





def model_open(modelname):
    
    #model_use = modelname.load_state_dict(torch.load(modelname))
    model = torch.load(args.model) #this loads the model
    
    
    model_vocab = []
    for key in model.__dict__.items():
        model_vocab.append(key)
    
    #sometimes [10][1], sometimes [11][1]
    vocabulary2 = model_vocab[10][1]
    print(vocabulary2)
    
    model = model.eval()
    
    return model, vocabulary2
    


#all letters in the file and the vocabulary
def file_open(f, vocabulary2):
    all_letters = []
    
    model_vocab = vocabulary2
    
    with open(f, "r") as q:
        for l in q:
            all_letters += [c for c in l if c in model_vocab]  #testing should not contain anything not in training? "if c in model_vocab"
    

    all_letters = ["<s>", "<s>"] + all_letters + ["<e>", "<e>"]
    
    
    vocabulary = list(set(all_letters + model_vocab))
    
    return all_letters, vocabulary



def g(x, p):
    z = np.zeros(len(p)) ##size of training difference x 4, does this change the order of the letters?
    z[p.index(x)] = 1
    return z



def letters_and_contexts(u, p):
    #talk with asad
    #if there is a letter that is not in the training data then skip that one
    #skip it before creating the instances
    #youll have to print it out
    #
    
    model_vocab = vocabulary2
    
    
    gt = []
    gr = []
    listofvowels = []
    listofwords = []
    listofconsonants = []
    for v in range(len(u) - 4):
        listofwords.append(u[v+2])
        if u[v+2] not in vowels or u[v+2] not in model_vocab: #or u[v+2] not in model_vocab:    #if its not a vowel or if it is a vowel but its not in model_vocab
            listofconsonants.append(u[v+2]) #get all text without vowels
            continue
        
        listofvowels.append(u[v+2])
        
        
        
        h2 = vowels.index(u[v+2])
        gt.append(h2)
        
        ##focus on r, its length is 400, should be 452
        r = np.concatenate([g(x, p) for x in [u[v], u[v+1], u[v+3], u[v+4]]])
        gr.append(r)
    
    
    
    
    correct_vowel = np.array(gt)
    vowel_context = np.array(gr)
    
   

    return vowel_context, correct_vowel, listofwords, listofvowels, listofconsonants


def test(x, y):   
    test_x = torch.Tensor(x)
    test_y_t = torch.LongTensor(y)
    test_y = y

    output = model(test_x.unsqueeze(0))
    
    predictions = pd.Series(output.squeeze(0).argmax(dim=1).numpy())
    
    test_y = pd.Series(test_y)
    predictions.index = test_y.index
    
    
    accuracy = len(test_y[predictions == test_y]) / len(test_y)
    
    return print("accuracy: ", accuracy), predictions

def newtext(words, predictions, listofnonvowels):
    newtext = ""
    
    preds = []
    for item in predictions:
        preds.append(vowels[item])
    
    counter = 0
    counter2 = 0
    for i in range(len(words)):
        if listofwords[i] not in vowels:
            newtext += listofnonvowels[counter]
            counter += 1
        elif listofwords[i] in vowels:
            newtext += preds[counter2] #predicted
           # newtext += listofvowels[counter2]
            counter2 += 1
            
    return newtext

    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    parser.add_argument("model", type=str)
    parser.add_argument("name", type=str)
    
    args = parser.parse_args()
    vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])

    model, vocabulary2 = model_open(args.model)
    
    #file_open opens the file, outputs vocabulary and all letters in the text
    all_letters, vocabulary = file_open(args.text, vocabulary2)
   
    #vowel_contexts outputs np arrays of surrounding letters and the vowel it surrounds
    vowel_context, correct_vowel, listofwords, listofvowels, listofconsonants = letters_and_contexts(all_letters, vocabulary)
    
    #self explanatory
    accuracy, predictions = test(vowel_context, correct_vowel)
    
    #prints the new text
    newtext = newtext(listofwords, predictions, listofconsonants)
                        
    file_name = args.name
    f = open(file_name, 'a+')
    f.write(newtext)
    f.close()
    
    #print(newtext)
    print(accuracy)
    print(vocabulary2)
    
    

