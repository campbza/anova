
I made the "main" functions runabble via the command line.

## Running ANOVA

There are now three modes of running `anova.py`.  They write to CSV files with very detailed filenames.  Watch out, they overwrite existing files if they are in the directory!  This is a change from Zachary's original code, that just happened to work better when I'm running lots of these.

- `python3 anova.py estimate`: Runs the three-group example, using MSE as the estimate of the variance when generating the null distribution.

```
m1 = 0.35
m2 = 0.5
m3 = 0.65
stddev = 0.15
```

- `python3 anova.py realvar`: Runs the three-group example, using `stddev**2` as the real variance when generating the null distribution.

```
m1 = 0.35
m2 = 0.5
m3 = 0.65
stddev = 0.15
```

- `python3 anova.py noisy`: Runs the six-group example, using MSE as the estimate of the variance when generating the null distribution.

```
means_list = [0.5,0.5,0.5,0.6,0.4,0.43]
stddev = 0.2
```

## Plotting values in CSV files

```
python3 csvreader.py ARtest_estimate_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_12counts.csv AR_estimate.png 'Differentially private ANOVA, MSE estimate of variance'

python3 csvreader.py ARtest_realvar_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_12counts.csv AR_realvar.png 'Differentially private ANOVA, ground truth variance'

python3 csvreader.py ARtest_noisy_1000runs_6means_0.20var_5epsilons_12counts.csv AR_noisy.png 'ANOVA with smaller effect size'
```

## Adding additional points

Rerun with different values of epsilon and/or group sizes. Let's call it tmp_estimate.csv.

```
cat ARtest_estimate_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_12counts.csv tmp_estimate.csv > ARtest_estimate_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv
python3 csvreader.py ARtest_estimate_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv AR_estimate.pdf 'Differentially private ANOVA, MSE estimate of variance'

cat ARtest_realvar_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_12counts.csv tmp_realvar.csv > ARtest_realvar_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv
python3 csvreader.py ARtest_realvar_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv AR_realvar.pdf 'Differentially private ANOVA, ground truth variance'

cat ARtest_noisy_1000runs_6means_0.20var_5epsilons_12counts.csv tmp_noisy.csv | awk -F"," '($4!=0.01){print $0}' > ARtest_noisy_1000runs_6means_0.20var_5epsilons_15counts.csv
python3 csvreader.py ARtest_noisy_1000runs_6means_0.20var_5epsilons_15counts.csv AR_noisy.pdf 'ANOVA with smaller effect size'

## Making a list of plotted values

```
python3 csvreader.py ARtest_estimate_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv AR_estimate.png 'Differentially private ANOVA, MSE estimate of variance' > plotted_values.txt
python3 csvreader.py ARtest_realvar_1000runs_0.35m1_0.50m2_0.65m3_0.15var_5epsilons_16counts.csv AR_realvar.png 'Differentially private ANOVA, ground truth variance' >> plotted_values.txt
python3 csvreader.py ARtest_noisy_1000runs_6means_0.20var_5epsilons_15counts.csv AR_noisy.png 'ANOVA with smaller effect size' >> plotted_values.txt
```