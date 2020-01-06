#!/bin/bash
pip install --user -r requirments.txt || echo "ERROR!"
django-admin startproject mp4_lang || echo "ERROR2!"
