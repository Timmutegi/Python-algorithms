class Solution:
    def find_prime_factors(self, num):
        factors = []
        divisor = 2

        while divisor <= num:
            if num % divisor == 0:
                factors.append(divisor)
                num = num // divisor
            else:
                divisor += 1

        return factors


print(Solution().find_prime_factors(630))

