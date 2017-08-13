#input hours
#input wage
#if hours>40:
#apply overtime hours *1.5
#print wage

hours=int(input("How many hours did you work this week? "))
wage=10*hours
if hours>40:
    wage=(hours*1.5)+wage
print("Your wage is: $",wage)
