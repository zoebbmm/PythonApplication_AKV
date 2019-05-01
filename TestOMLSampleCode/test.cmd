@echo off
pytest tests --cov=TestOMLSampleCode --verbose
pylint TestOMLSampleCode
bandit --recursive TestOMLSampleCode