#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014, Issa Rice
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import json
from datetime import datetime
import yaml
from yaml import SafeLoader, BaseLoader
from jinja2 import Template, Environment, FileSystemLoader
from tag_ontology import *
from util import *

class AbsolutePathException(Exception):
    pass

class DirectoryException(Exception):
    pass

class Filepath(object):
    '''
    Represents a single filepath of a file relative to the current
    directory.
    '''
    def __init__(self, path):
        path = path.strip()
        if path[0] in ["/", "~"]:
            raise AbsolutePathException(
                "path is absolute; must be relative"
            )
        elif path[-1] in ["/"] or os.path.isdir(path):
            raise DirectoryException(
                "path is a directory; must be a file"
            )
        self.path = path

    def __repr__(self):
        return self.path

    def filename(self):
        '''
        Return the base filename.

        >>> Filepath("pages/programming/hello.md").filename()
        'hello.md'
        '''
        return os.path.split(self.path)[1]

    def directory(self):
        '''
        Return the relative directory name.

        >>> Filepath("pages/programming/hello.md").directory()
        'pages/programming/'
        '''
        return os.path.split(self.path)[0] + "/"

    def path_lst(self):
        '''
        Return a list of the individual components of the filepath.

        >>> Filepath("pages/programming/hello.md").path_lst()
        ['pages', 'programming', 'hello.md']
        '''
        return split_path(self.path)

    def route_with(self, route):
        return route(self)

    def relative_to(self, other):
        '''
        >>> fp1 = Filepath("tags/python")
        >>> fp2 = Filepath("pages/programming/hello.md")
        >>> print(fp1.relative_to(fp2))
        ../../tags/python
        '''
        path1 = os.path.normpath(self.path)
        path2 = os.path.normpath(other.path)
        depth = len(Filepath(path2).path_lst()) - 1
        return Filepath("../" * depth + path1)

    def to_item(self):
        with open(self.path, 'r') as f:
            return Item(self, f.read())

class Route(object):
    '''
    Represents a route (Filepath -> Filepath)
    '''
    def __init__(self, route):
        self.route = route

    def __call__(self, filepath):
        if type(filepath) is not Filepath:
            raise TypeError("input is not a filepath")
        result = self.route(filepath)
        if type(result) is not Filepath:
            raise TypeError(
                "output is not a filepath; " +
                "this route object is an invalid route"
            )
        return result

class Tag(object):
    '''
    Represents a tag
    '''
    def __init__(self, name, pages=[]):
        self.name = name
        self.pages = pages

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return (slug(self.name) == slug(other.name))

class TagList(object):
    def __init__(self, data=[]):
        self.data = data

    def __repr__(self):
        return self.data.__repr__()

    def standardize_using(self, tag_synonyms):
        '''
        Take a dictionary of tag synonyms  and update the TagList
        instance's list of tags according to the synonyms.  For
        instance, if tag_synonyms contains the line
            "university-of-washington": ["uw", "uwashington"],
        and if tags contains "uw" or "uwashington", then this will be
        replaced by "university-of-washington".
        '''
        result = []
        for tag in self.data:
            canonical = []
            for key, value in tag_synonyms.items():
                slug_value = [slug(i) for i in value]
                if slug(tag) == slug(key) or slug(tag) in slug_value:
                    canonical.append(key)
            if not canonical:
                # So could not find a match in tag_synonyms
                canonical = [tag]
            result.extend(canonical)
        self.data = result

    def imply_using(self, tag_implications):
        '''
        Take an OrderedDict of tag implications and  update the TagList
        instance's list of tags with the implications applied.  Apply
        this after standardizing tags.
        '''
        for key in tag_implications:
            if key.lower() in self.data or key in self.data:
                self.data.extend(tag_implications.get(key))
        self.data = list(set(self.data))

    def organize_using(self, tag_synonyms, tag_implications):
        self.standardize_using(tag_synonyms)
        self.imply_using(tag_implications)

def process_metadata(metadata, **kwargs):
    # Combine kwargs; kwargs overrides
    metadata.update(kwargs)
    math = "False"
    if "math" in metadata:
        # Change possible bool to str
        math = str(metadata['math'])
    metadata['math'] = math
    license = "UNKNOWN"
    if "license" in metadata:
        license = metadata['license']
        # Clean up license string
        for char in ' -':
            license = license.replace(char, '')
        license = license.upper()
        if license in ["CC0", "PUBLICDOMAIN", "PD"]:
            license = "CC0"
        elif license in ["CCBY", "BY", "ATTRIBUTION"]:
            license = "CC-BY"
        elif license in ["CCBYSA", "CCSA", "SHAREALIKE"]:
            license = "CC-BY-SA"
        else:
            # Set default license to unknown (i.e., copyrighted)
            license = "UNKNOWN"
    metadata['license'] = license
    tags = ["untagged"]
    if "tags" in metadata:
        tag_list = TagList(parse_as_list(metadata['tags']))
        tag_list.organize_using(TAG_SYNONYMS, TAG_IMPLICATIONS)
        tags = tag_list.data
    metadata['tags'] = tags
    aliases = []
    if "aliases" in metadata:
        aliases = parse_as_list(metadata['aliases'])
    metadata['aliases'] = aliases
    language = "English"
    if "language" in metadata:
        language = metadata['language']
    metadata['language'] = language
    return metadata

class Page(object):
    '''
    Represents a typical page (i.e. those that are read from a file and
    are to be converted); special pages like the page with all the tags
    will not be an object of this class.
    '''
    def __init__(self, origin, metadata={}):
        if type(origin) is Filepath:
            self.origin = origin
        else:
            self.origin = Filepath(origin)
        self.metadata = process_metadata(metadata)

    def load_metadata(self):
        with open(self.origin.path, 'r') as f:
            metadata = ""
            first = f.readline()
            if first == '---\n':
                then = f.readline()
                while then not in ['---\n', '...\n', '']:
                    metadata += then
                    then = f.readline()
            self.metadata = process_metadata(yaml.load(
                metadata,
                Loader = BaseLoader,
            ))

    def pandoc_compiled(self):
        '''
        Compile page with Pandoc and return the string of the output.
        '''
        output = run_command("pandoc --smart -f markdown -t json {page}".format(page=self.origin.path))
        ast = json.loads(output)
        return to_unicode(
            run_command(
                "pandoc -f json -t html --toc --toc-depth=4 " +
                "--template=templates/toc.html --smart --mathjax " +
                "--base-header-level=2 --filter generator/url_filter.py",
                pipe_in=json.dumps(ast, separators=(',',':'))
            )
        )

    def compiled(self, tags_dir):
        '''
        Compile page all the way and return the string of the output.
        '''
        if not self.metadata:
            self.load_metadata()
        env = Environment(loader=FileSystemLoader('.'))
        if self.metadata['language'].lower() in [u"ja", u"japanese",
            u"にほんご", u"日本語"]:
            skeleton = env.get_template('templates/ja/skeleton.html')
        else:
            skeleton = env.get_template('templates/skeleton.html')
        final = skeleton.render(
            body = self.pandoc_compiled(),
            # In templates, we use page.field to access metadata fields
            page = self.metadata,
            tags = sorted(
                [
                    {
                        'name': tag,
                        'path': to_unicode(
                            Filepath(to_string(slug(tag))).\
                            route_with(to_dir(tags_dir)).path,
                        ),
                    }
                    for tag in self.metadata["tags"]
                ],
                key = lambda t: t['name'].lower(),
            ),
            source = to_unicode(self.origin.path),
            path = "./",
        )
        return final

    def base(self):
        return self.origin.route_with(set_extension("")).route_with(drop_one_parent_dir_route).path

    def __repr__(self):
        return "Page({})".format(self.origin.path.__repr__())

    def revision_date(self, string=True):
        try:
            rev_date = self.metadata.__getattribute__(
                'last-major-revision-date'
            )
        except AttributeError:
            rev_date = ''
        rev_date = to_string(rev_date) # sanitize
        if rev_date != '':
            date_obj = datetime.strptime(rev_date, '%Y-%m-%d')
            if string:
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z").strip()
            else:
                return date_obj
        else:
            date_obj = datetime.strptime("2010-01-01", '%Y-%m-%d')
            if string:
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z").strip()
            else:
                return date_obj

@Route
def drop_one_parent_dir_route(filepath):
    return Filepath('/'.join([i for i in split_path(filepath.path)[1:]]))

def to_dir(dirname):
    '''
    dirname(str) -> (Filepath -> Filepath)
    '''
    @Route
    def f(filepath):
        return Filepath(dirname + filepath.path)
    return f

def set_extension(extension):
    '''
    Extension(str) -> Filepath -> Filepath
    '''
    @Route
    def f(filepath):
        '''
        Filepath -> Filepath
        '''
        return Filepath(os.path.splitext(filepath.path)[0] + extension)
    return f

site_dir = "_site/"
site_dir_route = to_dir(site_dir)

@Route
def my_route(filepath):
    return filepath.route_with(set_extension("")).route_with(drop_one_parent_dir_route).route_with(site_dir_route)

