#! /usr/bin/python3
import logging
import sys
import io
import atheris

logging.disable(logging.CRITICAL)

with atheris.instrument_imports():
    import requirements


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    fd = io.StringIO()
    fd.write(fdp.ConsumeUnicodeNoSurrogates(atheris.ALL_REMAINING))

    requirements.parse(fd)


def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
