from scipy import special
x = 5
print("Gamma Function of 5:", special.gamma(x))
print("Log Gamma Function of 5:", special.gammaln(x))
y = 1.5
print("\nError Function erf(1.5):", special.erf(y))
print("Complementary Error Function erfc(1.5):", special.erfc(y))
z = 2.5
print("\nBessel Function J0(2.5):", special.jv(0, z))
print("Bessel Function J1(2.5):", special.jv(1, z))
a, b = 2, 3
print("\nBeta Function B(2,3):", special.beta(a, b))
n, k = 5, 2
print("\nCombination (5 choose 2):", special.comb(n, k))
print("Permutation (5 permute 2):", special.perm(n, k))
r = 1.0
print("\nSpherical Bessel j0(1.0):", special.spherical_jn(0, r))
t = 1.0
print("\nSine Integral Si(1.0):", special.sici(t)[0])
print("Cosine Integral Ci(1.0):", special.sici(t)[1])

