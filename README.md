# LT2222 V21 Assignment 3

Your name: Niclas Hertzberg

## Part 1


a:
a takes an argument f, which should be a file name, opens the file in read mode and for each line in the file and for each letter in each line adds these to mm.

mm is then changed by inserting two <s> strings before the actual content of mm. It is then extended with two <e> symbols at the end.

So it is a list ["<s>", "<s>", *all characters in mm* "<e>", "<e>"]


It then returns a tuple: mm and a list of each unique element in mm (a vocabulary).





g:
g takes two arguments as input, it creates an array of zeros the length of the second argument. If the first argument is anywhere in the array it turns that index into a 1.




b:
b takes as arguments the tuple returned from a.
u is mm and p is the vocabulary.

The loop starts after the first <s> symbols and ends before the two <e> symbols.
For each item in mm, if that item is not a vowel the loop starts over.

If the item is a vowel, it find and appends the vowel index to gt.
For example, "ö" is index 2 in vowels so 2 is appended to gt.

gt is then a list of numbers of vowel indexes that occur in mm.

if a vowel is found, r takes the 2 letters before the vowel and the 2 letters after the vowel but not the vowel.

g(x,p) creates a numpy array the length of the vocabulary with zeros, with a 1 where x is.

So each numpy array which are appended to gr is a matrix of zeroes with four 1's representing the surrounding context letters of each vowel.

gt is also a numpy array

b then returns gt and gr as a numpy array.

gr is the context of the vowel and gt is the vowel.




there are four arguments, two optional (k and r) and two required (m and h)
m is the filename that is parsed by a.
h is the name that torch.save saves the file as
--k is the hiddensize
--r is the number of epochs


the function train is imported with these parameters (X, y, vocab, hiddensize, epochs=100)
corresponding to 
train(gr as an np array, gt as an np array, vocabulary, --k and --r)





## Part 2


model_open 
opens the trained model and gets the vocabulary from the model.
Depending on what model is trained the vocabulary is either model_vocab[10][1] or model_vocab[11][1]

also puts the model in evaluation mode
it then returns the model and the vocabulary


file_open
opens the file inputed and combines the vocabulary from the file and the model used


letters_and_contexts
creates testing instances compatible with the training instances

test
test compares the actual vowel with the predicted model and prints out accuracy

newtext
newtext prints out the text with predicted vowels instead of the actual vowels


eval.py takes three inputs, text, model and the name of the file to write to.




## Part 3


600 epochs is the most accurate at 17.9%. The model seems to get some common words correctly, like "att", "har", "det". The longer words looks to me to usually be as wrong as the less accurate models. Many times the models might get some of the vowels in a word correct, but not all of them.

I have looked at the text and I am not sure that I could see any particular pattern that would differentiate the different types of errors that the models get. Some models just perform slightly better. Maybe one thing could be that sometimes the model will confuse an "é" for an "e" or the other way around, which would make sense since they might occur in similar contexts. There might be a slight tendency for some models to overuse certain specific vowels as well.

For example: this is the last 4 lines of the real text:
och när 10 hela eller delade obliga-
ſenaſte underrättelſen från liſſabon är af den 15
ring, mot billigt pris, ch anſwarar för deras bliſwande
rassmusson generaleu edsvalla d:o plank

800 epochs overuses "y":
äch när 10 huly ellar dulyda yblågå-
ſineſta endurrottilſin frin luſſébin er ef dän 15
ring, måt byllegt pris, ch enſwiryr fär döris blåſwindu
rassmussin gänyrilao edsvella d:a plink

200 epochs overuses "e" more than others:
åch nar 10 hélo iller delidi iblégu-
ſunoſta éndorrettelſen frön leſſaban ar éf dén 15
röng, mat byllegt pris, ch enſwöror far derés blåſwando
ryssmåssön gåneralae idsvylla d:e plönk

In what I saw there was not the same tendency for overusing a certain vowel in larger hidden layer models. So this might have something to do with more epochs instead.



## Bonuses

I did the third bonus question, Dropout.

dropout 50%, accuracy is around 10-12% with standard epochs and hidden layers
dropout 20%, same accuracy as 50% dropout with standard epochs and hidden layers.


## Other notes

In eval.py, I tried to get the vocabulary from the model in model_open but depending on the model the vocabulary can be either model_vocab[10][1] or model_vocab[11][1].