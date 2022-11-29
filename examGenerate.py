import os

f = open("myfile.md", "w")
f.write("--- \nlayout: default \ntitle: Exams \nnav_order: 6 \nhas_children: false \n---\n")
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

        file = file.replace(".pdf", "")     #file = name of exam

        f.write("- [" + file + "]")
        f.write("(" + filePath + ")")
        f.write("{:target=\"_blank\"}\n")

        
       # print(file)
    f.write("\n")
    


f.close()

