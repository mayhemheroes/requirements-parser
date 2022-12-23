FROM fuzzers/atheris:2.0.7-python3.9

RUN python3 -m pip install requirements-parser
ADD ./mayhem/fuzz_parse.py /fuzz_parse.py

CMD ["/fuzz_parse.py"]
