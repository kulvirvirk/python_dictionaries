
# 1. create and print dictionary that contain fruits
#    keys are nubmer and value are fruit names  
# 2. add values() method to fina a 'mango' in dictionary
# 3. copy the dictionary to new dictionary by using copy() method 

my_fruit_dictionary = {
 1:'mango',
 2:'apple',
 3:'kiwi',
 4:'orange',
 5:'banana'
}
 
print(my_fruit_dictionary)

print(my_fruit_dictionary.values())
print('--------------******--------------\n')

# 2. add values() method to fina a 'mango' in dictionary
print('mango' in my_fruit_dictionary.values())
print('--------------******--------------\n')

# 3. copy the dictionary to new dictionary by using copy() method 
my_fruit_dictionary_copy = my_fruit_dictionary.copy
print(my_fruit_dictionary)
print(my_fruit_dictionary_copy)
print('--------------******--------------\n')