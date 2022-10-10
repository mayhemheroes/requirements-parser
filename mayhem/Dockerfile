FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install
ADD ./mayhem/fuzz_parse.py /fuzz_parse.py

CMD ["/fuzz_parse.py"]
