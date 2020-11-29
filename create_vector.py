"""
  Mieu ta du lieu duoi dang vector, moi van ban trong moi loai la mot vector
"""
def convert_vector(document, dictionary):
    dictionary_mini = {}
    arr_text = document.split(' ')

    # create dictionary mini for document current
    for x in range(1,len(arr_text)-1):
        if arr_text[x] not in dictionary_mini:
            dictionary_mini[arr_text[x]] = 1
        else:
            dictionary_mini[arr_text[x]] += 1

    vectorDoc = []
    for x in dictionary:
      if x not in dictionary_mini: 
          dictionary_mini[x] = 0
      vectorDoc_tmp = (dictionary_mini[x])
      vectorDoc.append(vectorDoc_tmp)

    return vectorDoc

def getDictionary():
    path_file = "dataprocessing/dictionary/dictionary.txt"
    file_dictionary = open(path_file, "r", encoding = 'utf-8')
    doc_dictionary = file_dictionary.read()

    tmp = doc_dictionary.split('\n',1)
    number_of_works = tmp[0]
    dictionary_tmp = tmp[1].split('\n')

    dim = []
    dictionary = {}
    for x in dictionary_tmp:
        if x == '': # clear last line
            break
        tmp1 = x.split(" ")
        dictionary[tmp1[1]] = tmp1[0]
        dim.append(tmp1[1])

    return [dictionary, dim]

def calc_BoW(dictionary, dim):
    # open file write result
    path_file = "dataprocessing/vector/BoW.txt"
    write_file_result = open(path_file, "w", encoding = 'utf-8')

    # read file get data
    files_doc = open("path_file_dataset.txt", "r", encoding = 'utf-8')
    tmp = files_doc.read().split('\n',1)
    number_of_file = tmp[0] # get number of label
    file_doc = tmp[1].split('\n') # get name of label
    
    index = 0
    for path_list in file_doc: # check each type of document
        # read data from document
        path_list = "dataset/train/" + path_list
        doc = open(path_list, "r", encoding = 'utf-8').read()
        arr_doc = doc.split('\n')

        run = 0 # variable run limit the number of news 
        for element_doc in arr_doc: # check each document 
            tf = []
            tf = convert_vector(element_doc, dictionary)

            # print file BoW.txt with line, first number is label of document
            # numbers remaining is value of each dimmension of vector
            write_file_result.write(str(index))
            for x in tf:
                write_file_result.write(" " + str(x))
            write_file_result.write("\n")

            if run == 100: # get 11 news in each label
                break
            run += 1

        index += 1 
        if index == number_of_file: # avoid read is invalid characters
            break
        print("Hoan thanh tao vector cho tap du lieu thu ",index, "!")
    write_file_result.close()

dictionary, dim = getDictionary()
calc_BoW(dictionary, dim)