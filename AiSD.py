import re
with open("text2.txt", "r") as file:
        s = re.sub(r'\s+', ' ', file.read().decode('UTF-8'))

print("Предложения, не имеющие запятых:")        
print(" ")

flag = 0
for s in re.split(r'(?<=[.!?…\n\r\t]) ', s):
        element = re.split(",", s)
        if len(element) < 2:
                flag += 1
                print(s)
        
if flag == 0:
        print ("Таких предложений в тексте нет")

                       
        
        
    

