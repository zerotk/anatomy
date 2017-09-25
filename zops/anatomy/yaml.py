

def yaml_from_file(filename_):
    with open(filename_, 'r') as iss:
        content = iss.read()
        result = yaml_load(content)
    return result


def yaml_load(text):
    from ruamel.yaml import YAML
    from collections import OrderedDict

    loader = YAML(typ='safe')
    loader.constructor.mapping_type = OrderedDict
    return loader.load(text)
