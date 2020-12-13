from time import sleep
import string
import xlsxwriter
from xlsxwriter import Workbook
from time import sleep
import xlrd
import requests
from xlrd import open_workbook
import xlutils
from xlutils.copy import copy

class Run:
    def __init__(self,path=''):
        self.path = path
        self.item_id = ''
        self.customer_id=[]
        self.status=[]
        self.name='asd'
        self.contact='9716567856'
        self.email='you@gmail.com'
        self.invoice_id=[]
        self.col_name=[]
        self.col_mob=[]
        self.col_email=[]
        self.col_cost=[]
        self.col_amount=[]
        self.amount_paid=[]
        self.index=0
        # self.workbook=Workbook("result.xlsv")
        # self.worksheet=self.workbook.add_worksheet("School Payment")
        try:
            self.read_sheet()
            #print("yes")
            #self.get_item()
            self.generate_invoice()
            self.check_payment()
            # self.update_sheet()
            # self.workbook.close()
        except Exception as e:
            print(e)
                    
            
    def read_sheet(self):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_index(0)
        for i in range(1,sheet.nrows):
            self.col_name.append(sheet.cell_value(i,0))
            self.col_mob.append(sheet.cell_value(i,1))
            self.col_email.append(sheet.cell_value(i,2))
            self.col_cost.append(sheet.cell_value(i,3))
            self.col_amount.append(sheet.cell_value(i,4))
			
            self.name=sheet.cell_value(i,0)
            self.contact=sheet.cell_value(i,1)
            self.email=sheet.cell_value(i,2)
            self.add_customer()
        
    def add_customer(self):
        url="https://api.razorpay.com/v1/customers"
        PARAMS = {
        'name':self.name,'contact':self.contact,'email':self.email}
        r = requests.post(url = url,auth=('rzp_test_nszN0TzwchFKDB','tDDE5guqiyPCqNJlrN0BGvWJ'), params = PARAMS)
        data = r.json()
        print(data)
        self.customer_id.append(data['id'])

    def get_item(self):
        url="https://api.razorpay.com/v1/items"
        print(self.col_name[self.index])
        print(self.col_amount[self.index])
        PARAMS ={'name':self.col_name[self.index],'amount':int(self.col_amount[self.index]),'currency':'INR'}
        r = requests.post(url = url,auth=('rzp_test_nszN0TzwchFKDB','tDDE5guqiyPCqNJlrN0BGvWJ'),params=PARAMS)
        data = r.json()
        print(data)
        item=(data['id'])
        self.item_id=item
        print(self.item_id)

        
    def generate_invoice(self):
        print(self.customer_id)
        for i in self.customer_id:
            self.get_item()
            print("chutmarike")
            self.index=self.index+1
            print(i)
            url="https://api.razorpay.com/v1/invoices"
            PARAMS = {
            'customer_id':i,
            'line_items': [
        {
          "item_id": self.item_id
        }
      ],   
            "sms_notify": 1,
            "email_notify": 1
            }
            r = requests.post(url = url,auth=('rzp_test_nszN0TzwchFKDB','tDDE5guqiyPCqNJlrN0BGvWJ'), json = PARAMS)
            data = r.json()
            self.invoice_id.append(data['id'])
            print(data)
            
    def check_payment(self):
        url="https://api.razorpay.com/v1/invoices/"
        for flag in self.invoice_id:
            r = requests.get(url = url+flag,auth=('rzp_test_nszN0TzwchFKDB','tDDE5guqiyPCqNJlrN0BGvWJ'))
            data = r.json()
            print(data['status'])
            self.status.append(data['status'])
            self.amount_paid.append(data['amount_paid'])
            
        

    def update_sheet(self):
        try:
            # self.worksheet.write(0,0,'student_name')
            # self.worksheet.write(0,1,'contact_no')
            # self.worksheet.write(0,2,'email')
            # self.worksheet.write(0,3,'cost')
            # self.worksheet.write(0,4,'due')
            ind=0
            # row=1
            # print(self.status)
            result = []
            for flag in self.status:
                # print(ind)
                # self.worksheet.write(row,0,self.col_name[ind])
                # self.worksheet.write(row,1,self.col_mob[ind])
                # self.worksheet.write(row,2,self.col_email[ind])
                cost = int(self.col_cost[ind])
                due = int(self.col_amount[ind])
                
                if flag=='paid':
                    final=cost+due-(self.amount_paid[ind])
                else:
                    final=cost+due
                self.col_amount=final
                # self.worksheet.write(row,3,cost)
                # self.worksheet.write(row,4,final)
                
                # row=row+1
                result.append({'student_name': self.col_name[ind], 'contact_no':self.col_mob[ind], 'email':self.col_email[ind],'cost':self.col_[ind],'amount':self.col_amount[ind]})
		ind=ind+1
            return result

        except Exception as e:
            print (e)
            return []
