import os

f = open("myfile.md", "w")
f.write("--- \nlayout: default \ntitle: Home \nnav_order: 6 \nhas_children: false \n---\n")
f.write("# Exams")




f.close()

path = "./exams"
dir_list = os.listdir(path)

for dir in dir_list:
    dir = dir.replace(" ", "%20")
    
    print(path+"/"+dir)



