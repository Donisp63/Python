Total = int(input("Enter your total budget: $")) # Total Budget Amount.

# The different spending categories.
Housing = int(input("Enter cost of housing: $"))
Utilities = int(input("Enter cost of Utilites: $"))
Groceries = int(input("Enter cost of Groceries: $"))
Transportation = int(input("Enter cost of Transportation: $"))
HealthCare = int(input("Enter cost of Health Care: $"))
PersonalCare = int(input ("Enter cost of Personal Care: $"))
Clothing = int(input("Enter cost of Clothing: $"))
Debt = int(input("Enter Debt amount: $"))

HousingP = (Housing / Total ) * 100 # Formula for getting the percent spent on Housing.
print(f"You spend {int(HousingP)}% on Housing.") # Should print "You spend <Housing percentage>% on Housing."

UtilitiesP = (Utilities / Total ) * 100 # Formula for getting the percent spent on Utilites.
print(f"You spend {int(UtilitiesP)}% on Utilites.") # Should print "You spend <Utilites Percentage>% on Utilites."

GroceriesP = (Groceries / Total ) * 100 # Formula for getting the percent spent on Groceries.
print(f"You spend {int(GroceriesP)}% on Groceries.") # Should print "You spend <Groceries Percentage>% on Groceries."

TransportationP = (Transportation / Total ) * 100 # Formula for getting the percent spent on Transportation.
print(f"You spend {int(TransportationP)}% on Transportation.") # Should print "You spend <Transportation Percentage>% on Transportation."

HealthCareP = (HealthCare / Total ) * 100 # Formula for getting the percent spent on Health Care.
print(f"You spend {int(HealthCareP)}% on Health Care.") # Should print "You spend <Health Care Percentage>% on Health Care."

PersonalCareP = (PersonalCare / Total ) * 100 # Formula for getting the percent spent on Personal Care.
print(f"You spend {int(PersonalCareP)}% on Personal Care.") # Should print "You spend <Personal Care Percentage>% on Personal Care."

ClothingP = (Clothing / Total ) * 100 # Formula for getting the percent spent on Clothing.
print(f"You spend {int(ClothingP)}% on Clothing.") # Should print "You spend <Clothing Percentage>% on Clothing."

DebtP = (Debt / Total ) * 100 # Formula for getting the percent spent on Debt.
print(f"{int(DebtP)}% of your total budget is Debt.") # Should print "<Debt Percentage>% of your total budget is Debt."





