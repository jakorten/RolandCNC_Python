@echo off
color 0A
title Move Mill
cls

set qtmp=""
set ccom=""
set xCoord=""
set yCoord=""
set zCoord=""

:start 
echo.
echo Batch script to move roland MDX 15/20 printer
echo Syntax: movemill p,x,y,z
echo p:      com port (default=3)
echo x,y,z:  Coordinates * 10 "Example 2.55mm -> 25"
echo.

IF %1.==. GOTO NoPar
IF %2.==. GOTO NoPar
IF %3.==. GOTO NoPar
IF %4.==. GOTO NoPar
set ccom=%1
set xCoord=%2
set yCoord=%3
set zCoord=%4
GOTO moveit


:NoPar
echo.
echo Enter com port where mill is attached
echo (q. quit)
echo.
set /p ccom="com: "
if %ccom%==q goto end

cls
echo.
echo Enter X Coordinate * 10 
echo "Example 2.55mm -> 25"
echo (q. quit)
echo.
set /p xCoord="X=: "
if %xCoord%==q goto end

cls
echo.
echo Enter Y Coordinate * 10
echo "Example 1.0mm -> 10"
echo (q. quit)
echo. 
set /p yCoord="Y=: "
if %yCoord%==q goto end

cls
echo.
echo Enter Z Coordinate * 10
echo "Example -0.1mm -> -1"
echo (q. quit)
echo. 
set /p zCoord="Z=: "
if %zCoord%==q goto end

:moveit
cls
set /a xConv=%xCoord% * 4
set /a yConv=%yCoord% * 4
set /a zConv=%zCoord% * 4
echo.
echo Configuring port...

call setmode %ccom%
echo Press enter key to move mill on com%ccom% to %xCoord%,%yCoord%,%zCoord% (q. quit)
echo ***Make sure z-zero is set and no objects are in the way***
echo.
set /p qtmp=" "
if %qtmp%==q goto end
echo ;;^^IN;!RC0;!MC1;!PZ0,40;^^PU%xConv%,%yConv%;V3;Z%xConv%,%yConv%,%zConv%;!MC0; > com3
cls
echo.
echo Operation complete
echo.
:end