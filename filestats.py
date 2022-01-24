def path():
    path = input("Please insert file path: ")
    return path

def nooflines(path):
    with open(path, 'r') as fp:
        x = len(fp.readlines())
    return x
        
def emptyline(path):
    empty_line_count=0
    with open(path, 'r') as fp:
        for line in fp:
               if line.split() == []:
                empty_line_count += 1 
        return empty_line_count

def find_z(path, str = "z"):
    line_number = 0
    
    list_results = []
    with open(path
             ) as f:
        for line in f:
            line_number += 1
            if str in line:
                list_results.append((line_number, line.rstrip()))
        return len(list_results)
    
def find_and(path, str = "and"):
    line_number = 0
    list_results = []
    with open(path) as f:
        for line in f:
            line_number += 1
            if str in line:
                list_results.append((line_number, line.rstrip()))
        return len(list_results)

        
if __name__ == "__main__":

    path = path()
    print(nooflines(path))
    print(emptyline(path))
    print(find_z(path))
    print(find_and(path))
