punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(x):
    for char in punctuation_chars:
        x = x.replace(char, "")
    return x

def get_pos(strsentence):
    strsentence = strip_punctuation(strsentence)
    strsentence = strsentence.lower()
    spliting = strsentence.split()
    count = 0
    for word in spliting:
        if word in positive_words:
            count += 1
    return count

def get_neg(strsentence):
    strsentence = strip_punctuation(strsentence)
    strsentence = strsentence.lower()
    spliting = strsentence.split()
    count = 0
    for word in spliting:
        if word in negative_words:
            count += 1
    return count

file_open = open("project_twitter_data.csv","r")
resultingdatafile = open("resulting_data.csv","w")
read_file = file_open.readlines()
print(read_file)

def writedataonfile(resultingdatafile):
    resultingdatafile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingdatafile.write("\n")
    
    for eachline in read_file[1:]:
        eachline = eachline.strip().split(',')
        resultingdatafile.write("{}, {}, {}, {}, {}".format(eachline[1], eachline[2], get_pos(eachline[0]), get_neg(eachline[0]), (get_pos(eachline[0])-get_neg(eachline[0]))))    
        resultingdatafile.write("\n")
                           
writedataonfile(resultingdatafile)
file_open.close()
resultingdatafile.close()