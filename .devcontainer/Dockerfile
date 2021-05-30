# Ubuntuの公式コンテナを軸に環境構築
FROM ubuntu

# インフラを整備
RUN apt-get update && \
    apt-get install -y zsh && \
    apt-get install -y time && \
    apt-get install -y tzdata && \
    apt-get install -y tree && \
    apt-get install -y git

# デフォルトシェルをZ shellにする
RUN chsh -s /bin/zsh

# C++, Python3, PyPy3の3つの環境想定
RUN apt-get update && \
    apt-get install -y gcc-9 && \
    apt-get install -y g++-9 && \
    apt-get install -y python3.8 && \
    apt-get install -y python3-pip && \
    apt-get install -y pypy3 && \
    apt-get install -y nodejs && \
    apt-get install -y npm

# 一般的なコマンドで使えるように設定
# e.g. python3.8 main.py => python main.py
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 30 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 30 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30 && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 30

# AtCoderでも使えるPythonライブラリをインストール
RUN pip install numpy==1.18.2 && \
    pip install scipy==1.4.1 && \
    pip install scikit-learn==0.22.2.post1 && \
    pip install numba==0.48.0 && \
    pip install networkx==2.4

# C++でAtCoder Library(ACL)を使えるようにする
RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
ENV CPLUS_INCLUDE_PATH /lib/ac-library

# Pythonでの競技プログラミング用データ構造をインストール
RUN pip install git+https://github.com/hinamimi/ac-library-python && \
    pip install git+https://github.com/hinamimi/python-sortedcontainers

# コンテスト補助アプリケーションをインストール
RUN pip install online-judge-tools==11.3.0
RUN npm install -g atcoder-cli@2.1.1

# atcoder-cliの設定
RUN acc config-dir && \
    acc config default-template python && \
    acc config default-test-dirname-format test

WORKDIR /root/problems
WORKDIR /root/library