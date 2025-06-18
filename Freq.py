
# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency(my_list): 

	# Creating an empty dictionary 
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1
	return freq;




# Driver function 
if __name__ == "__main__": 
	my_list =['abc', 'abc', 'abc', '123', '123',  'abc',  'abc',  'xyz', 'xyz', 'xyz', 'xyz'] 

	CountFrequency(my_list) 
