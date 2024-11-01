from hashers.rot13 import ROT13
from hashers.rot47 import ROT47
from helpers.memory_buffer import MemoryBuffer
from managers.manager import Manager
from menus.menu import Menu

memory_buffer = MemoryBuffer()
rot13 = ROT13()
rot47 = ROT47()
menu = Menu({})
manager = Manager(memory_buffer=memory_buffer, rot13=rot13, rot47=rot47, menu=menu)
manager.main_loop()
