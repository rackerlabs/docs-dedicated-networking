# ~*~ coding: utf-8 ~*~
import fnmatch
import os
import subprocess
import sys


def Automate(path):
    """ Entry point to RAML Automative Parser.
    :param path:
    :return:
    """
    if path:
        for file in _find_files(path, '*.raml'):
            # Seems like duplication, but because the simple parser can fail, we
            # need to be able to capture the failure, and then run the advance
            # parser.
            # This is do to python parser, not being maintained.
            try:
                create_md_from_raml(file)
                print("Converted `{}` to MD format.".format(file))
            except Exception as e:
                print("\nFailed to parse: `{}`, with error: `{}`"
                      .format(file, str(e)))
            try:
                convert_to_rst_from_md(file)
            except subprocess.CalledProcessError as e:
                print("{}\n".format(str(e)))
            try:
                convert_raml_to_html(file)
            except subprocess.CalledProcessError as e:
                print("{}\n".format(str(e)))
    else:
        print("ERROR: Invalid path, or no path specified.")


def create_md_from_raml(file):
    """ Provided a file, convert to MD format
    :param file: string
    :return:
        void
    """

    try:
        md_file = subprocess\
            .check_output(['python', 'raml_parser.py', file])
    except Exception as e:
        raise Exception("Failed to parse RAML file. Error: {}".format(str(e)))
    print(md_file)  # Echoes all the prints from the inner parser.


def convert_to_rst_from_md(file):
    """ Convert MD to RST format.
    :param file: string
    :return:
        void
    """
    md_file = _construct_file_to_extension(file)
    rst_file = _construct_file_to_extension(file, ".rst")
    try:
        subprocess.call(
                ['pandoc', '--from=markdown', '--to=rst',
                 '--output={}'.format(rst_file),
                 md_file])
        print("RST conversion complete.")
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError("Encountered error: ", str(e))


def convert_raml_to_html(file):
    """ Method that converts from RAML to HTML format.
    :param: _file: str
    :return:
        void
    """
    html_file = _construct_file_to_extension(file, '.html')
    try:
        subprocess.call(['raml2html', '-i', file, '-o', html_file])
        print("Converted RAML to HTML")
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError("Encountered error: ", str(e))


def _find_files(directory, pattern):
    """ Generate a file location based on directory and lookup pattern.
    :param directory: string
    :param pattern: string
    :return:
        string: filename
    """
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def _construct_file_to_extension(file, extension='.md'):
    """ Constructs path based on file and desired extension.
    :param file: string
    :param extension: string
    :return:
        string
    """
    if file:
        output_file = file.split('/')
        md = output_file[-1].replace('.raml', extension)
        output_file.pop(-1)
        output_file.append(md)
        output_file = '/'.join(output_file)
    return output_file or None


if __name__ == '__main__':

    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]

    Automate(path)
