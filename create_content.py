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
for tag in metadata:
    if tag == "Date":
        value = input(tag + " (yyyy-mm-dd): ")
        if len(value) == 0:
            value = get_today_value()
    else:
        value = input(tag + ' ')
    metadata[tag] = value if len(value) > 0 else None

if metadata['Title'] is None:
    print('Give a title at least')
    exit(1)

title = metadata['Title']
lang = '_'+metadata['Lang'] if metadata['Lang'] is not None else ''
filename = title.replace(' ','_') + lang + ".md"

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
