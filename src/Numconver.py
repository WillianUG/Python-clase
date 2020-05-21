from zeep import Client

cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
print(cliente.service.NumberToDollars(30.00))
print(cliente.service.NumberToWords(20.00)) 