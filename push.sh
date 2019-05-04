#!/bin/sh

git clone https://github.com/NeeluMadan/optimization-benchmark.git
cd optimization-benchmark
git remote
git config user.email 'er.neelu.m@gmail.com'
git config user.name NeeluMadan
git add .
git commit -m "Travis Commit"
git push "https://1f0bf4f8a827fd032d6ded4a30d06f5b57ac1f1b@github.com/NeeluMadan/optimization-benchmark.git" master > /dev/null 2>&1