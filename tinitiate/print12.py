"""
This
is a multiline 
comment
"""
# Any text between TWO LINEs of THREE DOUBLE QUOTES is a multiline comment
"""
print('Welcome to tinitiate.com python turorials');
print("Welcome to tinitiate.com " , 'python turorials "Appended"');
print('Welcome to tinitiate.com ' + 'python turorials "Appended"')
print('Welcome to tinitiate.com ' + 'python turorials "Appended"')


print('Printing a single quote \'')

print(123)
print(12.3)
print("\"\"\"\\' abc)")
print('"abc)')

a = 10
b = 20
a = b
a =30
a = "a"
a= 'a'


print('print a double %5.3f' % (1000.23232))
print('print a double %5.5f' % (1000.23232))
print('print a double %5.7f' % (1000.23232))
#OUTPUT: print a double 1000.232

# Create variables
strVal = 'tinitiate.com'
intval = 100
print("String=%s  Integer= %i" % (strVal, intval))
print("String= %s Integer= %i" % ("aaa", 122))


"""
"""
str = 'tinitiate.com'
print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'));
#OUTPUT:  Welcome to tinitiate.com training of python language

print('{0} and {1}'.format(str, 'python'))
#OUTPUT:  tinitiate.com and python

print('{1} and {0}'.format('tinitiate.com', 'python'))
#OUTPUT: python and tinitiate.com

print('{siteName} teaches {LanguageName}.'.format(siteName=str, LanguageName='python'))
#OUTPUT: tinitiate.com teaches python.

#Positional and key-value arguments can be arbitrarily combined:
print('The site {0} teaches {LanguageName}'.format('tinitiate.com', LanguageName='Python'))

"""
var_integer = 1                # An integer type variable
var_float   = 10.44            # A float type variable
var_string  = "tinitiate.com"  # A string type variable

print(var_integer, var_float, var_string)
print ("hello " * 3)
print("line1" + '\n' + "line2"+ '\n')
print(r'This is a ASCII string, Has no special characters')
print(u'This is beta (ß), and Has special characters')
