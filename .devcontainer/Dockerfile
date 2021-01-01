# Ubuntuの公式コンテナを軸に環境構築
FROM ubuntu

# C++, Python3, PyPy3の3つの環境想定
RUN apt-get update && \
    apt-get install -y zsh && \
    apt-get install -y time && \
    apt-get install -y git && \
    apt-get install -y gcc-9 && \
    apt-get install -y g++-9 && \
    apt-get install -y python3.8 && \
    apt-get install -y python3-pip && \
    apt-get install -y pypy3

# デフォルトシェルをZ shellにする
RUN chsh -s /bin/zsh

# 一般的なコマンドで使えるように設定
# e.g. python3.8 main.py => python main.py
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 30 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 30 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30

# online-judge-toolsのinstall
RUN pip install online-judge-tools

# C++でAtCoder Library(ACL)を使えるようにする
RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
ENV CPLUS_INCLUDE_PATH /lib/ac-library

# AtCoderでも使えるPythonライブラリをインストール
RUN pip install numpy==1.18.2 && \
    pip install scipy==1.4.1 && \
    pip install scikit-learn==0.22.2.post1 && \
    pip install numba==0.48.0 && \
    pip install networkx==2.4

# problems以下をworkdirにする
WORKDIR /root/problems