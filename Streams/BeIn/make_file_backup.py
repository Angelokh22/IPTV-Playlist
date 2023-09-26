
a = 1
b = 3
c = 4




with open("BeIn.m3u", "r")as f:
    lines = f.readlines()


def write_file(file_name, stream_info, stream_link):
    with open(f"{file_name}.m3u", "a")as f:
        f.write(f"{lines[0].strip()}\n\n\n{lines[stream_info].strip()}\n{lines[stream_link].strip()}\n")


for _ in range(7):
    write_file(a, b, c)
    a = a + 1
    b = b + 2
    c = c + 2