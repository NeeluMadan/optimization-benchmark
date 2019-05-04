#!/bin/sh

git checkout master
git add rosenbrock.png
git remote add origin2 https://${GITHUB_TOKEN}@github.com/NeeluMadan/optimization-benchmark.git
git commit -m "update leaderboard"
git push origin2