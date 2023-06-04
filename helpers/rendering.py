from jinja2 import Template

def render_the_template(template, **dataDict):
    tm = Template(template)
    return tm.render(dataDict)

'''
It should return the string content for the template file.
'''
def openTemplate(fileName):
    return open(fileName,'r').read()