Rackspace Developer Guide sample project

This sample project supports building API developer documentation using the Nexus 
build platform to deliver Rackspace-branded content from the developer.rackspace.com 
API documentation page](https://developer.rackspace.com/docs/). 

The project uses the Sphinx Python documentation Generator to build documentation 
from restructured text source files as part of a static build process. 


If you are interested in contributing, all you need is a basic understanding of the 
project layout and how to use [Restructured Text markup](http://sphinx-doc.org/rest.html).

Layout:

* **_images**: image assets unique to the documentation; this may include js,
  css, images, etc.
* **conf.py**: Configuration, no touchy.
* **index.rst**: Main index or landing page for the docs
* **make.bat**: windows build script
* **Makefile**: linux/osx build

If you want to build the project locally, you have two options:

- Install and run the [Sphinx documentation generator](http://sphinx-doc.org/) to build 
  the project by using the default Sphinx template.
  
- Install and run the [deconst client](https://github.com/deconst/client) to build the 
  project with Rackspace-branded templates. The output from this build renders the content 
  as it displays on developer.rackspace.com. To build, see the 
  [instructions for building with the client](https://github.com/rackerlabs/docs-migration/blob/master/docs/migration-instructions.rst#building-your-project-with-the-local-deconst-client).
  
##Build with Sphinx

In the root directory that contains the configuration file ``conf.py``, run the 
following command.
   
   ```
     make singlehtml
     
   ```
This command generates a single page html document with a navigation bar on the right.

The build output is written to this folder ``_build/singlehtml``. The generated content 
includes the html files and the associated templates and static assets that contain 
the default Sphinx templates and files that create the documentation interface.


To view the generated content, open the index.html file in the browser:

**Windows:**  _build/indexhtml/index.html

**OS/X:**   From the command line, type ``open _build/singlehtml/index.html

When your content is ready for production, submit an issue to the 
[Nexus control repository[(https://github.com/rackerlabs/nexus-control/issues) 
to request build integration and configuration to deploy to developer.rackspace.com.

Adding documentation
--------------------

Here's a brief description of the document writing workflow:

1. Fork and then clone the repo (https://github.com/rackerlabs/docs-core-infra-user-guide)
2. git remote add upstream https://github.com/rackerlabs/docs-core-infra-user-guide.git
3. git pull upstream master
4. Create a git branch named after the topic you are going to write about
5. Follow the basic structure and ReST conventions present in other existing .rst files
6. Run Sphinx (as explained above)
7. If no errors, git commit[1], then git push origin branch-name
8. Submit PR from your branch, to upstream master

[1] We're not committing and pushing the output HTML files. We're only going to commit and 
push the .rst files. After the project has been configured for the Nexus platform, 
the static pages are built and deployed automatically by the CI.
