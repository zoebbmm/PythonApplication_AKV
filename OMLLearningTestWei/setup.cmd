::##### DO NOT EDIT BELOW THIS LINE #####
@echo off
(conda env update -p .oml\env\OMLLearningTestWei -f env-prod.yml --prune
.oml\env\OMLLearningTestWei\python.exe setup.py install --prefix .oml\env\OMLLearningTestWei)
::##### DO NOT EDIT ABOVE THIS LINE #####

::##### ADD CUSTOM COMMANDS BELOW #####