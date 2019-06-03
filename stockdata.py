from yahoo_fin import options

def get_exp_date(ticker):
    exp_date = options.get_expiration_dates(ticker)
    print(exp_date)
    return exp_date

def get_opt_chain(ticker, exp_date):
    date = None
    if exp_date is not None:
        date = exp_date
    opt_chain = options.get_options_chain(ticker, date)
   # print(opt_chain)
    return opt_chain

def get_calls(ticker, exp_date):
    opt_call = get_opt_chain(ticker, exp_date)["calls"].head()
#    opt_call = get_calls(ticker, None)
    print(opt_call)
    return opt_call

def get_puts(ticker, exp_date):
    opt_put = get_opt_chain(ticker, exp_date)["puts"].head()
    print(opt_put)
    return opt_put

get_calls("amzn", None)