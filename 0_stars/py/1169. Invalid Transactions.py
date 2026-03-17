# https://leetcode.com/problems/invalid-transactions/solutions/6318435/intuitive-to-understand-by-ybaleri-i75f/

# iterate by transaction and name instead of 2 loops over transaction times.

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = defaultdict(list)  # Mapping of names to their transaction details.
        idx = set()  # Set of indices of possibly invalid transactions.

        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(",")
            time, amount = int(time), int(amount)
            d[name].append((time, city, i))
          
            # Check if the transaction amount exceeds $1000.
            if amount > 1000:
                idx.add(i)
              
            # Check for transactions with the same name in different cities within 60 minutes.
            for t, c, j in d[name]:
                if c != city and abs(time - t) <= 60:
                    idx.add(i)
                    idx.add(j)

        # Generate a list of transactions that are possibly invalid.
        return [transactions[i] for i in idx]