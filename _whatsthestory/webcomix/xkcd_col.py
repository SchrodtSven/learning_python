# 
# xkcd.com_color_rgb.txt
# AUTHOR: Sven Schrodt
# SEE: https://xkcd.com/color/rgb/
# SEE: https://xkcd.com/color/rgb.txt

class XkcdCom:
    pass
    img_uri = 'https://imgs.xkcd.com/comics/'	 
    expl_uri = 'https://explainxkcd.com'
    def col(file:str = 'xkcd.com_color_rgb.txt')->list:
        return []






fh = open('xkcd.com_color_rgb.txt', 'r')
dta = fh.read().split('\n')
cols = {}
split = '#'
for line in dta:
    if line.find(split) == -1:
        break
    
    nme, col = line.split(split)
    cols[nme] = col


print(' '.join(cols.keys))

# https://imgs.xkcd.com/comics/3056
num = 666
print(f'https://m.xkcd.com/{num}/')