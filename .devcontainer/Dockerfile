# Ubuntuの公式コンテナを軸に環境構築
FROM ubuntu

# インタラクティブモードにならないようにする
ENV DEBIAN_FRONTEND=noninteractive
# タイムゾーンを日本に設定
ENV TZ=Asia/Tokyo

# インフラを整備
RUN apt-get update && \
    apt-get install -y zsh time tzdata tree git curl

# デフォルトシェルをZ shellにする
RUN chsh -s /bin/zsh

# C++, Python3, PyPy3の3つの環境想定
RUN apt-get update && \
    apt-get install -y gcc-9 g++-9 python3.8 python3-pip pypy3 nodejs npm

# 一般的なコマンドで使えるように設定
# e.g. python3.8 main.py => python main.py
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 30 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 30 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30 && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 30

# AtCoderでも使えるPythonライブラリをインストール
RUN pip install -U pip && \
    pip install numpy==1.18.2 scipy==1.4.1 scikit-learn==0.22.2.post1 \
    numba==0.48.0 networkx==2.4

# C++でAtCoder Library(ACL)を使えるようにする
RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
ENV CPLUS_INCLUDE_PATH /lib/ac-library

# Pythonでの競技プログラミング用データ構造をインストール
RUN pip install git+https://github.com/hinamimi/ac-library-python && \
    pip install git+https://github.com/hinamimi/python-sortedcontainers

# AHC用のRustのinstall
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH $PATH:/home/root/.cargo/bin

# コンテスト補助アプリケーションをインストール
RUN pip install online-judge-tools==11.5.1
RUN npm install -g atcoder-cli@2.2.0

# atcoder-cliの設定
RUN acc config-dir && \
    acc config default-template python && \
    acc config default-test-dirname-format test

WORKDIR /root/problems
WORKDIR /root/library