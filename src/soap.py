from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print(cliente.service.Multiply(4,5))
print(cliente.service.Add(8,5))
print(cliente.service.Subtract(4,5))
print(cliente.service.Divide(20,5))    

