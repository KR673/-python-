import threading

class Mythread(threading.Thread):
    def run(self):
        for i in range(3):
            print('threadName : {}'.format(self.name))

def main():
    thread = [Mythread() for x in range(3)]
    for i in thread:
        i.start()

if __name__ == '__main__':
    main()