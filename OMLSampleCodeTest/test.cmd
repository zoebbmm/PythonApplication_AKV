@echo off
pytest tests --cov=OMLSampleCodeTest --verbose
pylint OMLSampleCodeTest
bandit --recursive OMLSampleCodeTest