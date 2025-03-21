r1, r2, rb = map(int, input("Enter r1, r2, rb : ").split())

po = (300 - rb) / 6
crr = r2 / po

ro = rb / 6
rrr = ((r1 + 1) - r2) / ro

print(f"Current run rate: {crr:.2f} Required run rate: {rrr:.2f}")