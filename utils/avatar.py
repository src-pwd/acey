from iden import Iden
import hashlib

m = hashlib.md5()
bg = '#EEEEEE'
nicknames = ['boorooneen', 'lehahausmaker', 'methebus', 'glebvernigorov']
# nicknames = ["1", "2", "3", "4"]

for nick in nicknames:
    name = nick
    m.update(name.encode('UTF-8'))
    iden_avatar = Iden(m.hexdigest(), 'circle')
    iden_avatar.setBackgroundColor(bg)
    iden_avatar.save(nick+'.svg')