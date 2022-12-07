from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def getSize(self) -> int:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

class File(ABC):

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def getSize(self) -> int:
        return self.size

    def getName(self) -> str:
        return self.name

class Directory(Item):

    def __init__(self, name: str, parent: int) -> None:
        self.items = []
        self.name = name
        self.parent = parent

    def getSize(self) -> int:
        size = 0

        for item in self.items:
            size += item.getSize()

        return size

    def getName(self) -> str:
        return self.name

    def addItem(self, item: Item) -> None:
        self.items.append(item)

    def getParent(self) -> Item:
        return self.parent

    def findDirectory(self, directoryName: str) -> Item:
        for item in self.items:
            if item.getName() == directoryName:
                return item
        return None

    def printDirectoryTree(self, indents=0) -> None:
        indentation = "\t" * indents
        for item in self.items:
            if isinstance(item, Directory):
                print(f"{indentation}- {item.getName()} (dir)")
                item.printDirectoryTree(indents + 1)
            if isinstance(item, File):
                print(f"{indentation}- {item.getName()} (file, size={item.getSize()})")



with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    rootDirectory = Directory("/", None)
    currentDirectory = rootDirectory

    directories = [rootDirectory]

    for line in lines:

        if line[0] == "$":
            command = line[2:4]
            if command == "ls":
                continue
            if command == "cd":
                directoryName = line[5:]
                if directoryName == "/":
                    currentDirectory = rootDirectory
                elif directoryName == "..":
                    currentDirectory = currentDirectory.getParent()
                else:
                    currentDirectory = currentDirectory.findDirectory(directoryName)
        else:
            if line[:3] == "dir":
                directoryName = line[4:]
                subDirectory = Directory(directoryName, currentDirectory)
                currentDirectory.addItem(subDirectory)
                directories.append(subDirectory)
            else:
                fileSize, fileName = line.split()
                fileSize = int(fileSize)
                subFile = File(fileName, fileSize)
                currentDirectory.addItem(subFile)

    sumOfAllDirectoriesSmallerThan100000 = 0
    for directory in directories:
        directorySize = directory.getSize()
        if directorySize <= 100_000:
            sumOfAllDirectoriesSmallerThan100000 += directorySize
    print(f"1) {sumOfAllDirectoriesSmallerThan100000}")

    # This is the code for part 2 (which is failing)
    minimumSpaceThatNeedsToBeCleared = 30_000_000 - (70_000_000 - rootDirectory.getSize())
    minSize = float('inf')
    minDirectory = None
    for directory in directories:
        directorySize = directory.getSize()
        # print(f"checking {directory.getName()} of size {directorySize}")
        if directorySize >= minimumSpaceThatNeedsToBeCleared and directorySize < minSize:
            minSize = directorySize
            minDirectory = directory
            # print("updated")
    print(f"2) {minDirectory.getName()}")

    rootDirectory.printDirectoryTree()

