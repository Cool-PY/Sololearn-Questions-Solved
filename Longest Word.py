txt = input() # For taking Input

txt = txt.split() # For making the text a list

List_of_Lens = [] # For storing lenthes of the words

for i in txt:
    List_of_Lens.append(len(i))
# This is the for loop for storing lenthes of the words of the text

for j in txt:
    if len(j) == max(List_of_Lens):
        print(j)
    else:
        continue

# This is the for loop for checking the lenthes of the words and prints 
#if the lenthes is equal to the max lenthe in List_of_Lens
