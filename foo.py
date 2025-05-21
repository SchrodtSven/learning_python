from datetime import datetime
import random

rnd = ['Lorem', 'Ipsum', 'dororit', 'foo']

print(rnd[2])

class Secretary:
    user = 'User'
    bot_prologue = 'Bot ->>: '
    user_prologue = f'{user}-->Bot: '
    
    
    
    def __init__(self, file:str = 'chatty.txt'):
        self.file = file
        self.handle = open(self.file, 'a')
        self.writeline(self.prologue())
        
    
    def prologue(self):
        return str(datetime.now())
    
    def readline(self):
        pass
    
    def writeline(self, txt):
        self.handle.write(txt + '\n')
        
    def write_bot(self, txt):
        pl = self.user_prologue + self.bot_prologue
        self.writeline(pl + txt)
        
    def write_user(self, txt):
        self.writeline(self.user_prologue + txt)
        
        
ui = ''        
fh =   Secretary('plauderei.txt')
txt = 'Hallo ich bin Bot, wer bist Du?'
print(txt)
fh.writeline(txt)
while ui != 'quit':
     ui = input('% ')
     print(ui)
     fh.write_user(ui)
     bot = random.randrange(0, len(rnd))
     txt_bot = rnd[bot]
     print(txt_bot)
     fh.write_bot(txt_bot)