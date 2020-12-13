# Razorpay-Hackathon
Here we present an application to automate the fees management system for schools in which students are sent the invoices for the monthly fees with dues(if present) at the beginning of each month and they can pay the fees through the payment link provided along with the invoice.

This repository contains the script for fetching data from our database to create customers, create items and generate invoices for them along with payments links which upon transaction(successful/failure) are fetched and the database is updated. Database contains the information of the students, their fees to be paid and the due amount which are updated every month according to the result of the previous transactions.

read_sheet: This functions reads the database for the student information.

add_customer: This function creates customers from our database by using their information(name,email_id,contact_no).

get_item: This fucntion is used to create items on the basis of the provided info(name_item,cost)

generate_invoice: This function is used to generate invoice for a particular customer for a item ordered(fees in our usecase) along with a payment link which can be used to pay the amount within a month 

check_payment: This function is used to check the status of the payment.

update_sheet: This function is used to update the sheet according the status of the last invoice and if the payment was unsuccessful then the due amount is added in the next amount's and if it is successful dues are adjusted and updated amount request is sent.


