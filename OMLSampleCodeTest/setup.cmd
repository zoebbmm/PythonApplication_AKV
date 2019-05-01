::##### DO NOT EDIT BELOW THIS LINE #####
@echo off
(conda env update -p .oml\env\OMLSampleCodeTest -f env-prod.yml --prune
.oml\env\OMLSampleCodeTest\python.exe setup.py install --prefix .oml\env\OMLSampleCodeTest)
::##### DO NOT EDIT ABOVE THIS LINE #####

::##### ADD CUSTOM COMMANDS BELOW #####