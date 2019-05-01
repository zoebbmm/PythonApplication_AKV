::##### DO NOT EDIT BELOW THIS LINE #####
@echo off
(conda env update -p .oml\env\LearnOMLSampleCode -f env-prod.yml --prune
.oml\env\LearnOMLSampleCode\python.exe setup.py install --prefix .oml\env\LearnOMLSampleCode)
::##### DO NOT EDIT ABOVE THIS LINE #####

::##### ADD CUSTOM COMMANDS BELOW #####