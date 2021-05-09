# In grams
dry_weight_per_liter = 0.1

carbon_ratio_of_dry_algae = 0.7

cubic_meters_of_water = 1

batch_time_days = 1

# Calculate
liters_of_water = cubic_meters_of_water * 1000
carbon_removed = liters_of_water * dry_weight_per_liter * carbon_ratio_of_dry_algae

removed_daily = carbon_removed / batch_time_days

print('grams of carbon removed per day')
print(removed_daily)

print('')
print('grams of carbon removed per year')
print(removed_daily * 365)
