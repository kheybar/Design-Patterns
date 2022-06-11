class History:
    state = []

    def push(self, content):
        return self.state.append(content)

    def pop(self):
        try: 
            self.state.pop()
            return self.state[-1]
        except IndexError: raise ValueError('history is clean!')


class Editor(History):
    content = None

    def __call__(self, content):
        self.content = content

    def create_state(self):
        return self.push(self.content)

    def restore(self):
        self.content = self.pop()
        return self.content


a = Editor()

a('first')
a.create_state()

a('second')
a.create_state()

a('third')
a.create_state()


a.restore()
a.restore()
print(a.restore())
