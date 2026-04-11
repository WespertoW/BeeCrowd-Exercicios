from statistics import fmean


A=float(input())
B=float(input())
C=float(input())


print(f"MEDIA = {fmean([A,B,C], weights=[2,3,5]):.1f}")