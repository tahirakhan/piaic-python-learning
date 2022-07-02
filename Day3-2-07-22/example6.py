# Arithmatic operation

from http.server import ThreadingHTTPServer
from operator import concat


firstName = "Tahir"
lastname = "Khan"
age = 10
fullName = firstName + ' ' + lastname
result = concat(firstName, lastname)

print('Full Name ', fullName)
print('Full Name ', result + str(age))
