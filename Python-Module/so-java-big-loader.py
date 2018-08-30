import os
from gensim.models import FastText

EXP_HOME = "F:/MyWorks/Thesis Works/Crowdsource_Knowledge_Base/DeepGenQR/experiment"
# EXP_HOME = "C:/My MSc/ThesisWorks/BigData_Code_Search/DeepGenQR/experiment"
model_file = EXP_HOME + '/pymodel/so-java-big'
model = FastText.load(model_file)

# print(len(model.wv))

# quit()

word_file = EXP_HOME + '/w2vec-data/words.txt'
vec_file = EXP_HOME + '/w2vec-data/so-vector.txt'
vec_lines = list()
words = open(word_file, 'r')
for word in words:
    try:
        if model.wv.__contains__(word.strip()):
            vector = model.wv[word.strip()]
            line = word.strip() + " " + ' '.join(str(x) for x in vector)
            vec_lines.append(line)
    except IOError:
        print("Could not found " + word)
        pass

output_file = open(vec_file, 'w')
for content in vec_lines:
    output_file.write("%s\n" % content)
output_file.close()
