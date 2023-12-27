import cyaron
from cyaron import IO
from cyaron import Compare
from cyaron import randint

input_io = IO()
input_io.input_write("1111\n")

Compare.program("a.exe", input=input_io, std_program="std.exe")
# 以input_io这个IO对象中的input为stdin输入。
# std.exe的输出为标准输出，以此为标准对拍a.exe的输出。

Compare.program("a.exe", "b.exe", input=input_io, std_program="std.exe")
# 和上面的方法类似，但是你可以以std.exe为标准对拍多个程序输出。

Compare.program("a.exe", "b.exe", "c.exe", input="data.in", std="std.out")
# 当然input也可以简单地是文件，并以std.out这个输出文件的内容来对a.exe, b.exe, c.exe对拍。
# 这里std也可以是IO对象。

while True:

    input_io = IO()
    test_data = IO(file_prefix="heat", data_id=i)
    # input_io.input_writeln(randint(1,100000000))
    input_io.input_writeln(10)
    for i in range(10):
        input_io.input_writeln(randint(1,100000000))
    Compare.program("a.exe", "b.exe", input=input_io, std_program="std.exe")
# 不断地生成测试数据（这里是1到100的随机数），然后放到a.exe，b.exe中，分别以std.exe为标准进行对拍比较
# CYaRon 现在使用多线程比较器，原 stop_on_incorrect 参数现已 deprecated 且无实际作用。
# 并在工作目录下输出a.exe.out, std.out, error_input.in三个文件方便您进一步调试。