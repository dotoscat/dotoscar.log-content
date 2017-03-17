#!/usr/bin/env python
'''
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Lang: en
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.

'''
import datetime
import os.path
from pelicanconf import DEFAULT_LANG

metadata = {
    'Title': None,
    'Date': None,
    'Modified': None,
    'Category': None,
    'Tags': None,
    'Slug': None,
    'Authors': None,
    'Lang': None,
    'Summary': None
}

def get_today_value():
    now = datetime.date.today()
    return now.isoformat()

print("Let's create content for your blog")
for key in metadata:
    prompt = ' '
    if key == "Date":
        value = input(key + " (yyyy-mm-dd)[now time]: ")
        if len(value) == 0:
            value = get_today_value()
        continue
    elif key == "Slug":
        prompt = ', common name for translations: '
    value = input(key + prompt)
    metadata[key] = value if len(value) > 0 else None

if metadata['Title'] is None:
    print('Give a title at least')
    exit(1)

title = metadata['Title']
title_hyphen = title.replace(' ','-')
lang = '-'+metadata['Lang'] if metadata['Lang'] is not None else '-'+DEFAULT_LANG
slug = metadata['Slug'] if metadata['Slug'] is not None else title_hyphen
filename = title_hyphen + lang + ".md"

print('where do I put this file (relative path or return for \'.\')?')
folder = input('> ')
folder = os.path.join(os.path.abspath('.'), folder)
folder = os.path.normpath(folder)
if not os.path.isdir(folder):
    print("'{}' is not a valid folder".format(folder))
    exit(2)
path = os.path.join(folder, filename)
if os.path.isfile(path):
    print('{} already exists, do you want to replace it?'.format(filename))
    answer = input('default \'No\' (No, Yes)> ')
    answer = answer.lower()
    if len(answer) == 0 or answer != 'yes':
        exit(3)

content = open(path, 'w')
for key in metadata:
    if metadata[key] is None: continue
    content.write('{}: {}\n'.format(key, metadata[key]))

content.write('\nWrite here your awesome content\n');
content.close()
print(path)
