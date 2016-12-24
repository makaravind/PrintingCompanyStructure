from collections import defaultdict
SPACE = '  '

def findRoot(employers):
    #finding node with no in-edges i.e not present in RHS
    root = list(employers.keys())[0]

    for key, values in employers.items():
        for child in values:
            if child == root:
                root = key

    return root


def findStruturePath(employers, depth, associate):

    current = employers[associate]
    if current == []:
        print(SPACE*depth, '-', associate)
    else:
        print(SPACE * depth, '-', associate)
        for value in current:
            findStruturePath(employers, depth+1, value)



if __name__ == "__main__":
    employers = defaultdict(list)

    # input graph
    employers['aa'] = ['bb', 'cc', 'ee']
    employers['cc'] = ['dd']

    print(employers)

    root = findRoot(employers)
    depth = 0
    struture = findStruturePath(employers, depth, root)