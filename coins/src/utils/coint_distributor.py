

class Distributor:

    @classmethod
    def distribute(cls, value):

        try:
            value = value * 100

            coin_list = [100, 50, 25, 10, 5, 1]
            distribution = list()
            distribution_dict = dict()

            for coin in coin_list:
                quotient, remaining = divmod(value, coin)
                distribution.append(quotient)
                value = round(remaining, 2)

            [distribution_dict.update({coin / 100: int(dist)}) for coin, dist in zip(coin_list, distribution)]

            return distribution_dict

        except ValueError:
            return False
