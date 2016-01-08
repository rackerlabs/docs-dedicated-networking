var fs = require('fs');
var nunjucks = require('nunjucks');
var raml = require('raml-parser');
// RAML file to be parsed
var ramlFile = process.argv[2];
// Path and file name for the new file being created.
var savePath = process.argv[3];

raml.loadFile(ramlFile).then(function (rootNode) {
    var result = {};
    var flatten_object = {};

    result['title'] = rootNode.title;
    result['baseUri'] = rootNode.baseUri;
    result['version'] = rootNode.version;
    result['securedBy'] = rootNode.securedBy;
    result['resources'] = {};
    if (rootNode.resources) {
        flatten_object = flattenResources(rootNode.resources);
        for (item in flatten_object) {
            result['resources'][item] = flatten_object[item];
        }
    }
    createMarkdownFile(result);
}, function (error) {
    console.log(error);    
});

function flattenResources(resources) {
    var bucket = {};
    var len = resources.length;
    var result;

    for (var i = 0; i < len; i++) {
        var resource_item = resources[i];
        if (typeof(resource_item.resources) !== 'undefined') {
            result = nextDepth(resource_item.resources, resource_item, resource_item.relativeUri);
            for (item in result) {
                bucket[item] = result[item];
            }
        }
    }

    function nextDepth(resource, root_resource, root, segment, depths) {
        var depth = {};
        var len = resource.length;
        if (depths) {
            depth = depths;
        }
        
        if (root_resource) {
            segment = root;
            depth[segment] = root_resource;
        }

        for (var i = 0; i < len; i++) {
            var resource_item = resource[i];
            var path = segment + resource_item.relativeUri;
            
            if (typeof(resource_item.resources) !== 'undefined') {
                depth[path] = resource_item;
                nextDepth(resource_item.resources, false, resource_item.relativeUri, path, depth);
            } else {
                depth[path] = resource_item;
            }
        }
        return depth;
    }

    return bucket;
}

function createMarkdownFile(parsedData) {
    var template_data = {};
    template_data['data'] = parsedData;
    fs.readFile('docs/templates/html_to_md.html', function (err, source) {
        if (err) throw err;
        nunjucks.configure('docs/templates', {autoescape: false});
        var template = nunjucks.render('html_to_md.html', template_data);
        fs.writeFile(savePath, template, function (err) {
            if (err) 
                throw err;
            console.log('File has been saved..');
        });
    });

    
}
