@echo off
REM Script para iniciar o projeto Django SGHSS

REM Ir para a pasta do projeto (esta pasta do .bat)
cd /d %~dp0

echo ============================================
echo Ativando ambiente virtual...
echo ============================================
call venv\Scripts\activate.bat

echo ============================================
echo Aplicando migracoes...
echo ============================================
python manage.py migrate

echo ============================================
echo Iniciando servidor Django em http://127.0.0.1:8000
echo Feche esta janela para parar o servidor.
echo ============================================
python manage.py runserver

pause
