from datetime import datetime

class Stock:
  def __init__(self, symbol):
    self.symbol = symbol
    self.current_price = 3

  def price(self, date):
    # Simulate stock price
    pass

class Portfolio:
  def __init__(self):
    self.stocks = {}

  def add_stock(self, stock: Stock, quantity: int):
    if stock.symbol in self.stocks:
      self.stocks[stock.symbol]['quantity'] += quantity
    else:
      self.stocks[stock.symbol] = {'stock': stock, 'quantity': quantity}

  def profit(self, start_date: str, end_date: str):
    """
      Return the profit of the portfolio between two dates. The profit
      is expressed in absolute terms, as a percentage of the starting
      portfolio value and as an annualized percentage.
        
      :param start_date: Start date in 'YYYY-MM-DD' format.
      :param end_date: End date in 'YYYY-MM-DD' format.
      :return: Dict with the different expressions of the profit.
    """
    if not isinstance(start_date, str) or not isinstance(end_date, str):
      raise TypeError("Dates must be strings")

    profit = 0
    starting_portfolio_value = 0
    ending_portfolio_value = 0

    formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d")
    formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d")
    days_in_period = (formatted_end_date - formatted_start_date).days
    years_in_period = days_in_period / 365

    for stock in self.stocks.values():
      starting_price = stock['stock'].price(start_date)
      end_price = stock['stock'].price(end_date)

      starting_portfolio_value += starting_price * stock['quantity']
      ending_portfolio_value += end_price * stock['quantity']
      profit += stock['quantity'] * (end_price - starting_price)

    profit_percentage = (profit / starting_portfolio_value)

    annualized_profit = 0
    if years_in_period > 0:
      annualized_profit = (ending_portfolio_value/starting_portfolio_value) ** (1 / years_in_period) - 1

    return {"profit": profit, "profit_percentage": profit_percentage * 100, "annualized_return": annualized_profit * 100}
  
## Example usage
if __name__ == "__main__":
  portfolio = Portfolio()
  portfolio.add_stock(Stock("AAPL"), 10)
  portfolio.add_stock(Stock("GOOGL"), 5)

  print(portfolio.profit("2020-01-01", "2021-01-01"))
