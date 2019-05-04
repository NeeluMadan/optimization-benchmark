#!/bin/sh

git checkout master
git add rosenbrock.png
git remote add origin2 https://1f0bf4f8a827fd032d6ded4a30d06f5b57ac1f1b@github.com/NiMlr/optimization-benchmark.git
git commit -m "update leaderboard"
git push origin2