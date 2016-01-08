# ~*~ coding: utf-8 ~*~
import subprocess


def main():
    process_simplified_raml()
    process_advanced_raml()
    convert_to_rst_from_md()
    clean()
    copy_lbs_file_to_dev_guide()
    copy_fws_file_to_dev_guide()


def process_simplified_raml():
    """ Method that process the standard RAML doc"""
    try:
        raml_parser_py_output = subprocess\
            .check_output(['python', 'raml_parser.py'])
        print('Process #1', raml_parser_py_output)
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))


def process_advanced_raml():
    """ Method that process the advance firewall RAML doc"""

    """ TODO: EG - Create a list with these values [(input, output,),
        (input2, output2,)]"""
    input_file = 'docs/firewall.api.v2/api.raml'
    output_file = 'docs/firewall.api.v2/api.md'
    try:
        raml_parser_js_output = subprocess\
            .check_output(['node', 'raml_parser.js', input_file, output_file])
        print('Process #2', raml_parser_js_output)
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))


def convert_to_rst_from_md():
    try:
        subprocess.call(
            ['pandoc', '--from=markdown', '--to=rst',
                '--output=docs/firewall.api.v2/api.rst',
                'docs/firewall.api.v2/api.md'])
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))

    try:
        subprocess.call(
            ['pandoc', '--from=markdown', '--to=rst',
                '--output=docs/load-balancer.api.v2/api.rst',
                'docs/load-balancer.api.v2/api.md'])
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))

    print("RST conversion complete.")


def clean():
    try:
        subprocess.call(['rm', 'docs/firewall.api.v2/gitread.md'])
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))


def copy_lbs_file_to_dev_guide():
    _from = 'docs/load-balancer.api.v2/api.rst'
    _to = '../api-docs/api-operations/load-balancer-v2.rst'
    try:
        subprocess.call(['cp', _from, _to])
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))


def copy_fws_file_to_dev_guide():
    _from = 'docs/firewall.api.v2/api.rst'
    _to = '../api-docs/api-operations/firewall-v2.rst'
    try:
        subprocess.call(['cp', _from, _to])
    except subprocess.CalledProcessError as e:
        print("Encountered error: ", str(e))
    print('Copied RST files to destination')

if __name__ == '__main__':
    main()
