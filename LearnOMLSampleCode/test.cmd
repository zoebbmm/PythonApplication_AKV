@echo off
pytest tests --cov=LearnOMLSampleCode --verbose
pylint LearnOMLSampleCode
bandit --recursive LearnOMLSampleCode