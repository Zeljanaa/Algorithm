
import time

def getStartTime():
    start_time = time.time()
    return start_time

def getSecondsTaken(start_time):
    return time.time() - start_time

def sort_by_value(mydict):
    return {k: v for k, v in sorted(mydict.items(), key=lambda item: item[1])}

def Extractor(raw_string, mappings):
    print(f'raw_string: {str(raw_string)}')
    print('*'*30)
    print(f'mappings: {str(mappings)}')
    print('*'*30)
    start_time = getStartTime()
    res_dict = {}
    for m in mappings:
        res_dict[m] = ''
    data_as_dict = {}
    for x in res_dict.keys():
        index = raw_string.find(x)
        if index != -1:
            data_as_dict[x] = index
    sorted_values = sort_by_value(data_as_dict)
    i = 0
    p = 0
    l = None
    d = {}
    for k, v in sorted_values.items():
        start = p
        end = v
        if i > 0:
            d[l] = raw_string[start:end]
        p = v + len(k)
        l = k
        i += 1

    d[l] = raw_string[p:]
    for k, v in d.items():
        res_dict[k] = v
    print(f'res: {str(res_dict)}')
    print(f"text extraction  took {getSecondsTaken(start_time)} seconds")
    print('*'*30)
    print('\n' * 2) 
    return res_dict



res = Extractor('namezeljana24', ['name','age'])