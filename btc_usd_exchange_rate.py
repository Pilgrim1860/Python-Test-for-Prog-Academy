btc_usd = float(input('What is Bitcoin price today?\n'))  #btc/usd rate
usd_value = int(input('How much $ do you have?\n'))  # amount of usd
print(f'You can buy {usd_value / btc_usd:.7}')
