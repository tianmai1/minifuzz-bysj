##### 环境：

python3.8

##### 依赖:

pyqt5等等

```
sudo apt-get update

sudo apt-get install -y build-essential python3-dev automake git flex bison libglib2.0-dev libpixman-1-dev python3-setuptools

sudo apt-get install -y lld-11 llvm-11 llvm-11-dev clang-11 || sudo apt-get install -y lld llvm llvm-dev clang

sudo apt-get install -y gcc-$(gcc --version|head -n1|sed 's/.* //'|sed 's/\..*//')-plugin-dev libstdc++-$(gcc --version|head -n1|sed 's/.* //'|sed 's/\..*//')-dev
```

##### 安装(afl++)：

```
git clone https://github.com/tianmai1/minifuzz-bysj.git
cd minifuzz-bysj/src/tool/fuzz
export LLVM_CONFIG="llvm-config-11"
make distrib
```

##### 使用

```bash
python3 minifuzz-bysj/src/minifuzz.py
```

##### 注意：

此工具只用于本人研究保存，不做他用