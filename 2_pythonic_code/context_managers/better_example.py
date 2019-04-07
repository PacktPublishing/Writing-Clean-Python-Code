from contextlib import contextmanager


@contextmanager
def file_handler(path, mode):
    print("----")
    print("Opening the file")
    resource = open(path, mode)
    yield resource
    print("Closing the file")
    resource.close()


for _ in range(500):
    with file_handler('temp.txt', 'w') as f:
        f.write('Hello World - From better example')
