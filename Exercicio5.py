from statistics import fmean


A = float(input())
B = float(input())

print(f"MEDIA = {fmean([A, B], weights=[3.5, 7.5]):.5f}")