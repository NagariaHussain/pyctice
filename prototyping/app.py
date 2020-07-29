import yaml
import markdown

from pprint import pprint
with open('tests.yaml', 'r') as yamlfile:
    test_data = yaml.load(yamlfile.read(), Loader=yaml.Loader)
    # pprint(test_data)

print(markdown.markdown('''
# H1
* 1 - *one*
* 2 - **two**
* 3 - three
[Link](http://google.com "Title text")
```:::python
import os
print("Hello world!")
```
''', extensions=['codehilite']))

# SYNTAX HIGHLIGHTING
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import ImageFormatter

# code = '''
# from pathlib import Path
# print("Hello World")

# '''
# # print(highlight(code, PythonLexer(), HtmlFormatter()))

# print(ImageFormatter())

# with open('hello.png', 'wb') as imgFile:
#     highlight(code, PythonLexer(), ImageFormatter(), outfile=imgFile)