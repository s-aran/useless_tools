import unittest
import sys

TESTFILE_PATTERN = 'test*.py'


def print_suite(suite, path, processed={}):
    if hasattr(suite, '__iter__'):
        for s in suite:
            print_suite(s, path, processed)

    else:
        # remove first "./"
        p = "{}.".format(path[2:].replace("/", ".")) if path != "." else ""

        s = type(suite)

        # print file name
        if s.__module__ not in processed.keys():
            print("{}{}".format(
                p,
                s.__module__,
                )
            )

            processed[s.__module__] = []

        # print class name
        if s.__name__ not in processed[s.__module__]:
            print("{}{}.{}".format(
                p,
                s.__module__,
                s.__name__
                )
            )

            processed[s.__module__].append(s.__name__)

        # print method name
        print("{}{}.{}.{}".format(
            p,
            s.__module__,
            s.__name__,
            suite._testMethodName
            )
        )


if __name__ == '__main__':
    args = sys.argv
    path = '.' if len(args) <= 1 else args[1]

    print_suite(
            unittest.defaultTestLoader.discover(path, TESTFILE_PATTERN),
            path
            )
