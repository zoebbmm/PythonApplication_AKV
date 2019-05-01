::##### DO NOT EDIT BELOW THIS LINE #####
@echo off
(conda env update -p .oml\env\TestOMLSampleCode -f env-prod.yml --prune
.oml\env\TestOMLSampleCode\python.exe setup.py install --prefix .oml\env\TestOMLSampleCode)
::##### DO NOT EDIT ABOVE THIS LINE #####

::##### ADD CUSTOM COMMANDS BELOW #####