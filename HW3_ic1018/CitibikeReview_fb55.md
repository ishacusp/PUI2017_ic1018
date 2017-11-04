** hypothesis formulation **
The hyopotheses, null and alternative, are formulated consistently with the scientific question . The ratio would be better formulated with the sum of all rides at the denominator:

Rides_weekend_S / (Rides_weekend_S + Rides_week_S) >= Rides_weekend_C / (Rides_weekend_C + Rides_week_C)

This gives a proper normalization (numerator always smaller equal to denoinator)

** Data **

the data supports the question and is processed correctly, but the week is still split by day, instead of being split by weekend vs week

** Test **

As formulated this is a test of proportions with a categorical IV and thus the chi_square test for proportion is appropriate

** further suggestions **

the split between week and weekend deos not fully convey communte vs not communte and this should be disussed in the report. Fridays and mondays are in many mobility studies found to behave similarly to weekends, and there may be holidays in the month of data used, if only 1 month is used, which would skew the result.
A test for robustness by associating fridays with weekends, instead of weeks, and seing if the result is significantly different, or by only using tue wed thu for the week, may be useful. 
