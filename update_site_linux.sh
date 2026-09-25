#!/bin/bash

@echo off

datestr=$(date '+%Y-%m-%d')
commit_message="chore: Automated update on "$datestr

git add .
git commit -m "$commit_message"
git push