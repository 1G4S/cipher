from src.hashers.text import Text
from src.helpers.memory_buffer import MemoryBuffer

buf = MemoryBuffer()
text = Text('str', 'rot13', 'encrypted')
text2 = Text('str', 'rot47', 'encrypted')
text3 = Text('st1234', 'rot13', 'encrypted')
buf.add_text(text)
buf.add_text(text2)
buf.add_text(text3)

print(buf.__str__())
buf.remove_text("st1234")
print(buf.__str__())
