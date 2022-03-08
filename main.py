#以 utf-8 的编码格式打开指定文件

f = open("log.txt",encoding = "utf-8")

#输出读取到的数据

file = f.readlines(1000)
keyword = "start"
for line in file:
    print(len(line),line)
    start_check_index = line.find(keyword)
    if start_check_index != -1:
        rel_time = line[:start_check_index]
        print(rel_time)
print(file)

#关闭文件

f.close()