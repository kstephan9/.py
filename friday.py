Python 3.6.7 (default, Jul  2 2019, 02:21:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> an = ['cat', 'dog', 'horse']
>>> an
['cat', 'dog', 'horse']
>>> an_list = [a for a in an]
>>> an_list
['cat', 'dog', 'horse']
>>> an_list = [a for a in an if len(an) >3]
>>> an_list
[]
>>>  an_list = [a for a in an if len(a) >3]
SyntaxError: unexpected indent
>>> an_list = [a for a in an if len(a) >3]
>>> an_list
['horse']
>>> an_list = [a for a in an if len(a) >3]
>>> an_list
['horse']
>>> import xlrd
>>> from DefaultItems import Raw2_Folder
Logger level:  10
Python Version:  3.6.7 (default, Jul  2 2019, 02:21:41) [MSC v.1900 64 bit (AMD64)]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    from DefaultItems import Raw2_Folder
ImportError: cannot import name 'Raw2_Folder'
>>> from DefaultItems import Raw_2Folder
>>> wb1 = 'Work Closed Yesterday.xlsx'
>>> wb1_name = 'Work Closed Yesterday.xlsx'
>>> wb1
'Work Closed Yesterday.xlsx'
>>> wb1_name
'Work Closed Yesterday.xlsx'
>>> book1 = xlrd.open_workbook(wb1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    book1 = xlrd.open_workbook(wb1)
  File "C:\EngTools\Anaconda3\v5.2.0\lib\site-packages\xlrd\__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'Work Closed Yesterday.xlsx'
>>> import os
>>> wb1_pan = os.path.join(Raw_2Folder, wb1_name)
>>> book1 = xlrd.open_workbook(wb1_oan)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    book1 = xlrd.open_workbook(wb1_oan)
NameError: name 'wb1_oan' is not defined
>>> book1 = xlrd.open_workbook(wb1_pan)
>>> first_sheet = book1.sheet_by_index(0)
>>> first_sheet
<xlrd.sheet.Sheet object at 0x0000026EBA504C50>
>>> print(first_sheet.row_values[0])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(first_sheet.row_values[0])
TypeError: 'method' object is not subscriptable
>>> print(first_sheet.row_values(0))
['Number', 'Task type', 'Priority', 'Contact type', 'Opened', 'Opened by', 'Updated', 'Updated by', 'Affected User [Incident]', 'Sector [Incident]', 'Requested for [Request]', 'Sector', 'Short description', 'Description', 'Additional comments', 'Item [Requested Item]', 'State', 'Parent', 'Assignment group', 'Assigned to', 'Tier 1 resolvable? [Incident]', 'Work notes', 'Closed', 'Closed by', 'Resolved [Incident]', 'Resolved by [Incident]', 'DurationDays']
>>> headings = first_sheet.row_values(0)
>>> i = 0
>>> for row in range(first_row
