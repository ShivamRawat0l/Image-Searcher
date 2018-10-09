from selenium import webdriver
from openpyxl import load_workbook
wb=load_workbook(filename="cities.xlsx")
wb=wb.active
driver=webdriver.Chrome('chromedriver.exe');
for a in range(1,297):
    search=wb['A'+str(a)].value;
    driver.get(f"https://www.google.co.in/search?q={search}&rlz=1C1CHBD_enIN799IN799&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi0hauz5fbdAhVYOisKHU8QBTMQ_AUIECgD&biw=675&bih=662");
    search=input()