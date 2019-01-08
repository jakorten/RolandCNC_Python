@echo off
IF %1.==. GOTO NoPar
mode com%1:9600,n,8,1,p
goto end
:NoPar
echo.
echo ***No comport specified***
echo Example: setmode 3
echo.
:end