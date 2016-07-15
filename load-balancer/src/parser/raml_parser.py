# ~*~ coding: utf-8 ~*~
import jinja2
import pyraml.parser
import sys

from collections import OrderedDict

# Set this value to disable stacktrace 0 - 5, 0 is disabled
sys.tracebacklimit = 0


def parse_raml(path=None):
    """ Entry point for pyraml-parser implementation. """

    env = get_template_environment()
    temp = env.get_template('raml_to_md.html')

    if path:
        load = pyraml.parser.load(path)
    else:
        raise Exception("Failed to load proper raml file")

    ordered_load = create_payload(load)
    rendered = temp.render(ordered_load=ordered_load)

    rename = path.split('/')  # Convert to list
    file_name = rename.pop().replace('.raml', '.md')
    rename.append(file_name)
    file_path = '/'.join(rename)
    with open(file_path, 'w') as rendered_md:
        rendered_md.write(str(rendered))


def get_template_environment():
    """ Returns a Jinja2 environment object """

    env = jinja2.\
        Environment(loader=jinja2.FileSystemLoader('templates'))
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
    resource_base_url = None
    if resource.baseUri:
        # This is making this bit of logic too smart...
        if 'Load Balancer' in resource.title:
            resource_base_url = resource.baseUri.replace(
                "https://bpi.automation.api.rackspacecloud.com",
                "https://lb.dedicated.api.rackspacecloud.com")
    resource_base_url = resource_base_url or resource.baseUri

    if resource:
        ordered_load = OrderedDict()
        ordered_load.update({'title': resource.title})
        ordered_load.update({'base_uri': resource_base_url})
        ordered_load.update({'security_schemes': resource.securitySchemes})
        ordered_load.update({'version': resource.version})

        parsed_data = normalize_parsed_data(resource.resources)
        ordered_load.update({'parsed_data': parsed_data})
    else:
        ordered_load = {}

    return ordered_load

if __name__ == '__main__':
    if sys.argv:
        path = sys.argv[1]
    parse_raml(path)
