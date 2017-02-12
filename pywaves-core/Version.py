import re


class Version(object):
    version_re = re.compile(r"^(\d+) \. (\d+) (\. (\d+))?", re.VERBOSE | re.ASCII)

    major = 0
    minor = 0
    patch = 0

    def __init__(self, version_string=None):
        if version_string:
            self.parse(version_string)

    def parse(self, version_string):
        match = self.version_re.match(version_string)
        if not match:
            raise ValueError("invalid version number '%s'" % version_string)

        (major, minor, patch) = match.group(1, 2, 4)

        self.major = int(major)
        self.minor = int(minor)

        if patch:
            self.patch = int(patch)
        else:
            self.patch = 0
