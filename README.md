# Acronym Finder
***A python GUI tool to check acronym contents***   

## Dependencies:
python v3.10.4  
pyside6==6.3.0  
pyinstaller v5.1 (optional)  
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
// install package with specified aliyun source path
pip install pyside6==6.3.0 -i https://mirrors.aliyun.com/pypi/simple
pip install pyinstaller==5.1 -i https://mirrors.aliyun.com/pypi/simple  (optional)
// or install all 
pip install requirements.txt
```

## pack with pyinstaller
```C
pyinstaller --clean main.spec
//or  
pyinstaller --onefile --noconsole --clean main.py
```
