def format_data(account):
    """ Toma los datos de la cuenta y devuelve el formato imprimible. """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
    