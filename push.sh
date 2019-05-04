#!/bin/sh

git clone https://github.com/NeeluMadan/optimization-benchmark.git
cd optimization-benchmark
git remote
git add rosenbrock.png
git commit -m "Travis Commit"
git push 