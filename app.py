import sys 

def read_file(file_name): 
	try: 
		with open(file_name, 'r') as f: 
		    data = f.read()
		return data 
	
	except IOError: 
		print("Error eading input file: ", file_name) 
		sys.exit() 
        
def list_handler(text):
    punctuation = ",."
    data = []
    for i in text:  
        if i in punctuation:  
            data = text.replace(i, "").split() 
    return data

def comparison(file_one, file_two):
    text_one = set(list_handler(read_file(file_one)))
    text_two = set(list_handler(read_file(file_two)))

    intersection = len(set(text_one).intersection(text_two))
    union = len(set(text_one)) + len(set(text_two)) - intersection

    return intersection / union

print(comparison("sampleOne.txt","sampleOne.txt"))