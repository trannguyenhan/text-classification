# read data from file 
def ReadFile():
    dictioniary_works = {}
    files_doc = open("path_file_dataset.txt", "r", encoding = 'utf-8')
    tmp = files_doc.read().split('\n',1)
    number_of_file = tmp[0] # lay so luong nhan
    file_doc = tmp[1].split('\n') # lay ten cua tung nhan

    index = 0
    for path_list in file_doc: # kiem tra tung loai van ban
        path_list = "dataset/train/" + path_list

        doc = open(path_list, "r", encoding = 'utf-8').read()
        arr_doc = doc.split('\n')
        for element_doc in arr_doc: # gan gia tri mac dinh cho dictioniary_works
            arr_txt = element_doc.split(' ')
            for target in range(1,len(arr_txt)-1):
                if arr_txt[target] not in dictioniary_works :
                    dictioniary_works[arr_txt[target]] = 0
        
        for element_doc in arr_doc: # kiem tra tung van ban 
            arr_txt = element_doc.split(' ')
            for target in range(1,len(arr_txt)-1):
                dictioniary_works[arr_txt[target]] += 1

        index += 1
        if index == number_of_file: # tranh truong hop path_list = '\0' se bi loi
            break

    return dictioniary_works

dictioniary_works = {}
dictioniary_works = ReadFile()

path_file = "dataprocessing/dictionary/dictionary.txt"
write_file_result = open(path_file, "w", encoding = 'utf-8')
write_file_result.write(str(len(dictioniary_works)) + "\n")

# in theo trinh tu : [sothutu] [tentutrongtudien] [solanxuathientrongtatcavanban]
index = 0
for x in dictioniary_works:
    write_file_result.write(str(index) + " " + x + " " + str(dictioniary_works[x]) + "\n")
    index += 1
print("Hoan thanh tao tu dien cho dataset")
