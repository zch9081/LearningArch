# Thrift

## 什么是Thrift

**Thrift**是一种接口描述语言和二进制通讯协议，它被用来定义和创建跨语言的服务。它被当作一个远程过程调用（RPC）框架来使用，是由Facebook为“大规模跨语言服务开发”而开发的。它通过一个代码生成引擎联合了一个软件栈，来创建不同程度的、无缝的跨平台高效服务，可以使用C#、C++（基于POSIX兼容系统）、Cappuccino、Cocoa、Delphi、Erlang、Go、Haskell、Java、Node.js、OCaml、Perl、PHP、Python、Ruby和Smalltalk。虽然它以前是由Facebook开发的，它现在是Apache软件基金会的开源项目。

## 什么是RPC

RPC, 远程过程调用直观说法就是A通过网络调用B的过程方法。

- 简单的说，RPC就是从一台机器（客户端）上通过参数传递的方式调用另一台机器（服务器）上的一个函数或方法（可以统称为服务）并得到返回的结果。
- RPC 会隐藏底层的通讯细节（不需要直接处理Socket通讯或Http通讯） RPC 是一个请求响应模型。
- 客户端发起请求，服务器返回响应（类似于Http的工作方式） RPC 在使用形式上像调用本地函数（或方法）一样去调用远程的函数（或方法）。

![img](https://upload-images.jianshu.io/upload_images/2221709-efa474cee2ef482f.png)

## Thrift架构

Thrift包含一套完整的栈来创建客户端和服务端程序。顶层部分是由Thrift定义生成的代码。而服务则由这个文件客户端和处理器代码生成。在生成的代码里会创建不同于内建类型的数据结构，并将其作为结果发送。协议和传输层是运行时库的一部分。有了Thrift，就可以定义一个服务或改变通讯和传输协议，而无需重新编译代码。除了客户端部分之外，Thrift还包括服务器基础设施来集成协议和传输，如阻塞、非阻塞及多线程服务器。栈中作为I/O基础的部分对于不同的语言则有不同的实现。

Thrift支持众多通讯协议：

- TBinaryProtocol – 一种简单的二进制格式，简单，但没有为空间效率而优化。比文本协议处理起来更快，但更难于调试。
- TCompactProtocol – 更紧凑的二进制格式，处理起来通常同样高效。
- TDebugProtocol – 一种人类可读的文本格式，用来协助调试。
- TDenseProtocol – 与TCompactProtocol类似，将传输数据的元信息剥离。
- TJSONProtocol – 使用JSON对数据编码。
- TSimpleJSONProtocol – 一种只写协议，它不能被Thrift解析，因为它使用JSON时丢弃了元数据。适合用脚本语言来解析。

支持的传输协议有：

- TFileTransport – 该传输协议会写文件。
- TFramedTransport – 当使用一个非阻塞服务器时，要求使用这个传输协议。它按帧来发送数据，其中每一帧的开头是长度信息。
- TMemoryTransport – 使用存储器映射输入输出。（Java的实现使用了一个简单的ByteArrayOutputStream。）
- TSocket – 使用阻塞的套接字I/O来传输。
- TZlibTransport – 用zlib执行压缩。用于连接另一个传输协议。

Thrift还提供众多的服务器，包括：

- TNonblockingServer – 一个多线程服务器，它使用非阻塞I/O（Java的实现使用了NIO通道）。TFramedTransport必须跟这个服务器配套使用。
- TSimpleServer – 一个单线程服务器，它使用标准的阻塞I/O。测试时很有用。
- TThreadPoolServer – 一个多线程服务器，它使用标准的阻塞I/O。

![img](https://upload-images.jianshu.io/upload_images/2221709-f86fa699e577fc4f.png)

## .thrift文件

```
# 命名空间，可以不写也可以写多个，按照使用服务端、客户端语言来写即可
namespace go thrift.user
namespace php thrift.user

# 定义一个用户结构
struct UserInfo {
    #序号:字段类型 字段名
    1:i64 id
    2:string username
    3:string password
    4:string email
}

# 定义一个用户服务
service User{
    # 定义一个GetUser方法（接收一个用户id，返回上面定义的用户信息）
    UserInfo GetUser(1:i32 id)
    # 定义一个GetName方法（接收一个用户id，返回用户名称）
    string GetName(1:i32 id)
   
   # 方法定义格式：
   # 返回的类型 方法名(序号:参数类型 参数名 ... )
   # bool Test(1:i32 id, 2:string name, 3:i32 age ... )
}
```

**基本类型**

- bool: A boolean value (true or false)
- byte: An 8-bit signed integer
- i16: A 16-bit signed integer
- i32: A 32-bit signed integer
- i64: A 64-bit signed integer
- double: A 64-bit floating point number
- string: A text string encoded using UTF-8 encoding

**字节类型**

binary: a sequence of unencoded bytes

**集合类型**

- list: 列表，定义时可直接赋值，如:  `list<string> stuNameList=["apple", "pearl"]`
- set: 集合
- map: 映射

**enum枚举类型**

enum定义枚举类型，默认从0开始赋值，也可以指定常量值 ，如：

```
enum level{
    GradeOne,
    GradeTwo=2,
    GradeThree=3
}
```

**struct结构体**

struct结构体定义实体(如java中的class)，字段格式为：`序号:  类型 名称`。如：

```
struct Stu{
    1: required string stuNo,
    2: optional i32 stuAge,
    3: bool isPass
}
```

**service接口**

service定义接口（接口可exetend其它接口），包含方法，参数同struct一样，需要加序号。如：

```
service Hello{
    Stu buildStu(1:string stuName);
}
```

**const常量**

const定义常量，如：`const i32 step=3;`

**namespace包名**

namespace定义包名，放在文件头，结构为：`namespace 语言  包名`。如：

```
namespace java com.dragon.study.thrift
```