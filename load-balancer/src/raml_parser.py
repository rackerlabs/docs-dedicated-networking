import jinja2
import pyraml.parser
import os

from collections import OrderedDict
from glob import glob

DIR = os.curdir
VALID_TYPES = [
    'readOnlyCollection',
    'creatableMember',
    'member',
    'collection',
    'deletableMember'
]


def parse_raml():
    """ Entry point for pyraml-parser implementation. """

    env = get_template_environment()
    temp = env.get_template('raml_to_md.html')

    raml_docs = get_all_raml_docs()
    for item in raml_docs:
        if 'lbs-v2-docs' in item:
            # Currently required, RAML doc is written in advance mode.
            continue
        api_doc = '{}/{}'.format(DIR, item)
        load = pyraml.parser.load(api_doc)

        ordered_load = create_payload(load)
        rendered = temp.render(ordered_load=ordered_load)

        rename = item.split('/')  # Convert to list
        file_name = rename.pop().replace('.raml', '.md')
        rename.append(file_name)
        file_path = '/'.join(rename)

        with open(file_path, 'w') as rendered_md:
            rendered_md.write(str(rendered))
    print('Parsing complete.')


def get_all_raml_docs():
    """ Return a list of raml docs with their relative paths."""

    all_raml_docs = glob('docs/**/*.raml')
    return all_raml_docs


def get_template_environment():
    """ Returns a Jinja2 environment object """

    env = jinja2.\
        Environment(loader=jinja2.PackageLoader('docs', 'templates'))
    return env


def normalize_parsed_data(
        data, count=0, ancestor='', parent='', container=None):
    """ Normalized a nested RamlRoot Object to a flat OrderedDict """

    if not container:
        _map = OrderedDict()
    else:
        _map = container
    count = count
    _ancestor = ancestor
    _parent = parent
    if data and isinstance(data, OrderedDict):
        for (key, value) in data.iteritems():
            if not count:
                _ancestor = key
                count = count + 1

            if value.resources:
                if _parent:
                    __parent = '{}{}'.format(_parent, key)
                else:
                    __parent = key
                _map[__parent] = value
                normalize_parsed_data(
                    value.resources, count, _ancestor, __parent, _map)
            else:
                if _parent:
                    mapper = None
                    if _parent is not ancestor:
                        mapper = '{}{}'.format(_parent, key)
                    else:
                        mapper = '{}{}'.format(ancestor, key)

                    _map[mapper] = value
                else:
                    mapper = '{}{}'.format(ancestor, key)
                    _map[mapper] = value
                count = 1
    return _map


def create_payload(resource=None):
    """ Retrieves RAML data from RamlRoot object. """

    if resource:
        ordered_load = OrderedDict()
        ordered_load.update({'title': resource.title})
        ordered_load.update({'base_uri': resource.baseUri})
        ordered_load.update({'security_schemes': resource.securitySchemes})
        ordered_load.update({'version': resource.version})

        parsed_data = normalize_parsed_data(resource.resources)
        ordered_load.update({'parsed_data': parsed_data})
    else:
        ordered_load = {}

    return ordered_load

if __name__ == '__main__':
    parse_raml()
