import uuid


def generateCode(num):
    list = []
    for i in range(num):
        list.append(uuid.uuid1())
    return list


if __name__ == "__main__":
    codes = generateCode(20000)
    code_file = open('gencodes.txt', 'w')
    for code in codes:
        code_file.write(str(code) + "\n")
    code_file.close()
