# Variables for kg values
kg_value_1 = 20
kg_value_2 = 50
kg_value_3 = 15
kg_value_4 = 61

# Conversion factor: 1lb (Pound) = 2.20462kg (Kilograms)
conversion_factor = 2.20462

# Calculate kilograms for each pound value
lb_value_1 = kg_value_1 * conversion_factor
lb_value_2 = kg_value_2 * conversion_factor
lb_value_3 = kg_value_3 * conversion_factor
lb_value_4 = kg_value_4 * conversion_factor

# Output the results
print(f"{kg_value_1} kilograms is equal to {lb_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4:.2f} pounds.")