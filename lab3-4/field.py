def field(items, *args):
    assert len(args) > 0
    list = []
    if len(args) == 1:
        for i in range(len(items)):
            for j in range(len(args)):
                if args[j] in items[i]:
                    list.append(items[i][args[j]])
    else:
        for i in range(len(items)):
            dictionary = {}
            for j in range(len(args)):
                if items[i].get(args[j]) != None:
                    dictionary[args[j]] = items[i].get(args[j])
                    list.append(dictionary)
    return list
