import my_package.module_a as ma # module a imported => module b imported

print(ma.welcome_user("user")) # from module_a

print(ma.greet("user")) # from module_b