# read data from file 
def ReadFile():
    dictionary_works = {}
    files_doc = open("path_file_dataset.txt", "r", encoding = 'utf-8')
    tmp = files_doc.read().split('\n',1)
    number_of_file = tmp[0] # get number of label
    file_doc = tmp[1].split('\n') # get name of label

    index = 0
    for path_list in file_doc: # check each type of document
        dictionary_mini = {}
        path_list = "dataset/train/" + path_list

        doc = open(path_list, "r", encoding = 'utf-8').read()
        arr_doc = doc.split('\n')
        for element_doc in arr_doc: # assign value default dictioniary_works
            arr_txt = element_doc.split(' ')
            for target in range(1,len(arr_txt)-1):
                if arr_txt[target] not in dictionary_mini :
                    dictionary_mini[arr_txt[target]] = 1
                else: 
                    dictionary_mini[arr_txt[target]] += 1
        
        dictionary_sorted = sorted(dictionary_mini.items(), key=lambda item: item[1], reverse=True)

        numberOfIndex = 0
        numberOfType = 0
        while numberOfType < 40:
            foo = dictionary_sorted[numberOfIndex][0]
            numberOfIndex += 1
            if foo not in dictionary_works:
                dictionary_works[foo] = index
                numberOfType += 1

        index += 1
        if index == number_of_file: # avoid case path_list = '\0' is fault
            break

    return dictionary_works

dictionary_works = {}
dictionary_works = ReadFile()

path_file = "dataprocessing/dictionary/dictionary.txt"
write_file_result = open(path_file, "w", encoding = 'utf-8')
write_file_result.write(str(len(dictionary_works)) + "\n")

# print : [numberical order] [name in dictionary] [number of occurrences in the way of writing]
index = 0
for x in dictionary_works:
    write_file_result.write(str(index) + " " + x + " " + str(dictionary_works[x]) + "\n")
    index += 1
print("Hoan thanh tao tu dien cho dataset")

# d = {'one':1,'three':3,'five':5,'two':2,'four':4}
# a = sorted(d.items(), key=lambda x: x[1], reverse=True)    

# print(a)