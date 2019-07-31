#!/usr/bin/env bash
tag=${1:-cp36}
rm ~/.local/bin/nichijou-cpu
rm ~/.local/bin/nichijou-jupyter-cpu
rm ~/.local/bin/nichijou-gpu
rm ~/.local/bin/nichijou-jupyter-gpu
ln -s $(realpath ${tag}_cpu/nichijou) ~/.local/bin/nichijou-cpu
ln -s $(realpath ${tag}_cpu/nichijou-jupyter) ~/.local/bin/nichijou-jupyter-cpu
ln -s $(realpath ${tag}_gpu/nichijou) ~/.local/bin/nichijou-gpu
ln -s $(realpath ${tag}_gpu/nichijou-jupyter) ~/.local/bin/nichijou-jupyter-gpu
chmod +x ~/.local/bin/nichijou-cpu
chmod +x ~/.local/bin/nichijou-jupyter-cpu
chmod +x ~/.local/bin/nichijou-gpu
chmod +x ~/.local/bin/nichijou-jupyter-gpu
