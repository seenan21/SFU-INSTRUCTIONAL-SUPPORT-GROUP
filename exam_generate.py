import os
import re

f = open("Exams.md", "w")
f.write("--- \nlayout: default \ntitle: Exams \nnav_order: 4 \nhas_children: false \n---\n")
f.write("# Exams\n\n")





path = "./exams"
folderList = os.listdir(path)

for folder in folderList:
    #folder = folder.replace(" ", "%20")
    f.write("## " + folder + "\n")      # Prints Course number
    folderPath = path+"/"+folder
    files = os.listdir(folderPath)
    for file in files:
        filePath = folderPath +"/" + file   #filepath = link to file
        filePath = filePath.replace(" ", "%20")

        file_name = file.replace(".pdf", "")     #file = name of exam
        first_word_in_file_name = file_name.split()[0] # Gets first word in file name
        file_name = file.replace(first_word_in_file_name+" ", "") # Removes first word in file name, the CMPT number


        file_name = re.sub(r"\B([A-Z])", r" \1", file_name) # Creates Spacing between words

        f.write("- [" + file_name + "]")
        f.write("(" + filePath + ")")
        f.write("{:target=\"_blank\"}\n")

        
       # print(file)
    f.write("\n")
    


f.close()

