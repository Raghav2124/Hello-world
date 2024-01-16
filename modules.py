import functions
functions.greeting("Raghav")# When using a function from a module, use the syntax: module_name.function_name.
#use of import
a = functions.person1["age"]
print(a)
#The dir() function can be used on all modules, also the ones you create yourself.
#When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]