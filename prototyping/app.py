import yaml
import markdown

from pprint import pprint
with open('tests.yaml', 'r') as yamlfile:
    test_data = yaml.load(yamlfile.read(), Loader=yaml.Loader)
    pprint(test_data)

print(markdown.markdown('''
# H1
* 1 - *one*
* 2 - **two**
* 3
[Link](http://google.com "Title text")
'''))
