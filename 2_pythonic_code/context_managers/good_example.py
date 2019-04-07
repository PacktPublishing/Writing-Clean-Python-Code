class FileHandler:

    def __init__(self, filename, mode):
        print("----")
        print("Loading " + filename)
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening the file")
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print("Closing the file")
        self.open_file.close()


for _ in range(500):
    with FileHandler('temp.txt', 'w') as f:
        f.write('Hello World - From good example')
