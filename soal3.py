def kemunculanKata(inputList, queryList):
    hasil = [inputList.count(query) for query in queryList]
    return hasil

inputList = ['xc', 'dz', 'bbb', 'dz']
queryList = ['bbb', 'ac', 'dz']
output = kemunculanKata(inputList, queryList)
print(output)
