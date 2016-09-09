""" Build index from directory listing
"""

INDEX_TEMPLATE = r"""
<html>
<body>
<h2>Downloads for psych-214 class website</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}<a></li>
% endfor
</p>
</body>
</html>
"""

EXCLUDED = 'index.html'

import os
import sys

from mako.template import Template

def main():
    directory = sys.argv[1]
    fnames = [fname for fname in sorted(os.listdir(directory))
              if fname not in EXCLUDED]
    print(Template(INDEX_TEMPLATE).render(names=fnames))


if __name__ == '__main__':
    main()
