# read data from file 
def ReadFile():
    dictioniary_works = {}
    files_doc = open("path_file_dataset.txt", "r", encoding = 'utf-8')
    tmp = files_doc.read().split('\n',1)
    number_of_file = tmp[0] # get number of label
    file_doc = tmp[1].split('\n') # get name of label

    index = 0
    for path_list in file_doc: # check each type of document
        path_list = "dataset/train/" + path_list

        doc = open(path_list, "r", encoding = 'utf-8').read()
        arr_doc = doc.split('\n')
        for element_doc in arr_doc: # assign value default dictioniary_works
            arr_txt = element_doc.split(' ')
            for target in range(1,len(arr_txt)-1):
                if arr_txt[target] not in dictioniary_works :
                    dictioniary_works[arr_txt[target]] = 0
        
        for element_doc in arr_doc: # check each document 
            arr_txt = element_doc.split(' ')
            for target in range(1,len(arr_txt)-1):
                dictioniary_works[arr_txt[target]] += 1

        index += 1
        if index == number_of_file: # avoid case path_list = '\0' is fault
            break

    return dictioniary_works

dictioniary_works = {}
dictioniary_works = ReadFile()

path_file = "dataprocessing/dictionary/dictionary.txt"
write_file_result = open(path_file, "w", encoding = 'utf-8')
write_file_result.write(str(len(dictioniary_works)) + "\n")

# print : [numberical order] [name in dictionary] [number of occurrences in the way of writing]
index = 0
for x in dictioniary_works:
    write_file_result.write(str(index) + " " + x + " " + str(dictioniary_works[x]) + "\n")
    index += 1
print("Hoan thanh tao tu dien cho dataset")
