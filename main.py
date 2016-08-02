import os


class fastaReader:
    def __init__(self, fileName, start=0, end=1):
        self.fileIn = open(fileName)
        self.fileOut = open(fileName+".out", "w+")
        self.start = start
        self.end = end
        self.count = 0
        self.total = 0

    def copy(self, tar, s, e):
        result = ""
        for i in range(s, e):
            result += tar[i]
        return result

    def cut(self):
        print("Cuting....")
        while 1:
            name = ""
            line = self.fileIn.readline()
            if not line:
                break
            elif(line[0] == '>'):
                # print(line,end="")
                string = ""
                name = line
                # self.fileOut.write(line)
                line = self.fileIn.readline()
                self.total += 1
            while 1:
                if(line != "\n"):
                    string += line
                    line = self.fileIn.readline()
                else:
                    string.replace('\n', '')
                    length = len(string)
                    s = length * self.start
                    e = length * self.end
                    if len(string) <= 8:
                        string += '\n'
                        self.fileOut.write(name)
                        self.fileOut.write(string)
                        self.count += 1
                    elif len(string) > 8:
                        temp = self.copy(string, int(s), int(e))
                        if len(temp) < 8:
                            string += '\n'
                            self.fileOut.write(name)
                            self.fileOut.write(string)
                            break
                        temp += '\n'
                        self.fileOut.write(name)
                        self.fileOut.write(temp)
                        self.count += 1
                    break
        self.fileIn.close()
        self.fileOut.close()
        os.rename(fileName+".out", fileName+"["+str(self.count)+"/"+str(self.total)+"]"+".out")
        print("Over")

fileName = raw_input("fileLocated:")
start = float(input("start:"))
end = float(input("end:"))
# fileName="D:\H3B-1-pnovo-11-value.fasta"
# start=0
# end=0.2
tar = fastaReader(fileName, start, end)
tar.cut()
