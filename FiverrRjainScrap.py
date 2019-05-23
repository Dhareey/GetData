import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from openpyxl import load_workbook
from lot import realLots


url = 'http://www.pittsburghlegaljournal.org/subscribe/pn_sheriffsale.php'
sheet2 = []
correctSheet = []
response = requests.get(url)
page = BeautifulSoup(response.content, 'lxml')
eachLine= page.find_all('div', class_ = 'notice_body_parent')
for i in eachLine:
    sales_id = i.find('span', {'id': 'notice_sequence_number'}).get_text()
    try:
        lots = i.find('div', {'id': 'notice_property_description'}).find_all('p')
        owner = i.find('span', {'id': 'notice_name2'}).get_text().strip()
        mgNum,amt = i.find_all('p', {'class': 'no_indent'})[1].get_text().split('$')[0][:-1],i.find_all('p', {'class': 'no_indent'})[1].get_text().split('$')[1]
        for lot in lots:
            pattern = re.compile(r'\d+-\w-\w+-?\w*-?\w*\.')
            match = pattern.findall(lot.get_text())[0]
            addressPattern = re.compile(r'\d+\s.+,\s\w+,\s\w+\s\d+.')
            try:
                addMatch = addressPattern.findall(lot.get_text())[0]
            except:
                pass
            add = addMatch.strip().split(',')
            address,city,statezip = add[0].strip(), add[1].strip(),add[2].strip()
            state,zipcode = statezip.split()[0],statezip.split()[1]
            block = realLots(match)
            emp = ''
            sheet2.append([sales_id,match,emp,emp,block[4],block])
            correctSheet.append([sales_id, emp,emp,owner,emp,emp,mgNum,amt,address,city,state,zipcode,emp,block,emp,emp,emp,emp])
    except:
        emp= ''
        can = 'cancelled'
        correctSheet.append([sales_id, emp,emp,can,emp,emp,can,can,can,can,can,can,emp,can,emp,emp,emp,emp])

# Convert sheet2 and correctSheet to pandas DataFrame
sheetFrame = pd.DataFrame(sheet2)
correctSheetFrame = pd.DataFrame(correctSheet)


book = load_workbook('sherriff may 2019.xlsx')
writer = pd.ExcelWriter('sherriff may 2019.xlsx',engine = 'openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
sheetFrame.to_excel(writer,'Sheet2')
correctSheetFrame.to_excel(writer, 'correct sheet')
writer.save()
writer.close()