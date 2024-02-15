class Queue():
    def __init__(self):
        self.cards = []

    
    def push(self, card):
        self.append(card)


    def pop(self):
        del self[0]

if __name__ == '__main__':
    pass
