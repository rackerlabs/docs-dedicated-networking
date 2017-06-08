# Rackspace Developer Guide sample project readme

This general readme explains how this project supports building API developer documentation using deconst
to deliver Rackspace-branded content from the [developer.rackspace.com API documentation page](https://developer.rackspace.com/docs/). 

The project uses the Sphinx Python Documentation Generator to build documentation 
from ReStructuredText (RST) source files as part of a static build process. 

If you are interested in contributing, all you need is a basic understanding of the 
project layout and how to use [Restructured Text markup](http://sphinx-doc.org/rest.html).

## Project Layout:

* **\_images**: assets unique to the documentation; this may include js,
  css, images, etc. despite the name of the directory
* **conf.py**: Sphinx configuration file
* **index.rst**: Main index or landing page for the docs
* **make.bat**: windows build script
* **Makefile**: linux/osx build
* **\_deconst.json**: Deconst configuration file

If you want to build the project locally, you can install and run the
[Sphinx documentation generator](http://sphinx-doc.org/) to build the project with the default
Sphinx template.
  
## Build with Sphinx

Navigate to the clone of the repo on your local machine. In the root directory that contains the
configuration file ``conf.py``, run the 
following command:

     make singlehtml

This command generates a single-page html document with a navigation bar on the right.

The build output is written to this folder ``_build/singlehtml``. The generated content 
includes the html files and the associated templates and static assets that contain 
the default Sphinx templates and files that create the documentation interface.

To view the generated content, open the index.html file in the browser:

**Windows:**  `_build/indexhtml/index.html`

**OS/X:**   From the command line, type `open _build/singlehtml/index.html`

When your content is ready for production, notify the Information Development team via
[email](mailto:devdocs@rackspace.com) or on [#docs on Slack](https://rackspace.slack.com/#docs)
to request build integration and configuration to deploy to developer.rackspace.com.

# Getting started with adding documentation to this repo

Here's a brief description of the document writing workflow:

1. Fork and then clone this repo.
1. Run `git remote add upstream git@github.com:rackerlabs/docs-dedicated-networking.git` in your terminal.
1. Run `git pull upstream master` in your terminal.
1. Create a git branch named after the topic you are going to write about.
1. Follow the basic structure and RST conventions present in other existing .rst files.
1. (_Optional_) Run Sphinx (as explained above) to view your content.
1. If no errors, `git add <your .rst files>`, `git commit`[1], and then `git push origin <branch-name>`, replacing `<branch-name>` with your branch name from step 4.
1. Submit a PR from your branch to the upstream master. Deconst will then build your content in a staging environment.
1. Once the staging build completes successfully, view the staging link provided by deconst. It will appear as a comment on the PR by RackerNexus.
1. Review the staging link for any formatting errors. Correct them if necessary.
1. If everything is satisfactory, request a review-and-merge from one of the IX team members through [#docs on Slack](https://rackspace.slack.com/#docs) (preferred) or via [email](mailto:devdocs@rackspace.com)

[1] Do not commit and push the output HTML files, just the .rst files. The static pages are built and deployed automatically by the CI from the .rst files themselves.
