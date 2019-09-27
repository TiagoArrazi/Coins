from src.utils.coint_distributor import Distributor


if __name__ == '__main__':
    while True:
        try:
            print(Distributor.distribute(value=float(input('Insert your value: '))))

        except ValueError:
            print('Invalid input!')