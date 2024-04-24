from json import load, dump

def load_files():
    try:
        with open('data/config.json') as fp:
            config = load(fp)

        file_path_dict = config['PRICINGS']
        invoice_info = config['INVOICE']
        pricings = {}

        for key, path in file_path_dict.items():
            pricings[key] = load_json(path)

        return (pricings, invoice_info)
    except Exception as e:
        raise e

def load_json(path):
    with open(path) as dct:
        json = load(dct)
    return json

def save_local_pricing(pricing):
    with open('data/local_pricing.json', 'w') as fp:
        dump(pricing, fp, indent=4)