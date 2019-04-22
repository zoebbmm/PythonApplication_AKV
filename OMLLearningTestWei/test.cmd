@echo off
pytest tests --cov=OMLLearningTestWei --verbose
pylint OMLLearningTestWei
bandit --recursive OMLLearningTestWei