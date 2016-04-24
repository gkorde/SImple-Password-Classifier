from collections import defaultdict, Counter
import math
import hashlib
    
#Problem 1 

freq_dict=defaultdict(int)
character_counter = Counter()
character_unique_counter = Counter()
with open('pwds300', 'r') as pwd_file:
    for line in pwd_file:
        if len(line.strip("\n")):
            freq_dict[line.strip("\n")] += 1


output1 = open("cse664spring16hw3Question1.txt", "w")
freq_list = sorted(freq_dict, key=freq_dict.get, reverse=True)

totalchar = 0.0
total_unique_char=0.0
for pwd in freq_list:
    for ch in pwd:
        character_counter[ch] += freq_dict[pwd]
        character_unique_counter[ch] += 1 
    totalchar += len(pwd)*freq_dict[pwd]
    total_unique_char += len(pwd)
    output1.write(str(freq_dict[pwd]) + "   " + pwd+"\n")
output1.close() 

# print totalchar
# print total_unique_char

#Problem 2 and 3 will use the following function

def entropy(total,file_handle,char_dict):
    entropy_dict = {}
    for pwd in freq_list:
        entropy = 0.0
        for ch in set(pwd):
            char_prob = char_dict[ch]/total
            entropy += char_prob*(math.log(char_prob)/math.log(2))
        entropy_dict[pwd] = -entropy

    entropy_list = sorted(entropy_dict, key=entropy_dict.get, reverse=True)
    for pwd in entropy_list:
      file_handle.write(str(entropy_dict[pwd]) + "  " + pwd +"\n" )
    file_handle.close() 


def problem2():
    output2 = open("cse664spring16hw3Question2.txt", "w") 
    entropy(totalchar,output2,character_counter)

def problem3():
    output3 = open("cse664spring16hw3Question3.txt", "w") 
    entropy(total_unique_char,output3,character_unique_counter)

#Problem 4

def problem4():
    output4 = open("cse664spring16hw3Question4.txt", "w")
    hash_dict = {} 
    hash_list = ['ba931c15ec0163c4bb339f41571694ce',
                 'c9cd905fc459e5550b8c3b01d4346c25',
                 'e9269d9e52a692f52caece9d0e7cdae1',
                 '660719b4a7591769583a7c8d20c6dfa4']

    for word in freq_list:
      current_hash = hashlib.md5(word).hexdigest()
      if current_hash in hash_list:
        output4.write(current_hash +"\t" + word + "\n")
    output4.close()

problem2()
problem3()
problem4()